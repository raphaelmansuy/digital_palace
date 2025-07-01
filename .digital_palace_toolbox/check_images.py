#!/usr/bin/env python3
"""
Digital Palace Image Asset Checker

Validates that all referenced images in markdown files exist and are accessible.
Provides comprehensive reporting on missing images, broken image links, and optimization suggestions.

Usage:
    python check_images.py [files/directories] [--format json|markdown|text]
    python check_images.py README.md
    python check_images.py guides/ --format json
    python check_images.py --all --format markdown

Author: Digital Palace Toolbox
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict
from urllib.parse import urlparse
import requests
from PIL import Image
import hashlib

@dataclass
class ImageIssue:
    """Represents an image validation issue"""
    file_path: str
    line_number: int
    image_text: str
    image_url: str
    issue_type: str
    description: str
    severity: str  # 'error', 'warning', 'info'
    file_size: Optional[int] = None
    dimensions: Optional[tuple] = None
    suggested_fix: Optional[str] = None

@dataclass
class ImageCheckResult:
    """Results of image checking operation"""
    total_files_checked: int
    total_images_found: int
    total_issues: int
    issues: List[ImageIssue]
    summary: Dict[str, int]

class ImageChecker:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()
        self.checked_images = {}  # Cache for image checks
        self.session = requests.Session()
        
    def find_images_in_content(self, content: str, file_path: Path) -> List[tuple]:
        """Find all image references in markdown content"""
        images = []
        
        # Pattern for markdown images ![alt](src)
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        for match in re.finditer(image_pattern, content):
            alt_text = match.group(1)
            image_url = match.group(2)
            line_num = content[:match.start()].count('\n') + 1
            images.append((alt_text, image_url, line_num))
        
        # Pattern for HTML img tags
        html_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'
        for match in re.finditer(html_pattern, content):
            image_url = match.group(1)
            line_num = content[:match.start()].count('\n') + 1
            images.append(("", image_url, line_num))
        
        return images
    
    def resolve_image_path(self, current_file: Path, image_path: str) -> Path:
        """Resolve relative image path"""
        if image_path.startswith('http'):
            return None  # External URL
        
        # Handle relative paths
        if image_path.startswith('./'):
            image_path = image_path[2:]
        elif image_path.startswith('../'):
            # Relative to parent directory
            return (current_file.parent / image_path).resolve()
        
        # Relative to current file's directory
        return (current_file.parent / image_path).resolve()
    
    def check_local_image(self, image_path: Path) -> Dict:
        """Check if local image exists and get metadata"""
        if not image_path.exists():
            return {
                'exists': False,
                'issue': 'file_not_found',
                'description': f'Image file not found: {image_path}'
            }
        
        try:
            # Get file size
            file_size = image_path.stat().st_size
            
            # Get image dimensions
            with Image.open(image_path) as img:
                dimensions = img.size
                format_type = img.format
            
            # Check for optimization opportunities
            issues = []
            if file_size > 1024 * 1024:  # > 1MB
                issues.append('large_file_size')
            
            if dimensions[0] > 2000 or dimensions[1] > 2000:
                issues.append('large_dimensions')
            
            return {
                'exists': True,
                'file_size': file_size,
                'dimensions': dimensions,
                'format': format_type,
                'optimization_issues': issues
            }
            
        except Exception as e:
            return {
                'exists': True,
                'issue': 'invalid_image',
                'description': f'Invalid image file: {e}'
            }
    
    def check_external_image(self, image_url: str) -> Dict:
        """Check if external image is accessible"""
        try:
            response = self.session.head(image_url, timeout=10)
            
            result = {
                'accessible': response.status_code == 200,
                'status_code': response.status_code,
                'content_type': response.headers.get('content-type', ''),
                'content_length': response.headers.get('content-length', 0)
            }
            
            if response.status_code != 200:
                result['issue'] = f'HTTP {response.status_code}'
                result['description'] = f'External image returned status {response.status_code}'
            
            return result
            
        except Exception as e:
            return {
                'accessible': False,
                'issue': 'connection_error',
                'description': f'Failed to access external image: {e}'
            }
    
    def check_file(self, file_path: str) -> Dict:
        """Check images in a single markdown file"""
        file_path = Path(file_path)
        
        if not file_path.exists():
            return {
                'file': str(file_path),
                'error': f'File does not exist: {file_path}',
                'issues': [],
                'stats': {'total_images': 0, 'broken_images': 0, 'valid_images': 0}
            }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {
                'file': str(file_path),
                'error': f'Could not read file: {e}',
                'issues': [],
                'stats': {'total_images': 0, 'broken_images': 0, 'valid_images': 0}
            }
        
        # Find all images
        images = self.find_images_in_content(content, file_path)
        issues = []
        
        for alt_text, image_url, line_num in images:
            issue = {
                'line': line_num,
                'image_text': alt_text,
                'image_url': image_url,
                'issue_type': None,
                'severity': 'info',
                'description': '',
                'suggested_fix': None
            }
            
            if image_url.startswith('http'):
                # External image
                check_result = self.check_external_image(image_url)
                if not check_result.get('accessible', False):
                    issue['issue_type'] = 'external_image_error'
                    issue['severity'] = 'error'
                    issue['description'] = check_result.get('description', 'External image not accessible')
                else:
                    issue['issue_type'] = 'valid_external'
                    issue['description'] = 'External image accessible'
            else:
                # Local image
                image_path = self.resolve_image_path(file_path, image_url)
                if image_path is None:
                    issue['issue_type'] = 'invalid_path'
                    issue['severity'] = 'error'
                    issue['description'] = 'Invalid image path'
                else:
                    check_result = self.check_local_image(image_path)
                    if not check_result.get('exists', False):
                        issue['issue_type'] = 'missing_image'
                        issue['severity'] = 'error'
                        issue['description'] = check_result.get('description', 'Image file not found')
                        
                        # Suggest similar images
                        suggested = self.find_similar_images(image_path)
                        if suggested:
                            issue['suggested_fix'] = f'Similar images found: {", ".join(suggested)}'
                    elif 'issue' in check_result:
                        issue['issue_type'] = check_result['issue']
                        issue['severity'] = 'error'
                        issue['description'] = check_result['description']
                    else:
                        issue['issue_type'] = 'valid_local'
                        issue['description'] = 'Local image exists'
                        
                        # Check for optimization opportunities
                        opt_issues = check_result.get('optimization_issues', [])
                        if opt_issues:
                            issue['severity'] = 'warning'
                            issue['description'] += f' (Optimization: {", ".join(opt_issues)})'
                            
                            if 'large_file_size' in opt_issues:
                                issue['suggested_fix'] = 'Consider compressing image or using WebP format'
            
            issues.append(issue)
        
        # Calculate stats
        total_images = len(issues)
        broken_images = len([i for i in issues if i['severity'] == 'error'])
        valid_images = total_images - broken_images
        
        return {
            'file': str(file_path.relative_to(self.base_path)),
            'issues': issues,
            'stats': {
                'total_images': total_images,
                'broken_images': broken_images,
                'valid_images': valid_images
            }
        }
    
    def find_similar_images(self, missing_path: Path) -> List[str]:
        """Find similar image files in the directory"""
        if not missing_path.parent.exists():
            return []
        
        missing_name = missing_path.stem.lower()
        similar = []
        
        for file in missing_path.parent.iterdir():
            if file.is_file() and file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']:
                if missing_name in file.stem.lower() or file.stem.lower() in missing_name:
                    similar.append(file.name)
        
        return similar[:3]  # Return top 3 matches
    
    def check_files(self, file_paths: List[str]) -> Dict:
        """Check multiple files and generate comprehensive report"""
        print(f"🖼️ Checking images in {len(file_paths)} files...")
        
        results = []
        total_stats = {'total_images': 0, 'broken_images': 0, 'valid_images': 0, 'files_checked': 0}
        
        for file_path in file_paths:
            if not file_path.endswith('.md'):
                continue
                
            result = self.check_file(file_path)
            results.append(result)
            
            # Update total stats
            if 'stats' in result:
                total_stats['total_images'] += result['stats']['total_images']
                total_stats['broken_images'] += result['stats']['broken_images']
                total_stats['valid_images'] += result['stats']['valid_images']
                total_stats['files_checked'] += 1
        
        return {
            'summary': {
                'timestamp': self.get_timestamp(),
                'base_path': str(self.base_path),
                'total_stats': total_stats
            },
            'results': results
        }
    
    def get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def generate_report(self, report_data: Dict, format: str = 'text') -> str:
        """Generate formatted report"""
        if format == 'json':
            return json.dumps(report_data, indent=2)
        elif format == 'markdown':
            return self.generate_markdown_report(report_data)
        else:
            return self.generate_text_report(report_data)
    
    def generate_text_report(self, report_data: Dict) -> str:
        """Generate plain text report"""
        lines = []
        lines.append("🖼️ IMAGE CHECKER REPORT")
        lines.append("=" * 50)
        
        summary = report_data['summary']
        lines.append(f"📅 Timestamp: {summary['timestamp']}")
        lines.append(f"📁 Base Path: {summary['base_path']}")
        lines.append("")
        
        stats = summary['total_stats']
        lines.append("📊 OVERALL STATISTICS")
        lines.append(f"Files Checked: {stats['files_checked']}")
        lines.append(f"Total Images: {stats['total_images']}")
        lines.append(f"Valid Images: {stats['valid_images']}")
        lines.append(f"Broken Images: {stats['broken_images']}")
        
        if stats['total_images'] > 0:
            success_rate = (stats['valid_images'] / stats['total_images']) * 100
            lines.append(f"Success Rate: {success_rate:.1f}%")
        
        lines.append("")
        
        # Issues by file
        for result in report_data['results']:
            lines.append(f"📄 FILE: {result['file']}")
            lines.append("-" * 40)
            
            if 'error' in result:
                lines.append(f"❌ ERROR: {result['error']}")
                lines.append("")
                continue
            
            file_stats = result['stats']
            lines.append(f"Images: {file_stats['total_images']} | Valid: {file_stats['valid_images']} | Broken: {file_stats['broken_images']}")
            
            if file_stats['broken_images'] > 0:
                lines.append("")
                lines.append("🚨 ISSUES FOUND:")
                
                for issue in result['issues']:
                    if issue['severity'] in ['error', 'warning']:
                        severity_icon = "❌" if issue['severity'] == 'error' else "⚠️"
                        lines.append(f"{severity_icon} Line {issue['line']}: {issue['issue_type'].upper()}")
                        lines.append(f"   Image: ![{issue['image_text']}]({issue['image_url']})")
                        lines.append(f"   Issue: {issue['description']}")
                        
                        if issue['suggested_fix']:
                            lines.append(f"   Fix: {issue['suggested_fix']}")
                        lines.append("")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def generate_markdown_report(self, report_data: Dict) -> str:
        """Generate markdown report"""
        lines = []
        lines.append("# 🖼️ Image Checker Report")
        lines.append("")
        
        summary = report_data['summary']
        lines.append(f"**Timestamp:** {summary['timestamp']}")
        lines.append(f"**Base Path:** `{summary['base_path']}`")
        lines.append("")
        
        stats = summary['total_stats']
        lines.append("## 📊 Overall Statistics")
        lines.append("")
        lines.append(f"- **Files Checked:** {stats['files_checked']}")
        lines.append(f"- **Total Images:** {stats['total_images']}")
        lines.append(f"- **Valid Images:** {stats['valid_images']}")
        lines.append(f"- **Broken Images:** {stats['broken_images']}")
        
        if stats['total_images'] > 0:
            success_rate = (stats['valid_images'] / stats['total_images']) * 100
            lines.append(f"- **Success Rate:** {success_rate:.1f}%")
        
        lines.append("")
        
        # File summary table
        lines.append("## 📋 File Summary")
        lines.append("")
        lines.append("| File | Total Images | Valid | Broken | Status |")
        lines.append("|------|--------------|-------|--------|--------|")
        
        for result in report_data['results']:
            if 'error' in result:
                lines.append(f"| `{result['file']}` | - | - | - | ❌ Error |")
            else:
                stats = result['stats']
                status = "✅ Clean" if stats['broken_images'] == 0 else f"⚠️ {stats['broken_images']} issues"
                lines.append(f"| `{result['file']}` | {stats['total_images']} | {stats['valid_images']} | {stats['broken_images']} | {status} |")
        
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description='Check images in markdown files')
    parser.add_argument('files', nargs='+', help='Markdown files to check')
    parser.add_argument('--format', choices=['text', 'json', 'markdown'], default='text',
                        help='Output format (default: text)')
    parser.add_argument('--output', help='Output file (default: stdout)')
    parser.add_argument('--base-path', help='Base path for relative paths (default: current directory)')
    
    args = parser.parse_args()
    
    # Determine base path
    if args.base_path:
        base_path = args.base_path
    else:
        base_path = Path(args.files[0]).parent
    
    # Check files
    checker = ImageChecker(base_path)
    report_data = checker.check_files(args.files)
    
    # Generate report
    report = checker.generate_report(report_data, args.format)
    
    # Output report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)
    
    # Exit with error code if there are broken images
    total_broken = report_data['summary']['total_stats']['broken_images']
    if total_broken > 0:
        print(f"\n❌ Found {total_broken} broken images", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"\n✅ All images are valid!", file=sys.stderr)

if __name__ == '__main__':
    main()

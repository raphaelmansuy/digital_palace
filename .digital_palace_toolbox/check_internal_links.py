#!/usr/bin/env python3
"""
Digital Palace Internal Link Checker

This script checks internal links within markdown files in the Digital Palace repository.
It validates that:
- Linked files exist
- Section anchors exist in target files
- Relative paths are correct
- Cross-references are valid

Usage:
    python check_internal_links.py [file_or_directory] [--format json|markdown|text]
    python check_internal_links.py README.md
    python check_internal_links.py guides/ --format json
    python check_internal_links.py --all --format markdown

Author: Digital Palace Toolbox
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from urllib.parse import unquote

@dataclass
class LinkIssue:
    """Represents a link validation issue"""
    file_path: str
    line_number: int
    link_text: str
    link_target: str
    issue_type: str
    description: str
    severity: str  # 'error', 'warning', 'info'
    suggested_fix: Optional[str] = None

@dataclass
class LinkCheckResult:
    """Results of link checking operation"""
    total_files_checked: int
    total_links_found: int
    total_issues: int
    issues: List[LinkIssue]
    summary: Dict[str, int]

class InternalLinkChecker:
    """Checks internal links in markdown files"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()
        self.issues: List[LinkIssue] = []
        
        # Regex patterns
        self.markdown_link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
        self.section_anchor_pattern = re.compile(r'^#+\s+(.+)$', re.MULTILINE)
        
    def check_files(self, paths: List[str]) -> LinkCheckResult:
        """Check internal links in specified files/directories"""
        files_to_check = self._collect_markdown_files(paths)
        total_links = 0
        
        for file_path in files_to_check:
            links_in_file = self._check_file(file_path)
            total_links += links_in_file
            
        # Generate summary
        summary = self._generate_summary()
        
        return LinkCheckResult(
            total_files_checked=len(files_to_check),
            total_links_found=total_links,
            total_issues=len(self.issues),
            issues=self.issues,
            summary=summary
        )
    
    def _collect_markdown_files(self, paths: List[str]) -> List[Path]:
        """Collect all markdown files from given paths"""
        files = []
        
        for path_str in paths:
            path = Path(path_str)
            if not path.is_absolute():
                path = self.base_path / path
                
            if path.is_file() and path.suffix.lower() in ['.md', '.markdown']:
                files.append(path)
            elif path.is_dir():
                files.extend(path.rglob('*.md'))
                files.extend(path.rglob('*.markdown'))
                
        return sorted(set(files))
    
    def _check_file(self, file_path: Path) -> int:
        """Check internal links in a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.issues.append(LinkIssue(
                file_path=str(file_path.relative_to(self.base_path)),
                line_number=1,
                link_text="",
                link_target="",
                issue_type="file_read_error",
                description=f"Could not read file: {e}",
                severity="error"
            ))
            return 0
            
        lines = content.split('\n')
        links_found = 0
        
        for line_num, line in enumerate(lines, 1):
            matches = self.markdown_link_pattern.findall(line)
            
            for link_text, link_target in matches:
                links_found += 1
                self._validate_internal_link(
                    file_path, line_num, link_text, link_target
                )
                
        return links_found
    
    def _validate_internal_link(self, source_file: Path, line_num: int, 
                               link_text: str, link_target: str):
        """Validate a single internal link"""
        # Skip external links
        if self._is_external_link(link_target):
            return
            
        # Parse the link target
        if '#' in link_target:
            file_part, anchor_part = link_target.split('#', 1)
        else:
            file_part, anchor_part = link_target, None
            
        # Handle same-file references
        if not file_part:
            target_file = source_file
        else:
            # Resolve relative path
            target_file = self._resolve_relative_path(source_file, file_part)
            
        # Check if target file exists
        if not target_file.exists():
            self.issues.append(LinkIssue(
                file_path=str(source_file.relative_to(self.base_path)),
                line_number=line_num,
                link_text=link_text,
                link_target=link_target,
                issue_type="missing_file",
                description=f"Target file does not exist: {self._safe_relative_path(target_file)}",
                severity="error",
                suggested_fix=self._suggest_file_fix(target_file)
            ))
            return
            
        # Check anchor if present
        if anchor_part:
            self._validate_anchor(source_file, line_num, link_text, link_target, 
                                target_file, anchor_part)
    
    def _validate_anchor(self, source_file: Path, line_num: int, link_text: str,
                        link_target: str, target_file: Path, anchor: str):
        """Validate that an anchor exists in the target file"""
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.issues.append(LinkIssue(
                file_path=str(source_file.relative_to(self.base_path)),
                line_number=line_num,
                link_text=link_text,
                link_target=link_target,
                issue_type="anchor_check_error",
                description=f"Could not read target file to check anchor: {e}",
                severity="warning"
            ))
            return
            
        # Extract all headers from the target file
        headers = self._extract_headers(content)
        
        # Convert anchor to the format used in markdown
        expected_anchors = self._generate_anchor_variants(anchor)
        
        # Check if any variant matches
        found_match = False
        for header_anchor in headers:
            if header_anchor in expected_anchors:
                found_match = True
                break
                
        if not found_match:
            closest_match = self._find_closest_header(anchor, headers)
            suggested_fix = f"#{closest_match}" if closest_match else None
            
            self.issues.append(LinkIssue(
                file_path=str(source_file.relative_to(self.base_path)),
                line_number=line_num,
                link_text=link_text,
                link_target=link_target,
                issue_type="missing_anchor",
                description=f"Anchor '{anchor}' not found in {self._safe_relative_path(target_file)}",
                severity="error",
                suggested_fix=suggested_fix
            ))
    
    def _extract_headers(self, content: str) -> List[str]:
        """Extract header anchors from markdown content"""
        headers = []
        matches = self.section_anchor_pattern.findall(content)
        
        for header_text in matches:
            # Convert header text to anchor format
            anchor = self._text_to_anchor(header_text.strip())
            headers.append(anchor)
            
        return headers
    
    def _text_to_anchor(self, text: str) -> str:
        """Convert header text to GitHub-style anchor"""
        # Remove markdown formatting
        text = re.sub(r'[*_`]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Replace spaces and special chars with hyphens
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'[\s_]+', '-', text)
        # Remove leading/trailing hyphens
        text = text.strip('-')
        return text
    
    def _generate_anchor_variants(self, anchor: str) -> List[str]:
        """Generate possible anchor variants"""
        variants = [anchor]
        
        # URL decode
        decoded = unquote(anchor)
        if decoded != anchor:
            variants.append(decoded)
            
        # Remove leading # if present
        if anchor.startswith('#'):
            variants.append(anchor[1:])
            
        # Convert spaces to hyphens
        variants.append(anchor.replace(' ', '-'))
        variants.append(anchor.replace('_', '-'))
        
        # Lowercase variants
        variants.extend([v.lower() for v in variants])
        
        return list(set(variants))
    
    def _find_closest_header(self, target_anchor: str, headers: List[str]) -> Optional[str]:
        """Find the closest matching header"""
        if not headers:
            return None
            
        target_lower = target_anchor.lower()
        best_match = None
        best_score = 0
        
        for header in headers:
            # Simple similarity check
            score = self._calculate_similarity(target_lower, header.lower())
            if score > best_score:
                best_score = score
                best_match = header
                
        return best_match if best_score > 0.5 else None
    
    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """Calculate simple similarity between two strings"""
        if not str1 or not str2:
            return 0.0
            
        # Simple character overlap ratio
        set1 = set(str1.replace('-', '').replace('_', ''))
        set2 = set(str2.replace('-', '').replace('_', ''))
        
        if not set1 or not set2:
            return 0.0
            
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def _resolve_relative_path(self, source_file: Path, relative_path: str) -> Path:
        """Resolve relative path from source file"""
        # Handle URL encoding
        relative_path = unquote(relative_path)
        
        # Remove query parameters and fragments
        if '?' in relative_path:
            relative_path = relative_path.split('?')[0]
        if '#' in relative_path:
            relative_path = relative_path.split('#')[0]
            
        # Resolve relative to source file's directory
        source_dir = source_file.parent
        target_path = (source_dir / relative_path).resolve()
        
        return target_path
    
    def _safe_relative_path(self, path: Path) -> str:
        """Safely get relative path, handling cases where path is outside base_path"""
        try:
            return str(path.relative_to(self.base_path))
        except ValueError:
            # Path is outside base_path, return absolute path
            return str(path)
    
    def _is_external_link(self, link: str) -> bool:
        """Check if link is external (HTTP/HTTPS)"""
        return link.startswith(('http://', 'https://', 'mailto:', 'ftp://'))
    
    def _suggest_file_fix(self, missing_file: Path) -> Optional[str]:
        """Suggest a fix for missing file"""
        # Look for similar files
        target_name = missing_file.name.lower()
        target_dir = missing_file.parent
        
        if target_dir.exists():
            for file in target_dir.iterdir():
                if file.is_file() and file.suffix.lower() in ['.md', '.markdown']:
                    if file.name.lower() == target_name:
                        return self._safe_relative_path(file)
                        
        # Look for files with similar names
        base_name = missing_file.stem.lower()
        for file in self.base_path.rglob('*.md'):
            if file.stem.lower() == base_name:
                return self._safe_relative_path(file)
                
        return None
    
    def _generate_summary(self) -> Dict[str, int]:
        """Generate summary statistics"""
        summary = {
            'total_issues': len(self.issues),
            'errors': len([i for i in self.issues if i.severity == 'error']),
            'warnings': len([i for i in self.issues if i.severity == 'warning']),
            'info': len([i for i in self.issues if i.severity == 'info']),
        }
        
        # Count by issue type
        issue_types = {}
        for issue in self.issues:
            issue_types[issue.issue_type] = issue_types.get(issue.issue_type, 0) + 1
        summary['by_type'] = issue_types
        
        return summary

class ReportFormatter:
    """Format link check results in different formats"""
    
    @staticmethod
    def format_json(result: LinkCheckResult) -> str:
        """Format results as JSON"""
        return json.dumps(asdict(result), indent=2, ensure_ascii=False)
    
    @staticmethod
    def format_markdown(result: LinkCheckResult) -> str:
        """Format results as Markdown"""
        md = []
        md.append("# 🔗 Internal Link Check Report")
        md.append("")
        md.append(f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md.append("")
        
        # Summary
        md.append("## 📊 Summary")
        md.append("")
        md.append(f"- **Files checked:** {result.total_files_checked}")
        md.append(f"- **Links found:** {result.total_links_found}")
        md.append(f"- **Issues found:** {result.total_issues}")
        md.append(f"- **Errors:** {result.summary.get('errors', 0)}")
        md.append(f"- **Warnings:** {result.summary.get('warnings', 0)}")
        md.append("")
        
        if result.summary.get('by_type'):
            md.append("### Issues by Type")
            md.append("")
            for issue_type, count in result.summary['by_type'].items():
                md.append(f"- **{issue_type.replace('_', ' ').title()}:** {count}")
            md.append("")
        
        # Issues detail
        if result.issues:
            md.append("## 🐛 Issues Found")
            md.append("")
            
            # Group by severity
            errors = [i for i in result.issues if i.severity == 'error']
            warnings = [i for i in result.issues if i.severity == 'warning']
            
            if errors:
                md.append("### ❌ Errors")
                md.append("")
                for issue in errors:
                    md.append(f"**{issue.file_path}:{issue.line_number}**")
                    md.append(f"- Link: `[{issue.link_text}]({issue.link_target})`")
                    md.append(f"- Issue: {issue.description}")
                    if issue.suggested_fix:
                        md.append(f"- 💡 Suggested fix: `{issue.suggested_fix}`")
                    md.append("")
            
            if warnings:
                md.append("### ⚠️ Warnings")
                md.append("")
                for issue in warnings:
                    md.append(f"**{issue.file_path}:{issue.line_number}**")
                    md.append(f"- Link: `[{issue.link_text}]({issue.link_target})`")
                    md.append(f"- Issue: {issue.description}")
                    if issue.suggested_fix:
                        md.append(f"- 💡 Suggested fix: `{issue.suggested_fix}`")
                    md.append("")
        else:
            md.append("## ✅ No Issues Found")
            md.append("")
            md.append("All internal links are valid!")
        
        md.append("---")
        md.append("*Report generated by Digital Palace Internal Link Checker*")
        
        return "\n".join(md)
    
    @staticmethod
    def format_text(result: LinkCheckResult) -> str:
        """Format results as plain text"""
        lines = []
        lines.append("INTERNAL LINK CHECK REPORT")
        lines.append("=" * 30)
        lines.append("")
        
        lines.append(f"Files checked: {result.total_files_checked}")
        lines.append(f"Links found: {result.total_links_found}")
        lines.append(f"Issues found: {result.total_issues}")
        lines.append(f"Errors: {result.summary.get('errors', 0)}")
        lines.append(f"Warnings: {result.summary.get('warnings', 0)}")
        lines.append("")
        
        if result.issues:
            lines.append("ISSUES:")
            lines.append("-" * 20)
            for i, issue in enumerate(result.issues, 1):
                lines.append(f"{i}. [{issue.severity.upper()}] {issue.file_path}:{issue.line_number}")
                lines.append(f"   Link: [{issue.link_text}]({issue.link_target})")
                lines.append(f"   Issue: {issue.description}")
                if issue.suggested_fix:
                    lines.append(f"   Fix: {issue.suggested_fix}")
                lines.append("")
        else:
            lines.append("✅ No issues found!")
        
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Check internal links in Digital Palace markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s README.md                    # Check single file
  %(prog)s guides/ tools/               # Check directories
  %(prog)s --all                        # Check entire repository
  %(prog)s README.md --format json      # Output as JSON
  %(prog)s guides/ --format markdown    # Output as Markdown report
        """
    )
    
    parser.add_argument(
        'paths',
        nargs='*',
        help='Files or directories to check (default: current directory)'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Check all markdown files in the repository'
    )
    
    parser.add_argument(
        '--format',
        choices=['json', 'markdown', 'text'],
        default='text',
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--output',
        help='Output file (default: stdout)'
    )
    
    parser.add_argument(
        '--base-path',
        help='Base path for the repository (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Determine base path
    base_path = args.base_path or os.getcwd()
    
    # Determine paths to check
    if args.all:
        paths = [base_path]
    elif args.paths:
        paths = args.paths
    else:
        paths = ['.']
    
    # Run the check
    checker = InternalLinkChecker(base_path)
    result = checker.check_files(paths)
    
    # Format output
    if args.format == 'json':
        output = ReportFormatter.format_json(result)
    elif args.format == 'markdown':
        output = ReportFormatter.format_markdown(result)
    else:
        output = ReportFormatter.format_text(result)
    
    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Report written to: {args.output}")
    else:
        print(output)
    
    # Exit with error code if issues found
    if result.summary.get('errors', 0) > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()

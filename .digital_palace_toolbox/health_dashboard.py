#!/usr/bin/env python3
"""
Digital Palace Documentation Health Dashboard

Generates a comprehensive health report for the Digital Palace repository,
including link integrity, content metrics, and actionable insights.

Usage:
    python health_dashboard.py [--format html|json|text] [--output report.html]
    python health_dashboard.py --generate-html --open-browser
    python health_dashboard.py --json-only --output health.json

Author: Digital Palace Toolbox
"""

import argparse
import json
import subprocess
import sys
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class HealthDashboard:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()
        self.toolbox_path = self.base_path / '.digital_palace_toolbox'
        self.health_data = {}
        
    def collect_health_metrics(self) -> Dict:
        """Collect comprehensive health metrics with visible progression"""
        print("📊 Collecting health metrics...")
        
        print("  1️⃣  Gathering file metrics...")
        file_metrics = self.get_file_metrics()
        print(f"    ✔️  {file_metrics.get('total_markdown_files', 0)} markdown files in {file_metrics.get('total_directories', 0)} directories.")
        
        print("  2️⃣  Checking link health...")
        link_health = self.get_link_health()
        if 'error' not in link_health.get('internal', {}):
            print(f"    ✔️  Internal links checked: {link_health['internal'].get('total_links', 0)} (broken: {link_health['internal'].get('broken_links', 0)})")
        else:
            print("    ⚠️  Internal link check failed.")
        if 'error' not in link_health.get('external', {}):
            print(f"    ✔️  External links checked: {link_health['external'].get('total_links', 0)} (errors: {link_health['external'].get('errors', 0)})")
        else:
            print("    ⚠️  External link check failed.")
        
        print("  3️⃣  Analyzing content quality...")
        content_metrics = self.get_content_metrics()
        print(f"    ✔️  {content_metrics.get('readme_files', 0)} README files, {content_metrics.get('files_with_toc', 0)} files with TOC, {content_metrics.get('files_with_images', 0)} files with images.")
        
        health_data = {
            'timestamp': datetime.now().isoformat(),
            'repository': {
                'path': str(self.base_path),
                'name': self.base_path.name
            },
            'file_metrics': file_metrics,
            'link_health': link_health,
            'content_metrics': content_metrics,
            'quality_scores': {},
            'recommendations': []
        }
        
        print("  4️⃣  Calculating quality scores...")
        health_data['quality_scores'] = self.calculate_quality_scores(health_data)
        print(f"    ✔️  Overall health score: {health_data['quality_scores'].get('overall', 0)}%")
        
        print("  5️⃣  Generating recommendations...")
        health_data['recommendations'] = self.generate_recommendations(health_data)
        print(f"    ✔️  {len(health_data['recommendations'])} recommendations generated.")
        
        self.health_data = health_data
        print("✅ Health metrics collection complete.")
        return health_data
    
    def get_file_metrics(self) -> Dict:
        """Get file and directory metrics"""
        print("  📁 Analyzing file structure...")
        
        md_files = list(self.base_path.rglob('*.md'))
        # Exclude toolbox files
        md_files = [f for f in md_files if not f.is_relative_to(self.toolbox_path)]
        
        directories = set()
        total_size = 0
        
        for md_file in md_files:
            directories.add(md_file.parent)
            total_size += md_file.stat().st_size
        
        return {
            'total_markdown_files': len(md_files),
            'total_directories': len(directories),
            'total_size_bytes': total_size,
            'total_size_mb': round(total_size / 1024 / 1024, 2),
            'files_by_directory': self.get_files_by_directory(md_files),
            'largest_files': self.get_largest_files(md_files)
        }
    
    def get_files_by_directory(self, md_files: List[Path]) -> Dict:
        """Group files by directory"""
        by_dir = {}
        for md_file in md_files:
            rel_dir = md_file.parent.relative_to(self.base_path)
            dir_key = str(rel_dir) if str(rel_dir) != '.' else 'root'
            by_dir[dir_key] = by_dir.get(dir_key, 0) + 1
        return dict(sorted(by_dir.items(), key=lambda x: x[1], reverse=True))
    
    def get_largest_files(self, md_files: List[Path]) -> List[Dict]:
        """Get largest files by size"""
        file_sizes = []
        for md_file in md_files:
            size_kb = round(md_file.stat().st_size / 1024, 1)
            file_sizes.append({
                'file': str(md_file.relative_to(self.base_path)),
                'size_kb': size_kb
            })
        return sorted(file_sizes, key=lambda x: x['size_kb'], reverse=True)[:10]
    
    def get_link_health(self) -> Dict:
        """Get comprehensive link health metrics with visible progression"""
        print("  🔗 Checking link health...")
        print("    ⏳ Running internal link checker...")
        internal_health = self.run_internal_link_check()
        if 'error' not in internal_health:
            print(f"      ✔️  Internal: {internal_health.get('total_links', 0)} links checked, {internal_health.get('broken_links', 0)} broken.")
        else:
            print("      ⚠️  Internal link check failed.")

        print("    ⏳ Running external link checker...")
        external_health = self.run_external_link_check()
        if 'error' not in external_health:
            print(f"      ✔️  External: {external_health.get('total_links', 0)} links checked, {external_health.get('errors', 0)} errors.")
        else:
            print("      ⚠️  External link check failed.")

        return {
            'internal': internal_health,
            'external': external_health,
            'overall_score': self.calculate_link_score(internal_health, external_health)
        }
    
    def run_internal_link_check(self) -> Dict:
        """Run internal link checker and parse results"""
        try:
            cmd = [
                'python', str(self.toolbox_path / 'check_internal_links.py'),
                str(self.base_path), '--format', 'json'
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            
            if result.stdout:
                data = json.loads(result.stdout)
                return {
                    'total_files': data.get('summary', {}).get('total_stats', {}).get('files_checked', 0),
                    'total_links': data.get('summary', {}).get('total_stats', {}).get('total_links', 0),
                    'broken_links': data.get('summary', {}).get('total_stats', {}).get('broken_links', 0),
                    'success_rate': self.calculate_success_rate(
                        data.get('summary', {}).get('total_stats', {}).get('total_links', 0),
                        data.get('summary', {}).get('total_stats', {}).get('broken_links', 0)
                    ),
                    'issues_by_type': self.categorize_internal_issues(data.get('results', []))
                }
        except Exception as e:
            print(f"    ⚠️ Could not run internal link check: {e}")
        
        return {'error': 'Could not check internal links'}
    
    def run_external_link_check(self) -> Dict:
        """Run external link checker and parse results, showing progression"""
        try:
            print("      ...external link checker started...")
            cmd = [
                'python', str(self.toolbox_path / 'check_external_links.py'),
                str(self.base_path), '--format', 'json', '--timeout', '5'
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            print("      ...external link checker finished.")
            if result.stdout:
                data = json.loads(result.stdout)
                print(f"        ↪️  External link data parsed: {data.get('total_links_found', 0)} links found.")
                return {
                    'total_links': data.get('total_links_found', 0),
                    'unique_urls': data.get('unique_urls_checked', 0),
                    'total_issues': data.get('total_issues', 0),
                    'errors': data.get('summary', {}).get('errors', 0),
                    'warnings': data.get('summary', {}).get('warnings', 0),
                    'success_rate': self.calculate_external_success_rate(data),
                    'avg_response_time': data.get('performance_stats', {}).get('average_response_time', 0)
                }
        except Exception as e:
            print(f"    ⚠️ Could not run external link check: {e}")
        
        return {'error': 'Could not check external links'}
    
    def categorize_internal_issues(self, results: List[Dict]) -> Dict:
        """Categorize internal link issues"""
        issues_by_type = {}
        for result in results:
            for issue in result.get('issues', []):
                issue_type = issue.get('issue_type', 'unknown')
                issues_by_type[issue_type] = issues_by_type.get(issue_type, 0) + 1
        return issues_by_type
    
    def calculate_success_rate(self, total: int, broken: int) -> float:
        """Calculate success rate percentage"""
        if total == 0:
            return 100.0
        return round(((total - broken) / total) * 100, 1)
    
    def calculate_external_success_rate(self, data: Dict) -> float:
        """Calculate external link success rate"""
        total = data.get('total_links_found', 0)
        errors = data.get('summary', {}).get('errors', 0)
        if total == 0:
            return 100.0
        return round(((total - errors) / total) * 100, 1)
    
    def calculate_link_score(self, internal: Dict, external: Dict) -> float:
        """Calculate overall link health score"""
        if 'error' in internal or 'error' in external:
            return 0.0
        
        internal_score = internal.get('success_rate', 0) * 0.6  # 60% weight
        external_score = external.get('success_rate', 0) * 0.4  # 40% weight
        
        return round(internal_score + external_score, 1)
    
    def get_content_metrics(self) -> Dict:
        """Analyze content quality metrics"""
        print("  📝 Analyzing content quality...")
        
        md_files = [f for f in self.base_path.rglob('*.md') 
                   if not f.is_relative_to(self.toolbox_path)]
        
        metrics = {
            'readme_files': 0,
            'files_with_toc': 0,
            'files_with_images': 0,
            'total_headings': 0,
            'total_code_blocks': 0,
            'average_file_length': 0,
            'content_types': {}
        }
        
        total_lines = 0
        
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                lines = content.split('\n')
                total_lines += len(lines)
                
                # Count READMEs
                if md_file.name.lower() == 'readme.md':
                    metrics['readme_files'] += 1
                
                # Check for Table of Contents
                if any('table of contents' in line.lower() or 'toc' in line.lower() 
                      for line in lines[:20]):  # Check first 20 lines
                    metrics['files_with_toc'] += 1
                
                # Check for images
                if '![' in content or '<img' in content:
                    metrics['files_with_images'] += 1
                
                # Count headings
                metrics['total_headings'] += len([line for line in lines if line.startswith('#')])
                
                # Count code blocks
                metrics['total_code_blocks'] += content.count('```')
                
                # Categorize by directory
                dir_name = md_file.parent.name
                metrics['content_types'][dir_name] = metrics['content_types'].get(dir_name, 0) + 1
                
            except Exception as e:
                print(f"    ⚠️ Could not analyze {md_file}: {e}")
        
        if len(md_files) > 0:
            metrics['average_file_length'] = round(total_lines / len(md_files), 1)
        
        return metrics
    
    def calculate_quality_scores(self, health_data: Dict) -> Dict:
        """Calculate quality scores for different aspects"""
        scores = {}
        
        # Link Health Score (0-100)
        link_health = health_data.get('link_health', {})
        scores['link_health'] = link_health.get('overall_score', 0)
        
        # Content Organization Score (0-100)
        file_metrics = health_data.get('file_metrics', {})
        content_metrics = health_data.get('content_metrics', {})
        
        organization_score = 0
        if file_metrics.get('total_markdown_files', 0) > 0:
            # README coverage
            readme_coverage = (content_metrics.get('readme_files', 0) / 
                             max(file_metrics.get('total_directories', 1), 1)) * 100
            readme_coverage = min(readme_coverage, 100)
            
            # TOC coverage
            toc_coverage = (content_metrics.get('files_with_toc', 0) / 
                           file_metrics.get('total_markdown_files', 1)) * 100
            
            # Image usage
            image_usage = (content_metrics.get('files_with_images', 0) / 
                          file_metrics.get('total_markdown_files', 1)) * 100
            
            organization_score = round((readme_coverage * 0.4 + toc_coverage * 0.3 + image_usage * 0.3), 1)
        
        scores['content_organization'] = min(organization_score, 100)
        
        # Overall Health Score
        scores['overall'] = round((scores['link_health'] * 0.6 + scores['content_organization'] * 0.4), 1)
        
        return scores
    
    def generate_recommendations(self, health_data: Dict) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Link health recommendations
        link_health = health_data.get('link_health', {})
        if link_health.get('overall_score', 0) < 90:
            recommendations.append("🔗 Fix broken internal and external links to improve link health score")
        
        internal = link_health.get('internal', {})
        if internal.get('broken_links', 0) > 0:
            recommendations.append(f"🔧 Fix {internal.get('broken_links', 0)} broken internal links")
        
        external = link_health.get('external', {})
        if external.get('errors', 0) > 0:
            recommendations.append(f"🌐 Address {external.get('errors', 0)} external link errors")
        
        # Content recommendations
        content_metrics = health_data.get('content_metrics', {})
        file_metrics = health_data.get('file_metrics', {})
        
        if content_metrics.get('readme_files', 0) < file_metrics.get('total_directories', 0):
            missing_readmes = file_metrics.get('total_directories', 0) - content_metrics.get('readme_files', 0)
            recommendations.append(f"📄 Add README.md files to {missing_readmes} directories")
        
        if content_metrics.get('files_with_toc', 0) < file_metrics.get('total_markdown_files', 0) * 0.5:
            recommendations.append("📋 Add table of contents to more files for better navigation")
        
        if content_metrics.get('files_with_images', 0) < file_metrics.get('total_markdown_files', 0) * 0.3:
            recommendations.append("🖼️ Consider adding more images to improve content engagement")
        
        # Performance recommendations
        largest_files = file_metrics.get('largest_files', [])
        if largest_files and largest_files[0].get('size_kb', 0) > 100:
            recommendations.append(f"📊 Consider splitting large files (largest: {largest_files[0]['file']})")
        
        return recommendations[:8]  # Limit to top 8 recommendations
    
    def generate_html_report(self) -> str:
        """Generate interactive HTML dashboard"""
        html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Palace Health Dashboard</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
               line-height: 1.6; color: #333; background: #f5f7fa; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                  color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { opacity: 0.9; font-size: 1.1em; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                gap: 20px; margin-bottom: 30px; }
        .card { background: white; padding: 25px; border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .card h3 { color: #2c3e50; margin-bottom: 15px; font-size: 1.3em; }
        .score { font-size: 3em; font-weight: bold; text-align: center; margin: 20px 0; }
        .score.excellent { color: #27ae60; }
        .score.good { color: #f39c12; }
        .score.poor { color: #e74c3c; }
        .metric { display: flex; justify-content: space-between; margin: 10px 0; 
                  padding: 8px 0; border-bottom: 1px solid #eee; }
        .metric:last-child { border-bottom: none; }
        .recommendations { background: #fff3cd; border: 1px solid #ffeaa7; 
                          border-radius: 5px; padding: 15px; margin: 15px 0; }
        .recommendation { margin: 8px 0; padding: 5px 0; }
        .status-excellent { color: #27ae60; font-weight: bold; }
        .status-good { color: #f39c12; font-weight: bold; }
        .status-poor { color: #e74c3c; font-weight: bold; }
        .timestamp { text-align: center; color: #7f8c8d; margin-top: 30px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Digital Palace Health Dashboard</h1>
            <p>Comprehensive health analysis for {repository_name}</p>
        </div>
        
        <div class="grid">
            <div class="card">
                <h3>🎯 Overall Health Score</h3>
                <div class="score {overall_class}">{overall_score}%</div>
                <div class="metric">
                    <span>Link Health:</span>
                    <span class="{link_health_class}">{link_health_score}%</span>
                </div>
                <div class="metric">
                    <span>Content Organization:</span>
                    <span class="{content_org_class}">{content_org_score}%</span>
                </div>
            </div>
            
            <div class="card">
                <h3>📁 Repository Overview</h3>
                <div class="metric">
                    <span>Total Markdown Files:</span>
                    <span><strong>{total_files}</strong></span>
                </div>
                <div class="metric">
                    <span>Total Directories:</span>
                    <span><strong>{total_directories}</strong></span>
                </div>
                <div class="metric">
                    <span>Repository Size:</span>
                    <span><strong>{total_size_mb} MB</strong></span>
                </div>
                <div class="metric">
                    <span>README Files:</span>
                    <span><strong>{readme_files}</strong></span>
                </div>
            </div>
            
            <div class="card">
                <h3>🔗 Link Health</h3>
                <div class="metric">
                    <span>Internal Links:</span>
                    <span>{internal_total} ({internal_broken} broken)</span>
                </div>
                <div class="metric">
                    <span>External Links:</span>
                    <span>{external_total} ({external_errors} errors)</span>
                </div>
                <div class="metric">
                    <span>Success Rate:</span>
                    <span class="{link_success_class}">{link_success_rate}%</span>
                </div>
                <div class="metric">
                    <span>Avg Response Time:</span>
                    <span>{avg_response_time}s</span>
                </div>
            </div>
            
            <div class="card">
                <h3>📝 Content Metrics</h3>
                <div class="metric">
                    <span>Files with TOC:</span>
                    <span><strong>{files_with_toc}</strong></span>
                </div>
                <div class="metric">
                    <span>Files with Images:</span>
                    <span><strong>{files_with_images}</strong></span>
                </div>
                <div class="metric">
                    <span>Total Headings:</span>
                    <span><strong>{total_headings}</strong></span>
                </div>
                <div class="metric">
                    <span>Avg File Length:</span>
                    <span><strong>{avg_file_length} lines</strong></span>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h3>💡 Recommendations</h3>
            <div class="recommendations">
                {recommendations_html}
            </div>
        </div>
        
        <div class="timestamp">
            Generated on {timestamp}
        </div>
    </div>
</body>
</html>'''
        
        # Prepare data for template
        def get_score_class(score):
            if score >= 90:
                return 'excellent'
            elif score >= 70:
                return 'good'
            else:
                return 'poor'
        
        health = self.health_data
        quality = health.get('quality_scores', {})
        file_metrics = health.get('file_metrics', {})
        content_metrics = health.get('content_metrics', {})
        link_health = health.get('link_health', {})
        
        overall_score = quality.get('overall', 0)
        link_health_score = quality.get('link_health', 0)
        content_org_score = quality.get('content_organization', 0)
        
        recommendations_html = ''.join([
            f'<div class="recommendation">{rec}</div>' 
            for rec in health.get('recommendations', [])
        ])
        
        return html_template.format(
            repository_name=health['repository']['name'],
            overall_score=overall_score,
            overall_class=get_score_class(overall_score),
            link_health_score=link_health_score,
            link_health_class=get_score_class(link_health_score),
            content_org_score=content_org_score,
            content_org_class=get_score_class(content_org_score),
            total_files=file_metrics.get('total_markdown_files', 0),
            total_directories=file_metrics.get('total_directories', 0),
            total_size_mb=file_metrics.get('total_size_mb', 0),
            readme_files=content_metrics.get('readme_files', 0),
            internal_total=link_health.get('internal', {}).get('total_links', 0),
            internal_broken=link_health.get('internal', {}).get('broken_links', 0),
            external_total=link_health.get('external', {}).get('total_links', 0),
            external_errors=link_health.get('external', {}).get('errors', 0),
            link_success_rate=link_health.get('overall_score', 0),
            link_success_class=get_score_class(link_health.get('overall_score', 0)),
            avg_response_time=link_health.get('external', {}).get('avg_response_time', 0),
            files_with_toc=content_metrics.get('files_with_toc', 0),
            files_with_images=content_metrics.get('files_with_images', 0),
            total_headings=content_metrics.get('total_headings', 0),
            avg_file_length=content_metrics.get('average_file_length', 0),
            recommendations_html=recommendations_html,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    
    def generate_text_report(self) -> str:
        """Generate text-based dashboard report"""
        lines = []
        lines.append("📊 DIGITAL PALACE HEALTH DASHBOARD")
        lines.append("=" * 50)
        lines.append("")
        
        # Overall scores
        quality = self.health_data.get('quality_scores', {})
        lines.append(f"🎯 Overall Health Score: {quality.get('overall', 0)}%")
        lines.append(f"🔗 Link Health: {quality.get('link_health', 0)}%")
        lines.append(f"📝 Content Organization: {quality.get('content_organization', 0)}%")
        lines.append("")
        
        # Repository metrics
        file_metrics = self.health_data.get('file_metrics', {})
        lines.append("📁 REPOSITORY OVERVIEW")
        lines.append(f"Total Markdown Files: {file_metrics.get('total_markdown_files', 0)}")
        lines.append(f"Total Directories: {file_metrics.get('total_directories', 0)}")
        lines.append(f"Repository Size: {file_metrics.get('total_size_mb', 0)} MB")
        lines.append("")
        
        # Link health
        link_health = self.health_data.get('link_health', {})
        internal = link_health.get('internal', {})
        external = link_health.get('external', {})
        
        lines.append("🔗 LINK HEALTH")
        lines.append(f"Internal Links: {internal.get('total_links', 0)} ({internal.get('broken_links', 0)} broken)")
        lines.append(f"External Links: {external.get('total_links', 0)} ({external.get('errors', 0)} errors)")
        lines.append(f"Overall Success Rate: {link_health.get('overall_score', 0)}%")
        lines.append("")
        
        # Content metrics
        content_metrics = self.health_data.get('content_metrics', {})
        lines.append("📝 CONTENT METRICS")
        lines.append(f"README Files: {content_metrics.get('readme_files', 0)}")
        lines.append(f"Files with TOC: {content_metrics.get('files_with_toc', 0)}")
        lines.append(f"Files with Images: {content_metrics.get('files_with_images', 0)}")
        lines.append(f"Total Headings: {content_metrics.get('total_headings', 0)}")
        lines.append("")
        
        # Recommendations
        recommendations = self.health_data.get('recommendations', [])
        if recommendations:
            lines.append("💡 RECOMMENDATIONS")
            for i, rec in enumerate(recommendations, 1):
                lines.append(f"{i}. {rec}")
            lines.append("")
        
        lines.append("Generated: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description='Generate Digital Palace health dashboard')
    parser.add_argument('--format', choices=['html', 'json', 'text'], default='text',
                        help='Output format (default: text)')
    parser.add_argument('--output', help='Output file (default: stdout)')
    parser.add_argument('--base-path', help='Base path for repository (default: current directory)')
    parser.add_argument('--open-browser', action='store_true', help='Open HTML report in browser')
    
    args = parser.parse_args()
    
    # Determine base path
    if args.base_path:
        base_path = args.base_path
    else:
        # Try to find repository root
        current = Path.cwd()
        while current != current.parent:
            if (current / '.digital_palace_toolbox').exists():
                base_path = current
                break
            current = current.parent
        else:
            base_path = Path.cwd()
    
    # Generate dashboard
    dashboard = HealthDashboard(base_path)
    health_data = dashboard.collect_health_metrics()
    
    # Generate output
    if args.format == 'html':
        output = dashboard.generate_html_report()
        default_filename = 'health_dashboard.html'
    elif args.format == 'json':
        output = json.dumps(health_data, indent=2)
        default_filename = 'health_dashboard.json'
    else:
        output = dashboard.generate_text_report()
        default_filename = 'health_dashboard.txt'
    
    # Write output
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(default_filename) if args.format != 'text' else None
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ Dashboard saved to: {output_path}")
        
        # Open in browser if requested
        if args.open_browser and args.format == 'html':
            webbrowser.open(f'file://{output_path.absolute()}')
    else:
        print(output)
    
    # Print summary
    quality = health_data.get('quality_scores', {})
    overall_score = quality.get('overall', 0)
    
    if overall_score >= 90:
        print(f"\n🎉 Excellent health score: {overall_score}%")
    elif overall_score >= 70:
        print(f"\n👍 Good health score: {overall_score}%")
    else:
        print(f"\n⚠️ Health score needs improvement: {overall_score}%")

if __name__ == '__main__':
    main()

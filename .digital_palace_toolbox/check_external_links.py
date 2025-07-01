#!/usr/bin/env python3
"""
Digital Palace External Link Checker

This script checks external links within markdown files in the Digital Palace repository.
It validates that:
- HTTP/HTTPS links are accessible
- Links return appropriate status codes
- Redirects are handled properly
- Response times are reasonable

Usage:
    python check_external_links.py [file_or_directory] [--format json|markdown|text]
    python check_external_links.py README.md
    python check_external_links.py guides/ --format json
    python check_external_links.py --all --format markdown --timeout 10

Author: Digital Palace Toolbox
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict
from urllib.parse import urlparse
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

@dataclass
class ExternalLinkIssue:
    """Represents an external link validation issue"""
    file_path: str
    line_number: int
    link_text: str
    link_url: str
    issue_type: str
    description: str
    severity: str  # 'error', 'warning', 'info'
    status_code: Optional[int] = None
    response_time: Optional[float] = None
    redirect_url: Optional[str] = None
    suggested_fix: Optional[str] = None

@dataclass
class ExternalLinkCheckResult:
    """Results of external link checking operation"""
    total_files_checked: int
    total_links_found: int
    unique_urls_checked: int
    total_issues: int
    issues: List[ExternalLinkIssue]
    summary: Dict[str, int]
    performance_stats: Dict[str, float]

class ExternalLinkChecker:
    def _suggest_link_duckduckgo(self, query: str) -> Optional[str]:
        """Suggest a correct link using DuckDuckGo HTML scraping (free, no API key required)"""
        import requests
        import re
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Digital Palace Link Checker) AppleWebKit/537.36',
            }
            resp = requests.get(f'https://duckduckgo.com/html/?q={requests.utils.quote(query)}', headers=headers, timeout=5)
            if resp.status_code == 200:
                # Find the first result URL in the HTML
                # DuckDuckGo result links look like: <a rel="nofollow" class="result__a" href="https://...">
                match = re.search(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"', resp.text)
                if match:
                    return match.group(1)
        except Exception:
            pass
        return None
    """Checks external links in markdown files"""
    
    def __init__(self, base_path: str, timeout: int = 10, max_retries: int = 3):
        self.base_path = Path(base_path).resolve()
        self.timeout = timeout
        self.max_retries = max_retries
        self.issues: List[ExternalLinkIssue] = []
        self.url_cache: Dict[str, Dict] = {}
        
        # Setup session with retries
        self.session = requests.Session()
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Common headers to avoid blocking
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Digital Palace Link Checker) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        
        # Regex patterns
        self.markdown_link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
        
    def check_files(self, paths: List[str], check_duplicates: bool = True) -> ExternalLinkCheckResult:
        """Check external links in specified files/directories, with ultra-fast async URL checking and console progression display"""
        import asyncio
        import httpx
        start_time = time.time()

        files_to_check = self._collect_markdown_files(paths)
        all_links = self._extract_all_links(files_to_check)

        # Get unique URLs to check
        unique_urls = set()
        for links_in_file in all_links.values():
            for _, _, url in links_in_file:
                if self._is_external_link(url):
                    unique_urls.add(self._normalize_url(url))

        unique_urls = sorted(unique_urls)
        total_unique = len(unique_urls)
        urls_to_check = [url for url in unique_urls if url not in self.url_cache]
        checked_count = 0
        bar_len = 30

        print(f"\n⚡ Checking {total_unique} unique external URLs asynchronously...\n")
        # For live status display
        ok_pages = []
        error_pages = []
        warning_pages = []

        # Generalized paywall detection: domain -> list of keywords
        paywall_heuristics = {
            'linkedin.com': ['paywall', 'sign in', 'join linkedin'],
            'medium.com': ['metered', 'become a member', 'get unlimited access'],
            'nytimes.com': ['subscribe', 'log in to continue', 'for subscribers'],
            'substack.com': ['this post is for paid subscribers', 'subscribe now'],
            # Add more domains and keywords as needed
        }

        def get_domain(url):
            try:
                return urlparse(url).netloc.lower()
            except Exception:
                return ''

        async def async_check_url(url, timeout):
            nonlocal checked_count
            try:
                async with httpx.AsyncClient(follow_redirects=True, timeout=timeout, http2=True, headers=self.session.headers) as client:
                    try:
                        response = await client.head(url)
                        if response.status_code in [405, 501]:
                            response = await client.get(url)
                        response_time = response.elapsed.total_seconds() if response.elapsed else None
                        redirect_url = str(response.url) if response.history else None
                        self.url_cache[url] = {
                            'status_code': response.status_code,
                            'response_time': response_time,
                            'redirect_url': redirect_url,
                            'headers': dict(response.headers),
                            'success': True
                        }
                        # Generalized paywall detection
                        content_snippet = (response.text[:1000] if hasattr(response, 'text') else "")
                        is_paywall = False
                        domain = get_domain(url)
                        for d, keywords in paywall_heuristics.items():
                            if d in domain:
                                for kw in keywords:
                                    if kw in content_snippet.lower():
                                        is_paywall = True
                                        break
                                if is_paywall:
                                    break
                        if is_paywall:
                            warning_pages.append((url, 'paywall', response_time))
                        elif response.status_code < 400:
                            ok_pages.append((url, response.status_code, response_time))
                        elif response.status_code >= 500:
                            error_pages.append((url, response.status_code, response_time))
                        else:
                            warning_pages.append((url, response.status_code, response_time))
                    except httpx.TimeoutException:
                        self.url_cache[url] = {
                            'status_code': None,
                            'response_time': timeout,
                            'error': f"Timeout after {timeout} seconds",
                            'success': False,
                            'error_type': 'timeout'
                        }
                        warning_pages.append((url, 'timeout', timeout))
                    except httpx.ConnectError as e:
                        self.url_cache[url] = {
                            'status_code': None,
                            'response_time': None,
                            'error': f"Connection Error: {str(e)}",
                            'success': False,
                            'error_type': 'connection_error'
                        }
                        error_pages.append((url, 'conn_error', None))
                    except httpx.RequestError as e:
                        self.url_cache[url] = {
                            'status_code': None,
                            'response_time': None,
                            'error': f"Request Error: {str(e)}",
                            'success': False,
                            'error_type': 'request_error'
                        }
                        error_pages.append((url, 'request_error', None))
            except Exception as e:
                self.url_cache[url] = {
                    'status_code': None,
                    'response_time': None,
                    'error': f"Unknown Error: {str(e)}",
                    'success': False,
                    'error_type': 'unknown_error'
                }
                error_pages.append((url, 'unknown', None))
            checked_count += 1
            filled_len = int(bar_len * checked_count // len(urls_to_check)) if urls_to_check else bar_len
            bar = '█' * filled_len + '-' * (bar_len - filled_len)
            sys.stdout.write(f"\r[{bar}] {checked_count}/{len(urls_to_check)}")
            sys.stdout.flush()

        async def run_async_checks():
            timeout = self.timeout
            tasks = [async_check_url(url, timeout) for url in urls_to_check]
            await asyncio.gather(*tasks)

        if urls_to_check:
            try:
                asyncio.run(run_async_checks())
            except RuntimeError:
                # If already in an event loop (e.g. Jupyter), fallback
                loop = asyncio.get_event_loop()
                loop.run_until_complete(run_async_checks())
            sys.stdout.write("\n")
            sys.stdout.flush()

        # Display categorized results
        print("\n--- OK PAGES ---")
        for url, code, t in ok_pages:
            print(f"✅ {url} [{code}] ({t:.2f}s)" if t is not None else f"✅ {url} [{code}]")
        if not ok_pages:
            print("(none)")
        print("\n--- WARNING PAGES ---")
        for url, code, t in warning_pages:
            print(f"⚠️  {url} [{code}] ({t:.2f}s)" if t is not None else f"⚠️  {url} [{code}]")
        if not warning_pages:
            print("(none)")
        print("\n--- ERROR PAGES ---")
        for url, code, t in error_pages:
            print(f"❌ {url} [{code}]" if t is None else f"❌ {url} [{code}] ({t:.2f}s)")
        if not error_pages:
            print("(none)")

        total_requests = len(urls_to_check)

        # Validate all links against cache
        total_links = 0
        print("\n🔍 Validating links in files...\n")
        for file_idx, (file_path, links_in_file) in enumerate(all_links.items(), 1):
            for line_num, link_text, url in links_in_file:
                if self._is_external_link(url):
                    total_links += 1
                    normalized_url = self._normalize_url(url)
                    self._validate_link_from_cache(
                        file_path, line_num, link_text, url, normalized_url
                    )
            # Show file progress
            sys.stdout.write(f"\rFiles checked: {file_idx}/{len(all_links)}")
            sys.stdout.flush()
        if all_links:
            sys.stdout.write("\n")
            sys.stdout.flush()

        # Generate summary and performance stats
        end_time = time.time()
        summary = self._generate_summary()
        performance_stats = {
            'total_time_seconds': round(end_time - start_time, 2),
            'unique_requests_made': total_requests,
            'cache_hits': len(unique_urls) - total_requests,
            'average_response_time': self._calculate_average_response_time(),
        }

        return ExternalLinkCheckResult(
            total_files_checked=len(files_to_check),
            total_links_found=total_links,
            unique_urls_checked=len(unique_urls),
            total_issues=len(self.issues),
            issues=self.issues,
            summary=summary,
            performance_stats=performance_stats
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
    
    def _extract_all_links(self, files: List[Path]) -> Dict[Path, List]:
        """Extract all links from files"""
        all_links = {}
        
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                links = []
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    matches = self.markdown_link_pattern.findall(line)
                    for link_text, link_url in matches:
                        links.append((line_num, link_text, link_url))
                
                all_links[file_path] = links
                
            except IOError as e:
                self.issues.append(ExternalLinkIssue(
                    file_path=str(file_path.relative_to(self.base_path)),
                    line_number=1,
                    link_text="",
                    link_url="",
                    issue_type="file_read_error",
                    description=f"Could not read file: {e}",
                    severity="error"
                ))
                all_links[file_path] = []
        
        return all_links
    
    def _check_url(self, url: str):
        """Check a single URL and cache the result"""
        start_time = time.time()
        
        try:
            response = self.session.head(
                url, 
                timeout=self.timeout,
                allow_redirects=True
            )
            
            # If HEAD doesn't work, try GET
            if response.status_code in [405, 501]:  # Method not allowed
                response = self.session.get(
                    url, 
                    timeout=self.timeout,
                    allow_redirects=True,
                    stream=True  # Don't download the full content
                )
                # Close the connection immediately
                response.close()
            
            response_time = time.time() - start_time
            
            # Determine if this is a redirect
            redirect_url = None
            if response.history:
                redirect_url = response.url
            
            self.url_cache[url] = {
                'status_code': response.status_code,
                'response_time': response_time,
                'redirect_url': redirect_url,
                'headers': dict(response.headers),
                'success': True
            }
            
        except requests.exceptions.SSLError as e:
            self.url_cache[url] = {
                'status_code': None,
                'response_time': time.time() - start_time,
                'error': f"SSL Error: {str(e)}",
                'success': False,
                'error_type': 'ssl_error'
            }
            
        except requests.exceptions.Timeout:
            self.url_cache[url] = {
                'status_code': None,
                'response_time': self.timeout,
                'error': f"Timeout after {self.timeout} seconds",
                'success': False,
                'error_type': 'timeout'
            }
            
        except requests.exceptions.ConnectionError as e:
            self.url_cache[url] = {
                'status_code': None,
                'response_time': time.time() - start_time,
                'error': f"Connection Error: {str(e)}",
                'success': False,
                'error_type': 'connection_error'
            }
            
        except requests.exceptions.RequestException as e:
            self.url_cache[url] = {
                'status_code': None,
                'response_time': time.time() - start_time,
                'error': f"Request Error: {str(e)}",
                'success': False,
                'error_type': 'request_error'
            }
    
    def _validate_link_from_cache(self, file_path: Path, line_num: int, 
                                 link_text: str, original_url: str, normalized_url: str):
        """Validate a link using cached results"""
        cache_entry = self.url_cache.get(normalized_url, {})

        # Helper to always try to suggest a correct link for any issue
        def get_suggestion():
            search_query = link_text if link_text.strip() else urlparse(original_url).netloc
            suggestion = self._suggest_link_duckduckgo(search_query)
            if suggestion:
                # Return both the suggestion and a flag indicating web search was performed
                return f"Try this link: {suggestion}", True
            return None, False

        if not cache_entry.get('success', False):
            error_type = cache_entry.get('error_type', 'unknown_error')
            error_msg = cache_entry.get('error', 'Unknown error')
            severity = 'error'
            suggested_fix = None
            web_search_performed = False
            # Always try to suggest a correct link for any error
            suggested_fix, web_search_performed = get_suggestion()
            if error_type == 'timeout':
                severity = 'warning'
                if not suggested_fix:
                    suggested_fix = f"Consider increasing timeout or checking if {urlparse(normalized_url).netloc} is slow"
            elif error_type == 'ssl_error':
                if not suggested_fix:
                    suggested_fix = "Check if the SSL certificate is valid"
            elif error_type == 'connection_error' and not suggested_fix:
                suggested_fix = "Check if the domain exists and is accessible"
            if suggested_fix and web_search_performed:
                suggested_fix += " _(web search performed)_"
            self.issues.append(ExternalLinkIssue(
                file_path=str(file_path.relative_to(self.base_path)),
                line_number=line_num,
                link_text=link_text,
                link_url=original_url,
                issue_type=error_type,
                description=error_msg,
                severity=severity,
                response_time=cache_entry.get('response_time'),
                suggested_fix=suggested_fix
            ))
            return

        status_code = cache_entry.get('status_code')
        response_time = cache_entry.get('response_time', 0)
        redirect_url = cache_entry.get('redirect_url')

        # Check for problematic status codes
        if status_code >= 400:
            severity = 'error' if status_code >= 500 else 'warning'
            description = f"HTTP {status_code}"
            suggested_fix = None
            web_search_performed = False
            # Always try to suggest a correct link for any HTTP error
            # For warnings (status 400-499), always conduct a web search for a potential link
            if 400 <= status_code < 500:
                suggested_fix, web_search_performed = get_suggestion()
                if not suggested_fix:
                    suggested_fix = "Check if the URL is correct or if the page has moved"
            else:
                suggested_fix, web_search_performed = get_suggestion()
            if status_code == 404:
                description = "Page not found (404)"
            elif status_code == 403:
                description = "Access forbidden (403)"
                if not suggested_fix:
                    suggested_fix = "The resource may require authentication or be restricted"
            elif status_code >= 500:
                description = f"Server error ({status_code})"
                if not suggested_fix:
                    suggested_fix = "The server is experiencing issues, try again later"
            if suggested_fix and web_search_performed:
                suggested_fix += " _(web search performed)_"
            self.issues.append(ExternalLinkIssue(
                file_path=str(file_path.relative_to(self.base_path)),
                line_number=line_num,
                link_text=link_text,
                link_url=original_url,
                issue_type="http_error",
                description=description,
                severity=severity,
                status_code=status_code,
                response_time=response_time,
                redirect_url=redirect_url,
                suggested_fix=suggested_fix
            ))
        # Check for slow responses
        elif response_time > 5.0:
            self.issues.append(ExternalLinkIssue(
                file_path=str(file_path.relative_to(self.base_path)),
                line_number=line_num,
                link_text=link_text,
                link_url=original_url,
                issue_type="slow_response",
                description=f"Slow response: {response_time:.2f}s",
                severity="info",
                status_code=status_code,
                response_time=response_time,
                redirect_url=redirect_url,
                suggested_fix="Consider if this link should be kept or replaced with a faster alternative"
            ))
        # Check for redirects that might need updating (only if meaningfully different)
        elif redirect_url and redirect_url != normalized_url:
            # Ignore trivial redirects (trailing slash, http<->https, or case-insensitive match)
            def normalize_for_compare(url):
                p = urlparse(url)
                # Lowercase scheme and netloc, remove trailing slash
                return f"{p.scheme.lower()}://{p.netloc.lower()}{p.path.rstrip('/')}"
            orig_norm = normalize_for_compare(normalized_url)
            redir_norm = normalize_for_compare(redirect_url)
            if orig_norm != redir_norm:
                self.issues.append(ExternalLinkIssue(
                    file_path=str(file_path.relative_to(self.base_path)),
                    line_number=line_num,
                    link_text=link_text,
                    link_url=original_url,
                    issue_type="redirect",
                    description=f"Redirects to: {redirect_url}",
                    severity="info",
                    status_code=status_code,
                    response_time=response_time,
                    redirect_url=redirect_url,
                    suggested_fix=f"Consider updating link to: {redirect_url}"
                ))
    
    def _is_external_link(self, url: str) -> bool:
        """Check if URL is external (HTTP/HTTPS)"""
        return url.startswith(('http://', 'https://'))
    
    def _normalize_url(self, url: str) -> str:
        """Normalize URL for comparison"""
        # Remove trailing slashes and fragments for comparison
        parsed = urlparse(url)
        normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if parsed.query:
            normalized += f"?{parsed.query}"
        return normalized.rstrip('/')
    
    def _calculate_average_response_time(self) -> float:
        """Calculate average response time from cache"""
        response_times = []
        for cache_entry in self.url_cache.values():
            if cache_entry.get('response_time') is not None:
                response_times.append(cache_entry['response_time'])
        
        return round(sum(response_times) / len(response_times), 3) if response_times else 0.0
    
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
        
        # Status code distribution
        status_codes = {}
        for issue in self.issues:
            if issue.status_code:
                status_codes[str(issue.status_code)] = status_codes.get(str(issue.status_code), 0) + 1
        summary['status_codes'] = status_codes
        
        return summary

class ExternalReportFormatter:
    """Format external link check results in different formats"""
    
    @staticmethod
    def format_json(result: ExternalLinkCheckResult) -> str:
        """Format results as JSON"""
        return json.dumps(asdict(result), indent=2, ensure_ascii=False)
    
    @staticmethod
    def format_markdown(result: ExternalLinkCheckResult) -> str:
        """Format results as Markdown, including file name, path, and all line numbers for each link."""
        md = []
        md.append("# 🌐 External Link Check Report")
        md.append("")
        md.append(f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md.append("")

        # Summary
        md.append("## 📊 Summary")
        md.append("")
        md.append(f"- **Files checked:** {result.total_files_checked}")
        md.append(f"- **External links found:** {result.total_links_found}")
        md.append(f"- **Unique URLs checked:** {result.unique_urls_checked}")
        md.append(f"- **Issues found:** {result.total_issues}")
        md.append(f"- **Errors:** {result.summary.get('errors', 0)}")
        md.append(f"- **Warnings:** {result.summary.get('warnings', 0)}")
        md.append(f"- **Info:** {result.summary.get('info', 0)}")
        md.append("")

        # Performance stats
        md.append("## ⚡ Performance")
        md.append("")
        md.append(f"- **Total check time:** {result.performance_stats['total_time_seconds']}s")
        md.append(f"- **Requests made:** {result.performance_stats['unique_requests_made']}")
        md.append(f"- **Cache hits:** {result.performance_stats['cache_hits']}")
        md.append(f"- **Average response time:** {result.performance_stats['average_response_time']}s")
        md.append("")

        if result.summary.get('by_type'):
            md.append("### Issues by Type")
            md.append("")
            for issue_type, count in result.summary['by_type'].items():
                md.append(f"- **{issue_type.replace('_', ' ').title()}:** {count}")
            md.append("")

        if result.summary.get('status_codes'):
            md.append("### HTTP Status Codes")
            md.append("")
            for status_code, count in result.summary['status_codes'].items():
                md.append(f"- **{status_code}:** {count}")
            md.append("")

        # Group issues by file and link for line number aggregation
        from collections import defaultdict
        file_link_lines = defaultdict(lambda: defaultdict(list))
        for issue in result.issues:
            file_link_lines[issue.file_path][issue.link_url].append(issue.line_number)

        # Issues detail
        if result.issues:
            md.append("## 🐛 Issues Found")
            md.append("")

            # Group by severity
            errors = [i for i in result.issues if i.severity == 'error']
            warnings = [i for i in result.issues if i.severity == 'warning']
            info = [i for i in result.issues if i.severity == 'info']

            def issue_header(issue):
                file_name = Path(issue.file_path).name
                file_path = issue.file_path
                # List all lines for this file+link
                lines = sorted(set(file_link_lines[file_path][issue.link_url]))
                lines_str = ', '.join(str(line) for line in lines)
                return f"**{file_name}**  ", f"Path: `{file_path}`  ", f"Lines: {lines_str}"

            if errors:
                md.append("### ❌ Errors")
                md.append("")
                for issue in errors:
                    file_name, file_path_str, lines_str = issue_header(issue)
                    md.append(f"{file_name}{file_path_str}{lines_str}")
                    md.append(f"- Link: `[{issue.link_text}]({issue.link_url})`")
                    md.append(f"- Issue: {issue.description}")
                    if issue.status_code:
                        md.append(f"- Status: {issue.status_code}")
                    if issue.response_time:
                        md.append(f"- Response time: {issue.response_time:.2f}s")
                    if issue.suggested_fix:
                        md.append(f"- 💡 Suggested fix: {issue.suggested_fix}")
                    md.append("")

            if warnings:
                md.append("### ⚠️ Warnings")
                md.append("")
                for issue in warnings:
                    file_name, file_path_str, lines_str = issue_header(issue)
                    md.append(f"{file_name}{file_path_str}{lines_str}")
                    md.append(f"- Link: `[{issue.link_text}]({issue.link_url})`")
                    md.append(f"- Issue: {issue.description}")
                    if issue.status_code:
                        md.append(f"- Status: {issue.status_code}")
                    if issue.response_time:
                        md.append(f"- Response time: {issue.response_time:.2f}s")
                    if issue.suggested_fix:
                        md.append(f"- 💡 Suggested fix: {issue.suggested_fix}")
                    md.append("")

            if info:
                md.append("### ℹ️ Information")
                md.append("")
                for issue in info:
                    file_name, file_path_str, lines_str = issue_header(issue)
                    md.append(f"{file_name}{file_path_str}{lines_str}")
                    md.append(f"- Link: `[{issue.link_text}]({issue.link_url})`")
                    md.append(f"- Info: {issue.description}")
                    if issue.redirect_url:
                        md.append(f"- Redirects to: {issue.redirect_url}")
                    if issue.response_time:
                        md.append(f"- Response time: {issue.response_time:.2f}s")
                    if issue.suggested_fix:
                        md.append(f"- 💡 Suggested fix: {issue.suggested_fix}")
                    md.append("")
        else:
            md.append("## ✅ No Issues Found")
            md.append("")
            md.append("All external links are working correctly!")

        md.append("---")
        md.append("*Report generated by Digital Palace External Link Checker*")

        return "\n".join(md)
    
    @staticmethod
    def format_text(result: ExternalLinkCheckResult) -> str:
        """Format results as plain text"""
        lines = []
        lines.append("EXTERNAL LINK CHECK REPORT")
        lines.append("=" * 30)
        lines.append("")
        
        lines.append(f"Files checked: {result.total_files_checked}")
        lines.append(f"External links found: {result.total_links_found}")
        lines.append(f"Unique URLs checked: {result.unique_urls_checked}")
        lines.append(f"Issues found: {result.total_issues}")
        lines.append(f"Errors: {result.summary.get('errors', 0)}")
        lines.append(f"Warnings: {result.summary.get('warnings', 0)}")
        lines.append(f"Info: {result.summary.get('info', 0)}")
        lines.append("")
        
        lines.append(f"Total time: {result.performance_stats['total_time_seconds']}s")
        lines.append(f"Average response time: {result.performance_stats['average_response_time']}s")
        lines.append("")
        
        if result.issues:
            lines.append("ISSUES:")
            lines.append("-" * 20)
            for i, issue in enumerate(result.issues, 1):
                lines.append(f"{i}. [{issue.severity.upper()}] {issue.file_path}:{issue.line_number}")
                lines.append(f"   Link: [{issue.link_text}]({issue.link_url})")
                lines.append(f"   Issue: {issue.description}")
                if issue.status_code:
                    lines.append(f"   Status: {issue.status_code}")
                if issue.response_time:
                    lines.append(f"   Response time: {issue.response_time:.2f}s")
                if issue.suggested_fix:
                    lines.append(f"   Fix: {issue.suggested_fix}")
                lines.append("")
        else:
            lines.append("✅ No issues found!")
        
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="Check external links in Digital Palace markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s README.md                    # Check single file
  %(prog)s guides/ tools/               # Check directories
  %(prog)s --all                        # Check entire repository
  %(prog)s README.md --format json      # Output as JSON
  %(prog)s guides/ --format markdown    # Output as Markdown report
  %(prog)s --all --timeout 15           # Use longer timeout
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
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='Timeout for HTTP requests in seconds (default: 10)'
    )
    
    parser.add_argument(
        '--max-retries',
        type=int,
        default=3,
        help='Maximum number of retries for failed requests (default: 3)'
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
    checker = ExternalLinkChecker(base_path, timeout=args.timeout, max_retries=args.max_retries)
    result = checker.check_files(paths)
    
    # Format output
    if args.format == 'json':
        output = ExternalReportFormatter.format_json(result)
    elif args.format == 'markdown':
        output = ExternalReportFormatter.format_markdown(result)
    else:
        output = ExternalReportFormatter.format_text(result)
    
    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Report written to: {args.output}")
    else:
        print(output)
    
    # Exit with error code if errors found
    if result.summary.get('errors', 0) > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()

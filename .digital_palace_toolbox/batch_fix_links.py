#!/usr/bin/env python3
"""
Digital Palace Batch Link Fixer

Automatically fixes common link issues in markdown files with backup and rollback capabilities.

Usage:
    python batch_fix_links.py [files] [--dry-run] [--no-backup] [--quiet]
    python batch_fix_links.py README.md --dry-run
    python batch_fix_links.py guides/ --backup --fix-all
    python batch_fix_links.py --rollback .backups/batch_fix_20250701_090000
    python batch_fix_links.py --test

Features:
- Fixes anchor formats, redirect URLs, missing file extensions, and case sensitivity
- Supports parallel processing with progress bar for large repositories
- Creates timestamped backups with cleanup of old backups
- Provides quiet mode and JSON summary output
- Includes unit tests and URL safety checks

Author: Digital Palace Toolbox
"""

import argparse
import json
import re
import shutil
import sys
import unittest
from datetime import datetime
from multiprocessing import Pool
from pathlib import Path
from typing import Dict, List, Tuple
import subprocess
from urllib.parse import urlparse

# NEW: Import tqdm for progress bar, with fallback
try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    tqdm = None

class BatchLinkFixer:
    def __init__(self, base_path: str, dry_run: bool = True, backup: bool = True, quiet: bool = False, max_backups: int = 10):
        """
        Initialize the BatchLinkFixer.

        Args:
            base_path: Repository root path
            dry_run: If True, show fixes without applying
            backup: If True, create backups
            quiet: If True, show only summary
            max_backups: Maximum number of backup directories to keep
        """
        self.base_path = Path(base_path).resolve()
        self.dry_run = dry_run
        self.backup = backup
        self.quiet = quiet
        self.max_backups = max_backups
        self.backup_dir = None

        if backup and not dry_run:
            self.create_backup_directory()
            self.cleanup_old_backups()

    def create_backup_directory(self):
        """Create a timestamped backup directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.backup_dir = self.base_path / f".backups/batch_fix_{timestamp}"
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        if not self.quiet:
            print(f"📦 Backup directory created: {self.backup_dir}")

    def cleanup_old_backups(self):
        """Remove old backups to keep only max_backups."""
        backup_root = self.base_path / '.backups'
        backups = sorted(backup_root.glob('batch_fix_*'), key=lambda x: x.stat().st_mtime)
        for old_backup in backups[:-self.max_backups]:
            shutil.rmtree(old_backup, ignore_errors=True)
            if not self.quiet:
                print(f"🗑️ Removed old backup: {old_backup}")

    def backup_file(self, file_path: Path):
        """Backup a file before modification."""
        if not self.backup or self.dry_run:
            return

        relative_path = file_path.relative_to(self.base_path)
        backup_path = self.backup_dir / relative_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, backup_path)

    def get_internal_link_issues(self, file_path: str) -> List[Dict]:
        """Get internal link issues from the checker."""
        try:
            cmd = [
                'python',
                str(self.base_path / '.digital_palace_toolbox/check_internal_links.py'),
                file_path,
                '--format', 'json'
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(result.stdout).get('issues', [])
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            if not self.quiet:
                print(f"⚠️ Error checking internal links in {file_path}: {e}")
            return []

    def get_external_link_issues(self, file_path: str) -> List[Dict]:
        """Get external link issues from the checker."""
        try:
            cmd = [
                'python',
                str(self.base_path / '.digital_palace_toolbox/check_external_links.py'),
                file_path,
                '--format', 'json',
                '--timeout', '10'
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(result.stdout).get('issues', [])
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            if not self.quiet:
                print(f"⚠️ Error checking external links in {file_path}: {e}")
            return []

    def is_safe_url(self, url: str) -> bool:
        """Check if a URL is safe (basic domain validation)."""
        unsafe_domains = {'example-malicious.com'}  # Add known unsafe domains
        try:
            domain = urlparse(url).netloc.lower()
            return domain and domain not in unsafe_domains
        except ValueError:
            return False

    def fix_anchor_format(self, content: str, issue: Dict) -> Tuple[str, bool]:
        """
        Fix anchor format by removing invalid characters.

        Args:
            content: Original file content
            issue: Issue dictionary with 'link_target' and 'suggested_fix'

        Returns:
            Tuple of (modified content, whether changes were made)
        """
        old_anchor = issue.get('link_target', '')
        suggested_fix = issue.get('suggested_fix', '')

        if not old_anchor or not suggested_fix:
            return content, False

        if '#' in old_anchor:
            path_part, _ = old_anchor.split('#', 1)
            new_link = f"{path_part}#{suggested_fix.lstrip('#')}"
        else:
            return content, False

        old_pattern = re.escape(old_anchor)
        new_content = re.sub(f'\\({old_pattern}\\)', f'({new_link})', content)
        return new_content, new_content != content

    def fix_redirect_url(self, content: str, issue: Dict) -> Tuple[str, bool]:
        """
        Fix redirect URLs to their final destination.

        Args:
            content: Original file content
            issue: Issue dictionary with 'link_url' and 'description'

        Returns:
            Tuple of (modified content, whether changes were made)
        """
        old_url = issue.get('link_url', '')
        description = issue.get('description', '')
        redirect_match = re.search(r'Redirects to: (https?://[^\s]+)', description)

        if not redirect_match:
            return content, False

        new_url = redirect_match.group(1)
        if not self.is_safe_url(new_url):
            if not self.quiet:
                print(f"⚠️ Skipping unsafe redirect URL: {new_url}")
            return content, False

        old_pattern = re.escape(old_url)
        new_content = re.sub(f'\\({old_pattern}\\)', f'({new_url})', content)
        return new_content, new_content != content

    def fix_missing_file_extension(self, content: str, issue: Dict) -> Tuple[str, bool]:
        """
        Fix missing .md file extensions.

        Args:
            content: Original file content
            issue: Issue dictionary with 'link_target'

        Returns:
            Tuple of (modified content, whether changes were made)
        """
        link_target = issue.get('link_target', '')
        if not link_target or link_target.startswith('http') or '#' in link_target:
            return content, False

        if not link_target.endswith('.md') and not link_target.endswith('/'):
            new_target = f"{link_target}.md"
            target_path = self.base_path / new_target
            if target_path.exists():
                old_pattern = re.escape(link_target)
                new_content = re.sub(f'\\({old_pattern}\\)', f'({new_target})', content)
                return new_content, new_content != content
        return content, False

    def fix_case_sensitivity(self, content: str, issue: Dict) -> Tuple[str, bool]:
        """
        Fix case sensitivity in file paths.

        Args:
            content: Original file content
            issue: Issue dictionary with 'link_target'

        Returns:
            Tuple of (modified content, whether changes were made)
        """
        link_target = issue.get('link_target', '')
        if not link_target or link_target.startswith('http'):
            return content, False

        path_parts = link_target.split('/')
        current_path = self.base_path
        corrected_parts = []

        for part in path_parts:
            if not part:
                continue
            found = False
            if current_path.exists():
                for item in current_path.iterdir():
                    if item.name.lower() == part.lower():
                        corrected_parts.append(item.name)
                        current_path = item
                        found = True
                        break
            if not found:
                return content, False

        if corrected_parts:
            corrected_path = '/'.join(corrected_parts)
            if corrected_path != link_target:
                old_pattern = re.escape(link_target)
                new_content = re.sub(f'\\({old_pattern}\\)', f'({corrected_path})', content)
                return new_content, new_content != content
        return content, False

    def apply_internal_fixes(self, content: str, issues: List[Dict], fix_types: List[str]) -> Tuple[str, List[str]]:
        """Apply internal link fixes."""
        fixes_applied = []
        for issue in issues:
            if issue.get('severity') != 'error':
                continue
            issue_type = issue.get('issue_type', '')
            fixed = False

            if issue_type == 'missing_anchor' and 'anchors' in fix_types:
                content, fixed = self.fix_anchor_format(content, issue)
                if fixed:
                    fixes_applied.append(f"Fixed anchor format: {issue.get('link_target', '')}")

            elif issue_type == 'missing_file' and 'files' in fix_types:
                content, fixed = self.fix_missing_file_extension(content, issue)
                if fixed:
                    fixes_applied.append(f"Added .md extension: {issue.get('link_target', '')}")
                if not fixed:
                    content, fixed = self.fix_case_sensitivity(content, issue)
                    if fixed:
                        fixes_applied.append(f"Fixed case sensitivity: {issue.get('link_target', '')}")

        return content, fixes_applied

    def apply_external_fixes(self, content: str, issues: List[Dict], fix_types: List[str]) -> Tuple[str, List[str]]:
        """Apply external link fixes."""
        fixes_applied = []
        for issue in issues:
            if issue.get('severity') != 'info' or 'redirects' not in fix_types:
                continue
            if 'Redirects to:' in issue.get('description', ''):
                content, fixed = self.fix_redirect_url(content, issue)
                if fixed:
                    fixes_applied.append(f"Updated redirect URL: {issue.get('link_url', '')}")
        return content, fixes_applied

    def apply_fixes_to_file(self, file_path: str, fix_types: List[str]) -> Dict:
        """
        Apply fixes to a single file.

        Args:
            file_path: Path to the file
            fix_types: Types of fixes to apply

        Returns:
            Dictionary with file status and fixes applied
        """
        file_path = Path(file_path)
        if not file_path.exists():
            return {'file': str(file_path), 'error': 'File not found', 'fixes_applied': 0}

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except FileNotFoundError:
            return {'file': str(file_path), 'error': 'File not found', 'fixes_applied': 0}
        except PermissionError:
            return {'file': str(file_path), 'error': 'Permission denied', 'fixes_applied': 0}
        except UnicodeDecodeError:
            return {'file': str(file_path), 'error': 'Invalid encoding', 'fixes_applied': 0}

        content = original_content
        fixes_applied = []

        internal_issues = self.get_internal_link_issues(str(file_path)) if 'internal' in fix_types else []
        content, internal_fixes = self.apply_internal_fixes(content, internal_issues, fix_types)
        fixes_applied.extend(internal_fixes)

        external_issues = self.get_external_link_issues(str(file_path)) if 'external' in fix_types else []
        content, external_fixes = self.apply_external_fixes(content, external_issues, fix_types)
        fixes_applied.extend(external_fixes)

        if content != original_content and not self.dry_run:
            self.backup_file(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

        return {
            'file': str(file_path.relative_to(self.base_path)),
            'fixes_applied': len(fixes_applied),
            'fixes_detail': fixes_applied,
            'content_changed': content != original_content
        }

    def batch_fix(self, file_paths: List[str], fix_types: List[str]) -> Dict:
        """
        Apply batch fixes to multiple files with progress display.

        Args:
            file_paths: List of file paths to process
            fix_types: Types of fixes to apply

        Returns:
            Dictionary with summary and results
        """
        if not self.quiet:
            print(f"🔧 {'DRY RUN: ' if self.dry_run else ''}Applying batch fixes...")
            print(f"📁 Fix types: {', '.join(fix_types)}")
            print(f"📄 Files to process: {len(file_paths)}")
            if not HAS_TQDM:
                print("⚠️ Install 'tqdm' for progress bar display")
            print()

        results = []
        total_fixes = 0

        def process_file(file_path):
            if not file_path.endswith('.md'):
                return None
            return self.apply_fixes_to_file(file_path, fix_types)

        # NEW: Use tqdm for progress bar in non-quiet mode
        if self.quiet or not HAS_TQDM:
            with Pool() as pool:
                results = [r for r in pool.map(process_file, file_paths) if r is not None]
        else:
            with Pool() as pool:
                results = [r for r in tqdm(pool.imap(process_file, file_paths), total=len(file_paths), desc="Processing files") if r is not None]

        for result in results:
            fixes_count = result.get('fixes_applied', 0)
            total_fixes += fixes_count

            if not self.quiet:
                if fixes_count > 0:
                    status = "🟡 WOULD FIX" if self.dry_run else "✅ FIXED"
                    print(f"{status} {result['file']}: {fixes_count} fixes")
                    for fix in result.get('fixes_detail', []):
                        print(f"    - {fix}")
                elif 'error' in result:
                    print(f"❌ ERROR {result['file']}: {result['error']}")
                else:
                    print(f"✅ OK {result['file']}: No fixes needed")

        summary = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'total_fixes': total_fixes,
            'files_processed': len(results),
            'backup_location': str(self.backup_dir) if self.backup_dir else None
        }

        if not self.quiet:
            print()
            print(f"📊 SUMMARY:")
            print(f"   Files processed: {summary['files_processed']}")
            print(f"   Total fixes: {summary['total_fixes']}")
            print(f"   Files changed: {len([r for r in results if r.get('content_changed', False)])}")
            if self.backup and not self.dry_run and total_fixes > 0:
                print(f"   Backup location: {summary['backup_location']}")

        return {'summary': summary, 'results': results}

    def rollback_changes(self, backup_location: str = None) -> bool:
        """
        Rollback changes from a backup.

        Args:
            backup_location: Specific backup directory or None to list available

        Returns:
            True if rollback succeeded, False otherwise
        """
        backup_root = self.base_path / '.backups'
        if not backup_location:
            backups = sorted(backup_root.glob('batch_fix_*'), key=lambda x: x.stat().st_mtime, reverse=True)
            if not backups:
                print("❌ No backups available")
                return False
            print("Available backups:")
            for i, backup in enumerate(backups, 1):
                print(f"{i}. {backup.name} ({datetime.fromtimestamp(backup.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')})")
            return False

        backup_path = Path(backup_location)
        if not backup_path.exists():
            print(f"❌ Backup directory not found: {backup_path}")
            return False

        print(f"🔄 Rolling back changes from: {backup_path}")
        files_restored = 0
        for backup_file in backup_path.rglob('*'):
            if backup_file.is_file():
                relative_path = backup_file.relative_to(backup_path)
                target_file = self.base_path / relative_path
                target_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(backup_file, target_file)
                files_restored += 1
                if not self.quiet:
                    print(f"   Restored: {relative_path}")

        print(f"✅ Rollback complete: {files_restored} files restored")
        return True

class TestBatchLinkFixer(unittest.TestCase):
    """Unit tests for BatchLinkFixer."""
    def setUp(self):
        self.fixer = BatchLinkFixer('.')

    def test_fix_anchor_format(self):
        content = '[link](#test😊)'
        issue = {'link_target': '#test😊', 'suggested_fix': '#test'}
        new_content, fixed = self.fixer.fix_anchor_format(content, issue)
        self.assertTrue(fixed)
        self.assertEqual(new_content, '[link](#test)')

    def test_fix_redirect_url(self):
        content = '[link](http://old.com)'
        issue = {'link_url': 'http://old.com', 'description': 'Redirects to: https://new.com'}
        new_content, fixed = self.fixer.fix_redirect_url(content, issue)
        self.assertTrue(fixed)
        self.assertEqual(new_content, '[link](https://new.com)')

    def test_is_safe_url(self):
        self.assertTrue(self.fixer.is_safe_url('https://example.com'))
        self.assertFalse(self.fixer.is_safe_url('https://example-malicious.com'))

def main():
    parser = argparse.ArgumentParser(description='Batch fix common link issues in markdown files')
    parser.add_argument('files', nargs='*', help='Files to fix (default: all .md files)')
    parser.add_argument('--dry-run', action='store_true', help='Show fixes without applying')
    parser.add_argument('--no-backup', action='store_true', help='Skip creating backups')
    parser.add_argument('--quiet', action='store_true', help='Show only summary')
    parser.add_argument('--fix-anchors', action='store_true', help='Fix anchor format issues (default)')
    parser.add_argument('--fix-redirects', action='store_true', help='Update redirect URLs')
    parser.add_argument('--fix-files', action='store_true', help='Fix file path issues')
    parser.add_argument('--fix-all', action='store_true', help='Apply all available fixes')
    parser.add_argument('--rollback', help='Rollback changes from backup directory')
    parser.add_argument('--base-path', help='Base path for the repository')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        unittest.main(argv=['first-arg-is-ignored'])
        sys.exit(0)

    if args.rollback:
        base_path = Path(args.base_path or Path.cwd())
        fixer = BatchLinkFixer(base_path, dry_run=False, backup=False, quiet=args.quiet)
        fixer.rollback_changes(args.rollback)
        return

    base_path = Path(args.base_path or Path.cwd())
    if not (base_path / '.digital_palace_toolbox').exists():
        if not args.quiet:
            print(f"⚠️ Warning: Could not detect repository root. Using {base_path}")

    file_paths = args.files or [str(f) for f in base_path.rglob('*.md') if not f.is_relative_to(base_path / '.digital_palace_toolbox')]

    fix_types = ['internal', 'anchors'] if not (args.fix_all or args.fix_anchors or args.fix_redirects or args.fix_files) else (
        ['internal', 'external', 'anchors', 'redirects', 'files'] if args.fix_all else
        ['internal'] + (['anchors'] if args.fix_anchors else []) +
        (['external', 'redirects'] if args.fix_redirects else []) +
        (['files'] if args.fix_files else [])
    )

    if 'external' in fix_types and not args.dry_run and not args.quiet:
        confirm = input("External link checks may take time. Proceed? (y/n): ")
        if confirm.lower() != 'y':
            fix_types = [t for t in fix_types if t not in ['external', 'redirects']]

    fixer = BatchLinkFixer(base_path, dry_run=args.dry_run, backup=not args.no_backup, quiet=args.quiet)
    result = fixer.batch_fix(file_paths, fix_types)

    if not args.dry_run and result['summary']['total_fixes'] > 0:
        with open(base_path / 'fix_summary.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        if not args.quiet:
            print(f"📝 Summary saved to {base_path / 'fix_summary.json'}")

    if not args.quiet:
        if args.dry_run:
            print("\n💡 Run without --dry-run to apply these fixes")
        elif result['summary']['total_fixes'] > 0:
            print(f"\n✅ Batch fix complete! Use --rollback {result['summary']['backup_location']} to undo changes if needed")

if __name__ == '__main__':
    main()
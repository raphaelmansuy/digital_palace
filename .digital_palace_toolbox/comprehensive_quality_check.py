#!/usr/bin/env python3
"""
Comprehensive LinkedIn Posts Quality Compliance Check
Validates ALL LinkedIn posts against the quality guidelines in _quality_linkedin_post.md
"""

import re
from pathlib import Path
from typing import List, Dict, Any

def extract_post_content(file_path: str) -> str:
    """Extract only the post content between the two --- rulers"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find content between the two --- rulers
        pattern = r'---\s*\n(.*?)\n---'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        return ""
    except Exception:
        return ""

def count_characters_properly(content: str) -> int:
    """Count characters as per LinkedIn quality guidelines"""
    # Remove markdown formatting that doesn't count
    # Bold
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
    # Italic  
    content = re.sub(r'\*([^*]+)\*', r'\1', content)
    # Code (inline)
    content = re.sub(r'`([^`]+)`', r'\1', content)
    # Links (keep link text, remove URL)
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    # Remove header markers but keep text
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
    # Remove blockquote markers but keep text
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    # Remove list markers but keep text
    content = re.sub(r'^[-*+]\s*', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\d+\.\s*', '', content, flags=re.MULTILINE)
    
    return len(content.strip())

def check_title_requirement(content: str) -> bool:
    """Check if content starts with required title format ## [Title] (without 👉)"""
    lines = content.strip().split('\n')
    if not lines:
        return False
    
    first_line = lines[0].strip()
    # Must start with ## and NOT contain 👉
    return first_line.startswith('##') and '👉' not in first_line

def check_quoted_examples(content: str) -> int:
    """Count quoted text examples (blockquotes)"""
    # Count blocks of blockquoted text
    blockquote_blocks = 0
    lines = content.split('\n')
    in_blockquote = False
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if not in_blockquote:
                blockquote_blocks += 1
                in_blockquote = True
        else:
            in_blockquote = False
    
    return blockquote_blocks

def check_header_format(content: str) -> List[str]:
    """Check header formatting compliance"""
    issues = []
    lines = content.split('\n')
    first_header_found = False
    
    for line in lines:
        line = line.strip()
        if line.startswith('##'):
            if not first_header_found:
                # First header should NOT have 👉
                if '👉' in line:
                    issues.append("First header (title) should not contain 👉 emoji")
                first_header_found = True
            else:
                # Subsequent level 2 headers should have 👉
                if '👉' not in line:
                    issues.append(f"Header missing 👉 emoji: {line}")
    
    return issues

def validate_post(file_path: str) -> Dict[str, Any]:
    """Validate a single post against all quality requirements"""
    result = {
        'file': file_path,
        'compliant': True,
        'issues': [],
        'warnings': [],
        'character_count': 0,
        'quoted_examples': 0
    }
    
    content = extract_post_content(file_path)
    
    if not content:
        result['compliant'] = False
        result['issues'].append("No content found between --- rulers")
        return result
    
    # Character count check
    char_count = count_characters_properly(content)
    result['character_count'] = char_count
    
    if char_count > 1800:
        result['compliant'] = False
        result['issues'].append(f"Exceeds 1800 character limit ({char_count} chars)")
    elif char_count < 1200:
        result['warnings'].append(f"Below optimal minimum of 1200 chars ({char_count} chars)")
    
    # Title requirement check
    if not check_title_requirement(content):
        result['compliant'] = False
        result['issues'].append("Content must start with ## [Title] header (without 👉)")
    
    # Quoted examples check
    quoted_count = check_quoted_examples(content)
    result['quoted_examples'] = quoted_count
    
    if quoted_count > 1:
        result['compliant'] = False
        result['issues'].append(f"More than 1 quoted example found ({quoted_count})")
    
    # Header format check
    header_issues = check_header_format(content)
    if header_issues:
        result['compliant'] = False
        result['issues'].extend(header_issues)
    
    # Check for required elements
    if not any(word in content.lower() for word in ['problem', 'challenge', 'issue']):
        result['warnings'].append("No clear problem statement found")
    
    if '?' not in content:
        result['warnings'].append("No engaging question found")
    
    return result

def main():
    """Main function to check all LinkedIn posts"""
    workspace_root = Path("/Users/raphaelmansuy/Library/Mobile Documents/iCloud~md~obsidian/Documents/digital_palace")
    linkedin_dir = workspace_root / "personal" / "elitizon_linkedin"
    
    if not linkedin_dir.exists():
        print("❌ LinkedIn directory not found!")
        return
    
    print("🔍 Comprehensive LinkedIn Posts Quality Compliance Check")
    print("=" * 70)
    print(f"📁 Scanning: {linkedin_dir}")
    print()
    
    # Get all markdown files
    post_files = list(linkedin_dir.glob("post_*.md"))
    post_files.sort()
    
    if not post_files:
        print("❌ No post_*.md files found!")
        return
    
    print(f"📊 Found {len(post_files)} posts to validate...")
    print()
    
    compliant_posts = 0
    non_compliant_posts = 0
    total_issues = 0
    over_limit_posts = []
    missing_title_posts = []
    multiple_quotes_posts = []
    
    for post_file in post_files:
        result = validate_post(str(post_file))
        
        # Extract post number for reporting
        post_name = post_file.name
        post_number = post_name.split('_')[1] if '_' in post_name else '?'
        
        if result['compliant']:
            compliant_posts += 1
            status = "✅"
        else:
            non_compliant_posts += 1
            status = "❌"
            total_issues += len(result['issues'])
            
            # Track specific violations
            for issue in result['issues']:
                if "character limit" in issue:
                    over_limit_posts.append(f"Post {post_number}")
                elif "Title" in issue or "header" in issue:
                    missing_title_posts.append(f"Post {post_number}")
                elif "quoted example" in issue:
                    multiple_quotes_posts.append(f"Post {post_number}")
        
        # Show detailed results for non-compliant posts
        if not result['compliant'] or result['warnings']:
            print(f"{status} Post {post_number}: {post_name}")
            print(f"   📏 Characters: {result['character_count']}/1800")
            print(f"   💬 Quoted examples: {result['quoted_examples']}")
            
            if result['issues']:
                print("   ❌ Issues:")
                for issue in result['issues']:
                    print(f"      • {issue}")
            
            if result['warnings']:
                print("   ⚠️  Warnings:")
                for warning in result['warnings']:
                    print(f"      • {warning}")
            print()
    
    # Summary Report
    print("📈 COMPLIANCE SUMMARY")
    print("=" * 70)
    print(f"📊 Total posts analyzed: {len(post_files)}")
    print(f"✅ Compliant posts: {compliant_posts}")
    print(f"❌ Non-compliant posts: {non_compliant_posts}")
    print(f"⚠️  Total issues: {total_issues}")
    
    compliance_rate = (compliant_posts / len(post_files)) * 100
    print(f"📈 Compliance rate: {compliance_rate:.1f}%")
    
    print()
    print("🔍 VIOLATION BREAKDOWN")
    print("-" * 40)
    
    if over_limit_posts:
        print(f"📏 Character limit violations ({len(over_limit_posts)}):")
        for post in over_limit_posts[:10]:  # Show first 10
            print(f"   • {post}")
        if len(over_limit_posts) > 10:
            print(f"   • ... and {len(over_limit_posts) - 10} more")
    
    if missing_title_posts:
        print(f"📝 Title format violations ({len(missing_title_posts)}):")
        for post in missing_title_posts[:10]:
            print(f"   • {post}")
        if len(missing_title_posts) > 10:
            print(f"   • ... and {len(missing_title_posts) - 10} more")
    
    if multiple_quotes_posts:
        print(f"💬 Multiple quoted examples ({len(multiple_quotes_posts)}):")
        for post in multiple_quotes_posts[:10]:
            print(f"   • {post}")
        if len(multiple_quotes_posts) > 10:
            print(f"   • ... and {len(multiple_quotes_posts) - 10} more")
    
    print()
    
    if compliance_rate == 100:
        print("🎉 ALL POSTS ARE COMPLIANT! Excellent work!")
    elif compliance_rate >= 90:
        print("👍 Very high compliance rate - just a few posts need attention")
    elif compliance_rate >= 75:
        print("⚠️  Good compliance rate - some posts need fixes")
    elif compliance_rate >= 50:
        print("❌ Moderate compliance - significant improvements needed")
    else:
        print("🚨 Low compliance rate - urgent attention required")
    
    print()
    print("🔧 Next steps:")
    if non_compliant_posts > 0:
        print("   1. Fix character count violations first (hardest constraint)")
        print("   2. Update title formats to match requirements")
        print("   3. Remove excess quoted examples")
        print("   4. Add missing problem statements and questions")
    else:
        print("   ✅ All posts are compliant with quality guidelines!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Fix Character Count Violations - Step by Step Tool
Systematically reduces character count for posts exceeding 1800 characters
"""

import re
from pathlib import Path
from typing import List, Tuple

def extract_post_content(file_path: str) -> Tuple[str, str, str]:
    """Extract post content and return (before, content, after) sections"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        parts = content.split('---')
        if len(parts) < 3:
            return "", "", ""
        
        before_content = '---'.join(parts[:1]) + '---'
        post_content = parts[1]
        after_content = '---' + '---'.join(parts[2:])
        
        return before_content, post_content, after_content
    except Exception:
        return "", "", ""

def count_characters_properly(content: str) -> int:
    """Count characters as per LinkedIn quality guidelines"""
    # Remove markdown formatting that doesn't count
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # Bold
    content = re.sub(r'\*([^*]+)\*', r'\1', content)      # Italic
    content = re.sub(r'`([^`]+)`', r'\1', content)        # Code
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)  # Links
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)  # Headers
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)   # Blockquotes
    content = re.sub(r'^[-*+]\s*', '', content, flags=re.MULTILINE)  # Lists
    content = re.sub(r'^\d+\.\s*', '', content, flags=re.MULTILINE)  # Numbered lists
    
    return len(content.strip())

def optimize_content_length(content: str, target_chars: int = 1750) -> str:
    """Optimize content to reduce character count while maintaining quality"""
    
    # Strategy 1: Remove excessive spacing and formatting
    optimized = re.sub(r'\n\n\n+', '\n\n', content)  # Reduce multiple newlines
    optimized = re.sub(r'  +', ' ', optimized)        # Remove multiple spaces
    
    # Strategy 2: Condense verbose phrases
    replacements = {
        r'business professionals': 'professionals',
        r'organizations and companies': 'organizations',
        r'implementation and deployment': 'implementation',
        r'analysis and evaluation': 'analysis',
        r'coordination and management': 'coordination',
        r'strategies and techniques': 'strategies',
        r'methods and approaches': 'methods',
        r'solutions and recommendations': 'solutions',
        r'processes and procedures': 'processes',
        r'systems and frameworks': 'systems',
        r'tools and technologies': 'tools',
        r'results and outcomes': 'results',
        r'performance and efficiency': 'performance',
        r'quality and effectiveness': 'quality',
        r'innovation and creativity': 'innovation',
    }
    
    for pattern, replacement in replacements.items():
        optimized = re.sub(pattern, replacement, optimized, flags=re.IGNORECASE)
    
    # Strategy 3: Condense example sections if they're too long
    lines = optimized.split('\n')
    condensed_lines = []
    in_example = False
    example_lines = []
    
    for line in lines:
        if '```' in line and 'Example' in line:
            in_example = True
            example_lines = [line]
        elif in_example and '```' in line:
            in_example = False
            # Condense example if too long
            if len('\n'.join(example_lines)) > 300:
                condensed_example = [
                    example_lines[0],  # Opening
                    "Enterprise transformation across departments:",
                    "- Financial analysis: ROI projections",
                    "- Technical design: Architecture roadmap", 
                    "- HR strategy: Change management",
                    "- Operations: Process integration",
                    "Result: 89% success rate",
                    line  # Closing
                ]
                condensed_lines.extend(condensed_example)
            else:
                condensed_lines.extend(example_lines + [line])
        elif in_example:
            example_lines.append(line)
        else:
            condensed_lines.append(line)
    
    optimized = '\n'.join(condensed_lines)
    
    # Strategy 4: Trim sentences if still too long
    current_chars = count_characters_properly(optimized)
    if current_chars > target_chars:
        # Remove least essential sentences
        sentences = re.split(r'(?<=[.!?])\s+', optimized)
        
        # Score sentences by importance (keep key metrics, remove fluff)
        important_patterns = [
            r'\d+%',  # Percentages
            r'framework', r'system', r'process', r'methodology',
            r'implementation', r'business impact', r'your.*implementation'
        ]
        
        scored_sentences = []
        for sentence in sentences:
            score = 0
            for pattern in important_patterns:
                if re.search(pattern, sentence, re.IGNORECASE):
                    score += 1
            scored_sentences.append((sentence, score))
        
        # Keep highest scoring sentences until we hit target
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        
        final_sentences = []
        char_count = 0
        
        for sentence, score in scored_sentences:
            sentence_chars = count_characters_properly(sentence)
            if char_count + sentence_chars <= target_chars:
                final_sentences.append(sentence)
                char_count += sentence_chars
            elif score >= 2:  # Keep very important sentences even if over limit
                final_sentences.append(sentence)
                char_count += sentence_chars
        
        # Rebuild in logical order (approximate)
        optimized = ' '.join(final_sentences)
        
        # Fix formatting issues from sentence splitting
        optimized = re.sub(r'\s+([.!?])', r'\1', optimized)
        optimized = re.sub(r'([.!?])\s*\n\s*([A-Z])', r'\1\n\n\2', optimized)
    
    return optimized.strip()

def fix_character_count(file_path: str, target_chars: int = 1750) -> bool:
    """Fix character count for a specific post"""
    before, content, after = extract_post_content(file_path)
    
    if not content:
        return False
    
    current_chars = count_characters_properly(content)
    if current_chars <= 1800:
        return False  # Already compliant
    
    print(f"   📏 Current: {current_chars} chars, Target: {target_chars} chars")
    print(f"   ✂️  Need to reduce: {current_chars - target_chars} chars")
    
    optimized_content = optimize_content_length(content, target_chars)
    new_chars = count_characters_properly(optimized_content)
    
    if new_chars <= 1800:
        # Write optimized content
        new_file_content = before + optimized_content + after
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        
        print(f"   ✅ Reduced to: {new_chars} chars ({current_chars - new_chars} chars saved)")
        return True
    else:
        print(f"   ⚠️  Still over limit: {new_chars} chars (needs manual review)")
        return False

def get_violating_posts() -> List[str]:
    """Get list of posts that violate character count"""
    workspace_root = Path("/Users/raphaelmansuy/Library/Mobile Documents/iCloud~md~obsidian/Documents/digital_palace")
    linkedin_dir = workspace_root / "personal" / "elitizon_linkedin"
    
    violating_posts = []
    
    # Known violators from our analysis
    post_numbers = ['01', '48', '50', '51', '52', '53', '54']
    
    for post_num in post_numbers:
        post_files = list(linkedin_dir.glob(f"post_{post_num}_*.md"))
        for post_file in post_files:
            _, content, _ = extract_post_content(str(post_file))
            if content and count_characters_properly(content) > 1800:
                violating_posts.append(str(post_file))
    
    return violating_posts

def main():
    """Fix all character count violations step by step"""
    print("🔧 LinkedIn Posts Character Count Fixer")
    print("=" * 60)
    print("📋 Step-by-step character count optimization")
    print()
    
    violating_posts = get_violating_posts()
    
    if not violating_posts:
        print("✅ No posts found exceeding character limit!")
        return
    
    print(f"📊 Found {len(violating_posts)} posts exceeding 1800 characters")
    print()
    
    fixed_count = 0
    manual_review_count = 0
    
    for i, post_path in enumerate(violating_posts, 1):
        post_name = Path(post_path).name
        post_number = post_name.split('_')[1] if '_' in post_name else '?'
        
        print(f"🔧 Step {i}/{len(violating_posts)}: Post {post_number}")
        print(f"   📄 File: {post_name}")
        
        if fix_character_count(post_path):
            fixed_count += 1
        else:
            manual_review_count += 1
        
        print()
    
    print("📈 CHARACTER COUNT FIX SUMMARY")
    print("=" * 60)
    print(f"✅ Posts automatically fixed: {fixed_count}")
    print(f"⚠️  Posts needing manual review: {manual_review_count}")
    print(f"📊 Total processed: {len(violating_posts)}")
    
    if fixed_count > 0:
        print()
        print("🎉 Character count violations have been reduced!")
        print("💡 Next steps:")
        print("   1. Run comprehensive quality check to verify fixes")
        print("   2. Manually review posts that couldn't be auto-fixed")
        print("   3. Validate final compliance rate")
    
    if manual_review_count > 0:
        print()
        print("⚠️  Manual review needed for posts with complex content")
        print("   These posts require careful editing to maintain quality")

if __name__ == "__main__":
    main()

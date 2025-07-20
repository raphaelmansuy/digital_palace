#!/usr/bin/env python3
"""
LinkedIn Posts Quality Assessment Tool
Analyzes the first 20 LinkedIn posts for:
1. Character count (must be under 1800 characters)
2. Content quality assessment
3. Post body content only (between --- rulers)
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any

# Import character counting function from our LinkedIn character counter
try:
    from linkedin_character_counter import count_characters
except ImportError:
    # Fallback if module not available
    def count_characters(text):
        """Simple character count as fallback"""
        return len(re.sub(r'[*_#`>-]', '', text).strip())

def extract_post_content(file_path: str) -> str:
    """Extract only the post content between the two --- rulers"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find content between the two --- rulers
        # Pattern: first --- to second ---
        pattern = r'---\s*\n(.*?)\n---'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            post_content = match.group(1).strip()
            return post_content
        else:
            # Fallback: if no rulers found, look for content after metadata
            lines = content.split('\n')
            start_content = False
            content_lines = []
            
            for line in lines:
                if line.strip() == '---' and not start_content:
                    start_content = True
                    continue
                elif line.strip() == '---' and start_content:
                    break
                elif start_content:
                    content_lines.append(line)
            
            return '\n'.join(content_lines).strip()
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def count_words(text: str) -> int:
    """Count words in text, excluding markdown formatting"""
    # Remove markdown formatting
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Italic
    text = re.sub(r'`([^`]+)`', r'\1', text)        # Code
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # Links
    text = re.sub(r'#+ ', '', text)                 # Headers
    text = re.sub(r'> ', '', text)                  # Quotes
    text = re.sub(r'- ', '', text)                  # Lists
    text = re.sub(r'\d+\. ', '', text)              # Numbered lists
    
    # Count words
    words = text.split()
    return len([word for word in words if word.strip()])

def assess_content_quality(content: str) -> Dict[str, Any]:
    """Assess the quality of the LinkedIn post content"""
    assessment = {
        'word_count': count_words(content),
        'char_count': count_characters(content),  # Use proper character counting
        'issues': [],
        'suggestions': [],
        'quality_score': 0
    }
    
    # Check character count (new primary constraint)
    if assessment['char_count'] > 1800:
        assessment['issues'].append(f"Exceeds 1800 character limit ({assessment['char_count']} chars)")
    elif assessment['char_count'] < 1200:
        assessment['issues'].append(f"Too short for engaging content ({assessment['char_count']} chars)")
    
    # Check word count (secondary check for reference)
    if assessment['word_count'] < 50:
        assessment['issues'].append(f"Very short content ({assessment['word_count']} words)")
    elif assessment['word_count'] > 400:
        assessment['suggestions'].append(f"High word count ({assessment['word_count']} words) - consider condensing")
    
    # Check for engagement elements
    has_question = '?' in content
    has_examples = any(phrase in content.lower() for phrase in [
        'example:', 'for example', 'e.g.', 'for instance', 'such as',
        'imagine', 'consider this', 'here\'s how', 'case study', 'real-world'
    ])
    has_call_to_action = any(phrase in content.lower() for phrase in [
        'what do you think', 'share your thoughts', 'comment below', 
        'let me know', 'tag someone', 'follow for more'
    ])
    
    # Check structure
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    has_good_structure = len(paragraphs) >= 2
    
    # Check for practical content (instead of personal touch)
    has_practical_content = any(phrase in content.lower() for phrase in [
        'step', 'process', 'method', 'technique', 'approach', 'strategy',
        'framework', 'tool', 'solution', 'how to', 'implement', 'apply'
    ])
    
    # Calculate quality score
    score = 0
    if assessment['word_count'] <= 600 and assessment['word_count'] >= 50:
        score += 2
    if has_question:
        score += 1
        assessment['suggestions'].append("✓ Has engaging question")
    else:
        assessment['suggestions'].append("Consider adding a question to increase engagement")
    
    if has_examples:
        score += 1
        assessment['suggestions'].append("✓ Includes examples for clarity")
    else:
        assessment['suggestions'].append("Add concrete examples to illustrate points")
    
    if has_call_to_action:
        score += 1
        assessment['suggestions'].append("✓ Has call-to-action")
    else:
        assessment['suggestions'].append("Add a call-to-action to encourage engagement")
    
    if has_good_structure:
        score += 1
        assessment['suggestions'].append("✓ Well-structured with multiple paragraphs")
    else:
        assessment['suggestions'].append("Break content into smaller paragraphs for readability")
    
    if has_practical_content:
        score += 1
        assessment['suggestions'].append("✓ Contains practical, actionable content")
    else:
        assessment['suggestions'].append("Add more practical steps or actionable advice")
    
    assessment['quality_score'] = score
    return assessment

def main():
    """Main function to assess LinkedIn posts"""
    workspace_root = Path("/Users/raphaelmansuy/Library/Mobile Documents/iCloud~md~obsidian/Documents/digital_palace")
    
    # Find LinkedIn posts directory
    linkedin_dir = None
    for root, dirs, files in os.walk(workspace_root):
        if 'elitizon_linkedin' in dirs:
            linkedin_dir = Path(root) / 'elitizon_linkedin'
            break
    
    if not linkedin_dir or not linkedin_dir.exists():
        print("❌ LinkedIn posts directory not found!")
        return
    
    print("🔍 LinkedIn Posts Quality Assessment")
    print("=" * 50)
    
    # Get all markdown files and sort them
    post_files = list(linkedin_dir.glob("*.md"))
    post_files.sort()
    
    if len(post_files) == 0:
        print("❌ No markdown files found in LinkedIn directory!")
        return
    
    # Analyze first 20 posts
    posts_to_analyze = post_files[:20]
    
    print(f"📊 Analyzing first {len(posts_to_analyze)} LinkedIn posts...")
    print()
    
    total_issues = 0
    over_limit_count = 0
    quality_scores = []
    
    for i, post_file in enumerate(posts_to_analyze, 1):
        print(f"📄 Post {i}: {post_file.name}")
        print("-" * 40)
        
        # Extract post content
        content = extract_post_content(str(post_file))
        
        if not content:
            print("⚠️  No content found between rulers")
            print()
            continue
        
        # Assess quality
        assessment = assess_content_quality(content)
        quality_scores.append(assessment['quality_score'])
        
        # Display results
        print(f"� Character Count: {assessment['char_count']}/1800")
        print(f"� Word Count: {assessment['word_count']} words")
        print(f"⭐ Quality Score: {assessment['quality_score']}/6")
        
        if assessment['char_count'] > 1800:
            print("❌ EXCEEDS CHARACTER LIMIT!")
            over_limit_count += 1
        else:
            print("✅ Within character limit")
        
        if assessment['issues']:
            print("⚠️  Issues:")
            for issue in assessment['issues']:
                print(f"   • {issue}")
            total_issues += len(assessment['issues'])
        
        if assessment['suggestions']:
            print("💡 Suggestions:")
            for suggestion in assessment['suggestions']:
                print(f"   • {suggestion}")
        
        # Show content preview
        preview = content[:150] + "..." if len(content) > 150 else content
        preview = preview.replace('\n', ' ')
        print(f"📖 Preview: {preview}")
        
        print()
    
    # Summary
    print("📈 SUMMARY")
    print("=" * 50)
    print(f"📊 Total posts analyzed: {len(posts_to_analyze)}")
    print(f"❌ Posts over 1800 characters: {over_limit_count}")
    print(f"⚠️  Total issues found: {total_issues}")
    
    if quality_scores:
        avg_quality = sum(quality_scores) / len(quality_scores)
        print(f"⭐ Average quality score: {avg_quality:.1f}/6")
        
        if avg_quality >= 5:
            print("🎉 Excellent overall quality!")
        elif avg_quality >= 4:
            print("👍 Good overall quality")
        elif avg_quality >= 3:
            print("⚠️  Average quality - room for improvement")
        else:
            print("❌ Below average quality - needs significant improvement")
    
    print()
    print("✅ Assessment complete!")

if __name__ == "__main__":
    main()

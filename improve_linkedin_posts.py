#!/usr/bin/env python3
"""
LinkedIn Posts Analysis Tool
Analyzes posts for character count compliance and provides improvement suggestions.
Does NOT automatically modify posts - provides guidance for manual improvements.
Target: 1800 characters maximum per LinkedIn post.
"""

import os
import re
from pathlib import Path
from typing import Dict, Any

    print("🔍 LinkedIn Posts Character Analysis Tool")
    print("=" * 60)
    print("Target: 1800 characters maximum per post") extract_post_content(file_path: str) -> tuple[str, str, str]:
    """Extract metadata, post content, and remaining content separately"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            full_content = f.read()
        
        # Find content between the two --- rulers
        pattern = r'(---\s*\n.*?\n---\s*\n)(.*?)(\n---.*)?$'
        match = re.search(pattern, full_content, re.DOTALL)
        
        if match:
            metadata = match.group(1) if match.group(1) else ""
            post_content = match.group(2).strip() if match.group(2) else ""
            remaining = match.group(3) if match.group(3) else ""
            return metadata, post_content, remaining
        else:
            # Fallback parsing
            lines = full_content.split('\n')
            metadata_lines = []
            content_lines = []
            remaining_lines = []
            
            section = 0  # 0: before first ---, 1: between ---, 2: after second ---
            
            for line in lines:
                if line.strip() == '---':
                    section += 1
                    if section <= 2:
                        metadata_lines.append(line)
                    else:
                        remaining_lines.append(line)
                elif section == 0:
                    metadata_lines.append(line)
                elif section == 1:
                    content_lines.append(line)
                else:
                    remaining_lines.append(line)
            
            metadata = '\n'.join(metadata_lines) + '\n'
            post_content = '\n'.join(content_lines).strip()
            remaining = '\n'.join(remaining_lines) if remaining_lines else ""
            
            return metadata, post_content, remaining
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return "", "", ""

def count_characters(text: str) -> int:
    """Count characters in text, excluding markdown formatting (same logic as linkedin_character_counter.py)"""
    if not text:
        return 0
    
    # Remove markdown code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove inline code
    text = re.sub(r'`[^`]*`', '', text)
    
    # Remove markdown links [text](url) - keep only the link text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove markdown formatting characters (* ** _ __ # etc.) but keep the content
    text = re.sub(r'[*_#`>-]', '', text)
    
    # Remove extra whitespace but keep single spaces and newlines
    text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces/tabs to single space
    text = re.sub(r'\n+', '\n', text)    # Multiple newlines to single newline
    
    # Count characters (including spaces and newlines for readability)
    return len(text.strip())

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

def analyze_post_content(content: str) -> Dict[str, Any]:
    """Identify which sections can be safely trimmed"""
    lines = content.split('\n')
    sections = {
        'intro': [],
        'problem': [],
        'solution': [],
        'examples': [],
        'conclusion': [],
        'other': []
    }
    
    current_section = 'other'
    
    for line in lines:
        line_lower = line.lower().strip()
        
        # Identify section types
        if any(keyword in line_lower for keyword in ['problem', 'challenge', 'issue', 'struggle']):
            current_section = 'problem'
        elif any(keyword in line_lower for keyword in ['solution', 'answer', 'how to', 'approach', 'method']):
            current_section = 'solution'
        elif any(keyword in line_lower for keyword in ['example', 'imagine', 'consider', 'case study']):
            current_section = 'examples'
        elif any(keyword in line_lower for keyword in ['conclusion', 'summary', 'takeaway', 'key point']):
            current_section = 'conclusion'
        elif line.startswith('#'):
            if 'problem' in line_lower:
                current_section = 'problem'
            elif any(keyword in line_lower for keyword in ['solution', 'framework', 'method']):
                current_section = 'solution'
            else:
                current_section = 'intro'
        
        sections[current_section].append(line)
    
    return sections

def trim_content_intelligently(content: str, target_words: int = 580) -> str:
    """Trim content while preserving core value and structure"""
    current_words = count_words(content)
    
    if current_words <= target_words:
        return content
    
    words_to_cut = current_words - target_words
    
    # Split into sections
    sections = identify_sections_to_trim(content)
    
    # Priority for trimming (least important first)
    trim_priorities = [
        ('other', 0.3),      # Trim 30% of miscellaneous content
        ('intro', 0.2),      # Trim 20% of intro
        ('conclusion', 0.2), # Trim 20% of conclusion
        ('problem', 0.15),   # Trim 15% of problem description
        ('solution', 0.1),   # Trim 10% of solution (preserve core value)
        ('examples', 0.05),  # Trim 5% of examples (they're valuable)
    ]
    
    trimmed_sections = {}
    total_words_cut = 0
    
    for section_name, trim_ratio in trim_priorities:
        if total_words_cut >= words_to_cut:
            break
            
        section_content = '\n'.join(sections[section_name])
        section_words = count_words(section_content)
        target_cut = min(int(section_words * trim_ratio), words_to_cut - total_words_cut)
        
        if target_cut > 0:
            trimmed_sections[section_name] = trim_section(section_content, target_cut)
            actual_cut = section_words - count_words(trimmed_sections[section_name])
            total_words_cut += actual_cut
        else:
            trimmed_sections[section_name] = section_content
    
    # Reconstruct content
    result_lines = []
    current_section = 'other'
    
    for line in content.split('\n'):
        line_lower = line.lower().strip()
        
        # Determine section
        if any(keyword in line_lower for keyword in ['problem', 'challenge', 'issue', 'struggle']):
            current_section = 'problem'
        elif any(keyword in line_lower for keyword in ['solution', 'answer', 'how to', 'approach', 'method']):
            current_section = 'solution'
        elif any(keyword in line_lower for keyword in ['example', 'imagine', 'consider', 'case study']):
            current_section = 'examples'
        elif any(keyword in line_lower for keyword in ['conclusion', 'summary', 'takeaway', 'key point']):
            current_section = 'conclusion'
        elif line.startswith('#'):
            if 'problem' in line_lower:
                current_section = 'problem'
            elif any(keyword in line_lower for keyword in ['solution', 'framework', 'method']):
                current_section = 'solution'
            else:
                current_section = 'intro'
        
        # Use trimmed version if available
        if current_section in trimmed_sections:
            section_lines = trimmed_sections[current_section].split('\n')
            if line in section_lines:
                result_lines.append(line)
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)

def trim_section(section_content: str, words_to_cut: int) -> str:
    """Trim a specific section by removing redundant or verbose parts"""
    if not section_content.strip():
        return section_content
    
    lines = [line for line in section_content.split('\n') if line.strip()]
    
    # Remove redundant phrases and verbose explanations
    redundant_patterns = [
        r'\b(very|really|quite|extremely|absolutely|completely|totally)\b',
        r'\b(basically|essentially|fundamentally|ultimately)\b',
        r'\b(obviously|clearly|certainly|definitely|undoubtedly)\b',
        r'\b(in fact|as a matter of fact|to be honest|frankly speaking)\b',
        r'\b(it goes without saying|needless to say)\b',
    ]
    
    # Simplify sentences
    improved_lines = []
    for line in lines:
        improved_line = line
        
        # Remove redundant words
        for pattern in redundant_patterns:
            improved_line = re.sub(pattern, '', improved_line, flags=re.IGNORECASE)
        
        # Clean up extra spaces
        improved_line = re.sub(r'\s+', ' ', improved_line).strip()
        
        if improved_line:
            improved_lines.append(improved_line)
    
    result = '\n'.join(improved_lines)
    
    # If still need more cuts, remove some sentences
    current_words = count_words(result)
    target_words = current_words - words_to_cut
    
    if current_words > target_words:
        sentences = [s.strip() for s in result.split('.') if s.strip()]
        
        # Remove less essential sentences (those with certain patterns)
        essential_sentences = []
        for sentence in sentences:
            sentence_lower = sentence.lower()
            
            # Keep sentences with examples, numbers, or key concepts
            if any(keyword in sentence_lower for keyword in [
                'example', 'step', 'method', 'technique', 'framework',
                '%', 'increase', 'decrease', 'result', 'outcome'
            ]):
                essential_sentences.append(sentence)
            elif len(essential_sentences) < len(sentences) * 0.7:  # Keep at least 70%
                essential_sentences.append(sentence)
        
        result = '. '.join(essential_sentences)
        if result and not result.endswith('.'):
            result += '.'
    
    return result

def save_improved_post(file_path: str, metadata: str, improved_content: str, remaining: str):
    """Save the improved post back to file"""
    full_content = metadata + improved_content
    if remaining:
        full_content += '\n' + remaining
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

def analyze_post_content(content: str) -> Dict[str, Any]:
    """Analyze post content and provide improvement suggestions"""
    char_count = count_characters(content)
    word_count = count_words(content)
    
    # Count paragraphs and sentences
    paragraphs = [p for p in content.split('\n\n') if p.strip()]
    sentences = [s for s in content.split('.') if s.strip()]
    
    # Identify verbose patterns
    verbose_patterns = [
        (r'\b(very|really|quite|extremely|absolutely|completely|totally)\b', 'Remove intensifiers'),
        (r'\b(basically|essentially|fundamentally|ultimately)\b', 'Remove filler words'),
        (r'\b(obviously|clearly|certainly|definitely|undoubtedly)\b', 'Remove certainty modifiers'),
        (r'\b(in fact|as a matter of fact|to be honest|frankly speaking)\b', 'Remove conversational fillers'),
        (r'\b(it goes without saying|needless to say)\b', 'Remove redundant phrases'),
    ]
    
    suggestions = []
    verbose_count = 0
    
    for pattern, suggestion in verbose_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            verbose_count += len(matches)
            suggestions.append(f"• {suggestion}: Found {len(matches)} instances")
    
    # Check for long sentences (>25 words)
    long_sentences = [s for s in sentences if len(s.split()) > 25]
    if long_sentences:
        suggestions.append(f"• Break down {len(long_sentences)} long sentences (>25 words)")
    
    # Check for repetitive phrases
    words = content.lower().split()
    word_freq = {}
    for word in words:
        if len(word) > 4:  # Only check longer words
            word_freq[word] = word_freq.get(word, 0) + 1
    
    repeated_words = [word for word, count in word_freq.items() if count > 3]
    if repeated_words:
        suggestions.append(f"• Reduce repetition of words: {', '.join(repeated_words[:5])}")
    
    return {
        'char_count': char_count,
        'word_count': word_count,
        'paragraph_count': len(paragraphs),
        'sentence_count': len(sentences),
        'verbose_count': verbose_count,
        'suggestions': suggestions,
        'over_limit': char_count > 2500,
        'excess_chars': max(0, char_count - 2500),
        'reduction_needed_percent': max(0, (char_count - 2500) / char_count * 100) if char_count > 0 else 0
    }

def main():
    """Main function to analyze LinkedIn posts for character compliance"""
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
    
    print("� LinkedIn Posts Character Analysis Tool")
    print("=" * 60)
    print("Target: 2500 characters maximum per post")
    print("This tool provides analysis and suggestions WITHOUT modifying files")
    print("=" * 60)
    
    # Get all markdown files and sort them
    post_files = list(linkedin_dir.glob("*.md"))
    post_files.sort()
    
    # Analyze posts for character count compliance
    posts_over_limit = []
    posts_compliant = []
    
    for post_file in post_files:
        metadata, content, remaining = extract_post_content(str(post_file))
        if not content:
            continue
            
        analysis = analyze_post_content(content)
        
        if analysis['over_limit']:
            posts_over_limit.append((post_file, analysis))
        else:
            posts_compliant.append((post_file, analysis))
    
    # Report summary
    total_posts = len(posts_over_limit) + len(posts_compliant)
    print(f"\n📈 Analysis Summary:")
    print(f"   Total posts analyzed: {total_posts}")
    print(f"   ✅ Posts within limit (≤2500 chars): {len(posts_compliant)}")
    print(f"   ❌ Posts over limit (>2500 chars): {len(posts_over_limit)}")
    
    if len(posts_compliant) > 0:
        print(f"\n🎉 Compliant Posts:")
        for post_file, analysis in posts_compliant[:10]:  # Show first 10
            print(f"   ✅ {post_file.name}: {analysis['char_count']} chars ({2500-analysis['char_count']} remaining)")
    
    if len(posts_over_limit) > 0:
        print(f"\n⚠️  Posts Requiring Manual Reduction:")
        print("-" * 60)
        
        for post_file, analysis in posts_over_limit:
            print(f"\n📝 {post_file.name}")
            print(f"   Character count: {analysis['char_count']} (over by {analysis['excess_chars']})")
            print(f"   Reduction needed: {analysis['reduction_needed_percent']:.1f}%")
            print(f"   Words: {analysis['word_count']} | Paragraphs: {analysis['paragraph_count']} | Sentences: {analysis['sentence_count']}")
            
            if analysis['suggestions']:
                print(f"   💡 Improvement suggestions:")
                for suggestion in analysis['suggestions'][:5]:  # Show top 5 suggestions
                    print(f"      {suggestion}")
            print()
    
    print("\n🔧 Manual Improvement Guidelines:")
    print("1. Use linkedin_character_counter.py to check specific posts")
    print("2. Focus on removing filler words and redundant phrases")
    print("3. Break long sentences into shorter, punchier ones")
    print("4. Combine or remove less essential paragraphs")
    print("5. Keep examples and actionable content")
    print("6. Verify with: python3 check_post.py 'path/to/post.md'")

if __name__ == "__main__":
    main()

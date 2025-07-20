#!/usr/bin/env python3
"""
LinkedIn Posts Improvement Tool
Automatically trims posts that exceed 600 words while maintaining:
1. Core message and value
2. Examples and practical content
3. Engaging questions
4. Good structure
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any

def extract_post_content(file_path: str) -> tuple[str, str, str]:
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

def identify_sections_to_trim(content: str) -> Dict[str, Any]:
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

def main():
    """Main function to improve LinkedIn posts"""
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
    
    print("🔧 LinkedIn Posts Improvement Tool")
    print("=" * 50)
    
    # Get all markdown files and sort them
    post_files = list(linkedin_dir.glob("*.md"))
    post_files.sort()
    
    # Focus on posts that exceed 600 words
    posts_to_improve = []
    
    for post_file in post_files[:20]:  # First 20 posts
        metadata, content, remaining = extract_post_content(str(post_file))
        word_count = count_words(content)
        
        if word_count > 600:
            posts_to_improve.append((post_file, word_count, metadata, content, remaining))
    
    if not posts_to_improve:
        print("🎉 All posts are already within the 600-word limit!")
        return
    
    print(f"📊 Found {len(posts_to_improve)} posts that need improvement:")
    for post_file, word_count, _, _, _ in posts_to_improve:
        print(f"   • {post_file.name}: {word_count} words ({word_count - 600} over limit)")
    
    print("\n🚀 Starting improvement process...")
    
    improved_count = 0
    
    for post_file, original_words, metadata, content, remaining in posts_to_improve:
        print(f"\n📝 Improving: {post_file.name}")
        print(f"   Original: {original_words} words")
        
        # Trim content intelligently
        improved_content = trim_content_intelligently(content, 580)  # Target 580 to be safe
        new_word_count = count_words(improved_content)
        
        print(f"   Improved: {new_word_count} words")
        print(f"   Saved: {original_words - new_word_count} words")
        
        if new_word_count <= 600:
            # Save the improved version
            save_improved_post(str(post_file), metadata, improved_content, remaining)
            improved_count += 1
            print("   ✅ Successfully improved and saved!")
        else:
            print("   ⚠️  Still over limit, may need manual review")
    
    print(f"\n🎉 Improvement Summary:")
    print(f"   📊 Posts processed: {len(posts_to_improve)}")
    print(f"   ✅ Successfully improved: {improved_count}")
    print(f"   ⚠️  Need manual review: {len(posts_to_improve) - improved_count}")
    
    if improved_count > 0:
        print(f"\n💡 Tip: Run the assessment tool again to verify improvements:")
        print(f"   python assess_linkedin_posts.py")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
ASCII Diagram Alignment Verification Script
Checks for alignment issues in markdown files with ASCII diagrams.
"""

import re
from pathlib import Path

def analyze_file(filepath):
    """Analyze ASCII diagrams in a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    lines = content.split('\n')
    
    print(f"\n{'='*80}")
    print(f"Analyzing: {filepath}")
    print(f"{'='*80}\n")
    
    # Pattern 1: Check separator lines (─ character)
    print("CHECKING SEPARATOR LINES (─ character):")
    print("-" * 80)
    separator_pattern = r'# ─+$'
    separator_lines = []
    
    for i, line in enumerate(lines, 1):
        if re.match(separator_pattern, line):
            separator_lines.append((i, line))
    
    if separator_lines:
        print(f"Found {len(separator_lines)} separator lines\n")
        separator_lengths = {}
        
        for line_num, line in separator_lines:
            # Count the dash characters
            dash_count = len(re.search(r'─+', line).group())
            if dash_count not in separator_lengths:
                separator_lengths[dash_count] = []
            separator_lengths[dash_count].append((line_num, line))
        
        # Report findings
        if len(separator_lengths) == 1:
            length = list(separator_lengths.keys())[0]
            print(f"✓ All {len(separator_lines)} separators are consistent: {length} dashes")
        else:
            print("⚠ INCONSISTENT separator lengths found:")
            for length in sorted(separator_lengths.keys()):
                lines_with_this_length = separator_lengths[length]
                print(f"\n  {length} dashes: {len(lines_with_this_length)} occurrences")
                for line_num, line_text in lines_with_this_length[:3]:  # Show first 3
                    print(f"    Line {line_num}: {line_text[:70]}")
                if len(lines_with_this_length) > 3:
                    print(f"    ... and {len(lines_with_this_length) - 3} more")
                    line_nums = [item[0] for item in lines_with_this_length]
                    issues.append(f"Separator inconsistency: {length} dashes at lines {line_nums}")
    else:
        print("No separator lines found.\n")
    
    # Pattern 2: Check tree diagrams (├─, └─, │)
    print("\nCHECKING TREE DIAGRAMS (├─, └─, │ characters):")
    print("-" * 80)
    tree_pattern = r'[├│└]'
    tree_sections = []
    current_section = None
    
    for i, line in enumerate(lines, 1):
        if re.search(tree_pattern, line):
            if current_section is None or i > current_section['end'] + 1:
                current_section = {'start': i, 'end': i, 'lines': [line]}
                tree_sections.append(current_section)
            else:
                current_section['end'] = i
                current_section['lines'].append(line)
    
    if tree_sections:
        print(f"Found {len(tree_sections)} tree diagram sections\n")
        
        for idx, section in enumerate(tree_sections, 1):
            print(f"\nSection {idx} (Lines {section['start']}-{section['end']}):")
            
            # Check alignment of tree connectors
            indentation_levels = set()
            alignment_issues = []
            
            for line in section['lines']:
                # Find position of first tree character
                match = re.search(tree_pattern, line)
                if match:
                    pos = match.start()
                    indentation_levels.add(pos)
                    
                    # Verify proper tree structure
                    if '├' in line and line.rstrip()[-2:] != '─' and '─' not in line:
                        alignment_issues.append(f"Malformed: {line[:60]}")
            
            print(f"  Indentation levels: {sorted(indentation_levels)}")
            
            # Show sample lines
            for line in section['lines'][:5]:
                print(f"    {line[:75]}")
            if len(section['lines']) > 5:
                print(f"    ... ({len(section['lines']) - 5} more lines)")
            
            if alignment_issues:
                print("  ⚠ Alignment issues found:")
                for issue in alignment_issues[:3]:
                    print(f"    - {issue}")
                issues.extend(alignment_issues)
    else:
        print("No tree diagrams found.\n")
    
    # Pattern 3: Check box diagrams (┌─ ─┐, ├─ ─┤, └─ ─┘)
    print("\nCHECKING BOX DIAGRAMS (┌─┐, ├─┤, └─┘ characters):")
    print("-" * 80)
    box_pattern = r'[┌├└┐┤┘─]'
    box_sections = []
    current_box = None
    
    for i, line in enumerate(lines, 1):
        if re.search(box_pattern, line):
            if current_box is None or i > current_box['end'] + 1:
                current_box = {'start': i, 'end': i, 'lines': [line]}
                box_sections.append(current_box)
            else:
                current_box['end'] = i
                current_box['lines'].append(line)
    
    if box_sections:
        print(f"Found {len(box_sections)} potential box diagram sections\n")
        
        for idx, section in enumerate(box_sections, 1):
            # Check if it's actually a box (has top and bottom)
            has_top = any('┌' in line for line in section['lines'])
            has_bottom = any('└' in line for line in section['lines'])
            
            if has_top and has_bottom:
                print(f"\nBox {idx} (Lines {section['start']}-{section['end']}):")
                
                # Check width consistency
                widths = []
                for line in section['lines']:
                    if '─' in line:
                        width = len(re.search(r'─+', line).group())
                        widths.append(width)
                
                if widths:
                    if len(set(widths)) == 1:
                        print(f"  ✓ Width consistent: {widths[0]} dashes")
                    else:
                        print(f"  ⚠ Width inconsistent: {sorted(set(widths))}")
                        issues.append(f"Box width inconsistency at lines {section['start']}-{section['end']}")
                
                # Show sample
                for line in section['lines'][:4]:
                    print(f"    {line[:75]}")
                if len(section['lines']) > 4:
                    print(f"    ... ({len(section['lines']) - 4} more lines)")
    else:
        print("No box diagrams found.\n")
    
    # Pattern 4: Cost breakdowns and tree lists
    print("\nCHECKING COST BREAKDOWNS & LISTS:")
    print("-" * 80)
    cost_pattern = r'(Monthly|LLM|├|└)'
    cost_lines = []
    
    for i, line in enumerate(lines, 1):
        if 'Cost' in line or 'Breakdown' in line or re.search(cost_pattern, line):
            cost_lines.append((i, line))
    
    # Find actual cost breakdown sections
    cost_sections = []
    for i, (line_num, line) in enumerate(cost_lines):
        if 'Cost Estimate' in line or 'Monthly Cost Breakdown' in line:
            # Get surrounding lines
            start = max(0, line_num - 2)
            end = min(len(lines), line_num + 30)
            section_text = '\n'.join(lines[start:end])
            cost_sections.append((line_num, section_text))
    
    if cost_sections:
        print(f"Found {len(cost_sections)} cost breakdown sections\n")
        
        for idx, (line_num, section) in enumerate(cost_sections, 1):
            print(f"\nCost Section {idx} starting at line {line_num}:")
            
            # Verify tree alignment
            section_lines = section.split('\n')
            tree_starts = []
            
            for line in section_lines[:15]:  # Check first 15 lines
                if '├' in line or '└' in line:
                    match = re.search(r'(├|└)', line)
                    if match:
                        tree_starts.append(match.start())
            
            if tree_starts:
                if len(set(tree_starts)) == 1:
                    print(f"  ✓ Tree alignment consistent: column {tree_starts[0]}")
                else:
                    print(f"  ⚠ Tree alignment inconsistent: columns {sorted(set(tree_starts))}")
                    issues.append(f"Cost breakdown misalignment at line {line_num}")
            
            # Show sample
            for line in section_lines[:10]:
                if line.strip():
                    print(f"    {line[:75]}")
    else:
        print("No cost breakdown sections found.\n")
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    if not issues:
        print("✓ No alignment issues detected!\n")
    else:
        print(f"⚠ Found {len(issues)} potential issues:\n")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    
    return issues

if __name__ == '__main__':
    target_file = Path('/Users/raphaelmansuy/Github/00-obsidian/digital_palace/reference/technical-articles/2025-10-26-agentic-platform/05-implementation.md')
    
    if target_file.exists():
        issues = analyze_file(target_file)
        
        print("\n" + "="*80)
        if issues:
            print(f"RECOMMENDATION: Found {len(issues)} issues to review and fix")
        else:
            print("RECOMMENDATION: File passes ASCII diagram alignment checks")
        print("="*80 + "\n")
    else:
        print(f"Error: File not found at {target_file}")

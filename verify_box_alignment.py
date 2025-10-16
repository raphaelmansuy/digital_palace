#!/usr/bin/env python3
"""
Box Diagram Alignment Verification for 03-platforms-compared.md
"""

from pathlib import Path

def analyze_box_diagram(filepath):
    """Verify box diagram alignment."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    print("\n" + "="*80)
    print("BOX DIAGRAM ALIGNMENT VERIFICATION: 03-platforms-compared.md")
    print("="*80 + "\n")
    
    # Find the box diagram section
    in_box = False
    box_lines = []
    start_line = 0
    
    for i, line in enumerate(lines, 1):
        if '╔═══════════' in line:
            in_box = True
            start_line = i
        
        if in_box:
            box_lines.append((i, line))
        
        if in_box and '╚═══════════' in line:
            break
    
    if not box_lines:
        print("❌ No box diagram found!")
        return False
    
    print(f"Found box diagram at lines {start_line}-{box_lines[-1][0]}\n")
    
    # Verify box structure
    issues = []
    
    # Check line lengths (all should be 79 chars)
    print("CHECKING LINE LENGTHS:")
    print("-" * 80)
    line_lengths = {}
    
    for line_num, line in box_lines:
        length = len(line)
        if length not in line_lengths:
            line_lengths[length] = []
        line_lengths[length].append(line_num)
    
    if len(line_lengths) == 1 and list(line_lengths.keys())[0] == 79:
        print(f"✅ ALL {len(box_lines)} lines are exactly 79 characters")
    else:
        print("⚠️  INCONSISTENT line lengths found:")
        for length in sorted(line_lengths.keys()):
            count = len(line_lengths[length])
            lines_with_length = line_lengths[length][:3]
            print(f"   Length {length}: {count} lines (e.g., lines {lines_with_length})")
            issues.append(f"Inconsistent line length: {length}")
    
    # Check box corners
    print("\nCHECKING BOX CORNERS:")
    print("-" * 80)
    
    top_line = box_lines[0][1]
    bottom_line = box_lines[-1][1]
    
    if top_line.startswith('╔') and top_line.endswith('╗'):
        print("✅ Top corners correct (╔...╗)")
    else:
        print(f"❌ Top corners incorrect: {top_line[:10]}...{top_line[-10:]}")
        issues.append("Top corners incorrect")
    
    if bottom_line.startswith('╚') and bottom_line.endswith('╝'):
        print("✅ Bottom corners correct (╚...╝)")
    else:
        print(f"❌ Bottom corners incorrect: {bottom_line[:10]}...{bottom_line[-10:]}")
        issues.append("Bottom corners incorrect")
    
    # Check side borders
    print("\nCHECKING SIDE BORDERS:")
    print("-" * 80)
    side_issues = []
    
    for line_num, line in box_lines:
        if not line.startswith('║'):
            side_issues.append(f"Line {line_num}: doesn't start with ║")
        if not line.endswith('║'):
            side_issues.append(f"Line {line_num}: doesn't end with ║")
    
    if not side_issues:
        print(f"✅ All {len(box_lines)} lines have correct side borders (║...║)")
    else:
        print(f"❌ Found {len(side_issues)} side border issues:")
        for issue in side_issues[:3]:
            print(f"   {issue}")
        issues.extend(side_issues)
    
    # Check divider row
    print("\nCHECKING DIVIDER ROW:")
    print("-" * 80)
    divider_found = False
    
    for line_num, line in box_lines:
        if '╠═══════════' in line and '╣' in line:
            divider_found = True
            print(f"✅ Divider row found at line {line_num}")
            if len(line) == 79:
                print("   Width: 79 characters ✅")
            else:
                print(f"   Width: {len(line)} characters ❌ (should be 79)")
                issues.append(f"Divider row incorrect length: {len(line)}")
            break
    
    if not divider_found:
        print("❌ Divider row not found!")
        issues.append("Divider row missing")
    
    # Check alignment of content rows
    print("\nCHECKING CONTENT ALIGNMENT:")
    print("-" * 80)
    
    # Find rows with feature names
    feature_rows = [line for num, line in box_lines if line.startswith('║  ') and not any(c in line for c in '╔╚╠═╣')]
    
    if feature_rows:
        print(f"Found {len(feature_rows)} content rows")
        print("\nSample rows (first 5):")
        for i, row in enumerate(feature_rows[:5], 1):
            print(f"  {i}. {row[:79]}")
        
        # Check for consistent spacing
        padding_check = all(line.startswith('║  ') for line in feature_rows)
        if padding_check:
            print("\n✅ All content rows have consistent left padding (║  )")
        else:
            print("\n⚠️  Some content rows have inconsistent left padding")
            issues.append("Inconsistent left padding in content rows")
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80 + "\n")
    
    if not issues:
        print("✅ BOX DIAGRAM IS PERFECTLY ALIGNED\n")
        return True
    else:
        print(f"❌ Found {len(issues)} issues:\n")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        print()
        return False

if __name__ == '__main__':
    target_file = Path('/Users/raphaelmansuy/Github/00-obsidian/digital_palace/reference/technical-articles/2025-10-26-agentic-platform/03-platforms-compared.md')
    
    if target_file.exists():
        success = analyze_box_diagram(target_file)
        if success:
            print("✅ FILE PASSES BOX ALIGNMENT VERIFICATION")
        else:
            print("⚠️  FILE HAS ALIGNMENT ISSUES - PLEASE REVIEW")
    else:
        print(f"Error: File not found at {target_file}")

#!/usr/bin/env python3
"""
Fix LinkedIn Post Headers - Batch Update Tool
Updates header formats to comply with quality guidelines:
- First header (title) should NOT have 👉
- All other level 2 headers should have 👉
"""

import re
from pathlib import Path

def fix_header_formats(file_path: str) -> bool:
    """Fix header formats in a LinkedIn post"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Split content into sections
        parts = content.split('---')
        if len(parts) < 3:
            print(f"⚠️  No content section found in {file_path}")
            return False
        
        # Work with the middle section (between rulers)
        before_content = '---'.join(parts[:1]) + '---'
        post_content = parts[1]
        after_content = '---' + '---'.join(parts[2:])
        
        # Track if this is the first header
        lines = post_content.split('\n')
        modified_lines = []
        first_header_found = False
        
        for line in lines:
            if line.strip().startswith('##'):
                if not first_header_found:
                    # First header - remove 👉 if present
                    if '👉' in line:
                        line = line.replace('👉', '').replace('## ', '## ')
                        line = re.sub(r'##\s+', '## ', line)  # Clean up extra spaces
                    first_header_found = True
                else:
                    # Subsequent level 2 headers - add 👉 if missing
                    if '👉' not in line and line.strip().startswith('##') and not line.strip().startswith('###'):
                        line = line.replace('## ', '## 👉 ')
            
            modified_lines.append(line)
        
        # Reconstruct content
        new_post_content = '\n'.join(modified_lines)
        new_content = before_content + new_post_content + after_content
        
        # Only write if changes were made
        if new_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Fix header formats in all LinkedIn posts"""
    workspace_root = Path("/Users/raphaelmansuy/Library/Mobile Documents/iCloud~md~obsidian/Documents/digital_palace")
    linkedin_dir = workspace_root / "personal" / "elitizon_linkedin"
    
    if not linkedin_dir.exists():
        print("❌ LinkedIn directory not found!")
        return
    
    print("🔧 LinkedIn Posts Header Format Fixer")
    print("=" * 50)
    print(f"📁 Processing: {linkedin_dir}")
    print()
    
    # Get all post files
    post_files = list(linkedin_dir.glob("post_*.md"))
    post_files.sort()
    
    if not post_files:
        print("❌ No post_*.md files found!")
        return
    
    print(f"📊 Found {len(post_files)} posts to process...")
    print()
    
    fixed_count = 0
    skipped_count = 0
    error_count = 0
    
    for post_file in post_files:
        post_number = post_file.name.split('_')[1] if '_' in post_file.name else '?'
        
        try:
            if fix_header_formats(str(post_file)):
                print(f"✅ Fixed Post {post_number}: {post_file.name}")
                fixed_count += 1
            else:
                print(f"⚪ No changes needed for Post {post_number}")
                skipped_count += 1
        except Exception as e:
            print(f"❌ Error fixing Post {post_number}: {e}")
            error_count += 1
    
    print()
    print("📈 HEADER FIX SUMMARY")
    print("=" * 50)
    print(f"✅ Posts fixed: {fixed_count}")
    print(f"⚪ Posts skipped (no changes needed): {skipped_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📊 Total processed: {len(post_files)}")
    
    if fixed_count > 0:
        print()
        print("🎉 Header formats have been updated!")
        print("💡 Next steps:")
        print("   1. Run quality check again to verify fixes")
        print("   2. Address character count violations")
        print("   3. Review content quality improvements")
    else:
        print("ℹ️  No header format issues found.")

if __name__ == "__main__":
    main()

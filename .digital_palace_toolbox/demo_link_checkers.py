#!/usr/bin/env python3
"""
Digital Palace Link Checker Commands Demo

This script demonstrates how to use the link checking tools in the Digital Palace toolbox.
It provides example commands and shows how to integrate the tools with VSCode Copilot.

Usage:
    python demo_link_checkers.py
"""

import os
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and display results"""
    print(f"\n{'='*60}")
    print(f"🔧 {description}")
    print(f"{'='*60}")
    print(f"Command: {command}")
    print("-" * 60)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=Path(__file__).parent, check=False)
        
        if result.stdout:
            print("OUTPUT:")
            print(result.stdout)
        
        if result.stderr:
            print("ERRORS:")
            print(result.stderr)
        
        print(f"Exit code: {result.returncode}")
        return result.returncode == 0
        
    except subprocess.SubprocessError as e:
        print(f"Error running command: {e}")
        return False

def main():
    """Demonstrate link checker commands"""
    print("🧰 Digital Palace Link Checker Commands Demo")
    print("=" * 60)
    
    # Change to the toolbox directory
    toolbox_dir = Path(__file__).parent
    os.chdir(toolbox_dir)
    
    # Get the Digital Palace root directory
    palace_root = toolbox_dir.parent
    
    print(f"📁 Toolbox Directory: {toolbox_dir}")
    print(f"📁 Palace Root: {palace_root}")
    
    # Check if README.md exists in the parent directory
    readme_path = palace_root / "README.md"
    if not readme_path.exists():
        print(f"❌ README.md not found at {readme_path}")
        return
    
    print("\n🔍 Available Link Checker Commands:")
    print("=" * 60)
    
    # 1. Check internal links in README.md
    commands = [
        {
            "cmd": f"python check_internal_links.py {readme_path}",
            "desc": "Check internal links in README.md (text format)"
        },
        {
            "cmd": f"python check_internal_links.py {readme_path} --format json",
            "desc": "Check internal links in README.md (JSON format)"
        },
        {
            "cmd": f"python check_internal_links.py {readme_path} --format markdown",
            "desc": "Check internal links in README.md (Markdown format)"
        },
        {
            "cmd": f"python check_external_links.py {readme_path}",
            "desc": "Check external links in README.md (text format)"
        },
        {
            "cmd": f"python check_external_links.py {readme_path} --format json",
            "desc": "Check external links in README.md (JSON format)"
        },
        {
            "cmd": f"python check_external_links.py {readme_path} --timeout 10",
            "desc": "Check external links with 10-second timeout"
        }
    ]
    
    # Check if guides directory exists
    guides_dir = palace_root / "guides"
    if guides_dir.exists():
        commands.extend([
            {
                "cmd": f"python check_internal_links.py {guides_dir}",
                "desc": "Check internal links in guides directory"
            },
            {
                "cmd": f"python check_external_links.py {guides_dir} --format markdown",
                "desc": "Check external links in guides directory (Markdown format)"
            }
        ])
    
    # Show commands without running them all (to avoid long execution time)
    for i, cmd_info in enumerate(commands, 1):
        print(f"\n{i}. {cmd_info['desc']}")
        print(f"   Command: {cmd_info['cmd']}")
    
    print("\n" + "="*60)
    print("🚀 Example: Running Internal Link Check on README.md")
    print("="*60)
    
    # Run one example command
    run_command(
        f"python check_internal_links.py {readme_path} --format text",
        "Internal Link Check - README.md"
    )
    
    print("\n" + "="*60)
    print("🌐 Example: Running External Link Check on README.md")
    print("="*60)
    
    # Run external link check with shorter timeout for demo
    run_command(
        f"python check_external_links.py {readme_path} --timeout 5",
        "External Link Check - README.md (5s timeout)"
    )
    
    print("\n" + "="*60)
    print("📝 VSCode Copilot Integration Tips")
    print("="*60)
    
    integration_tips = [
        "1. Use JSON format for programmatic processing:",
        "   python check_internal_links.py file.md --format json",
        "",
        "2. Save reports to files for later analysis:",
        "   python check_external_links.py guides/ --format markdown --output report.md",
        "",
        "3. Check specific directories:",
        "   python check_internal_links.py guides/ tools/ reference/",
        "",
        "4. Use different timeouts for external checks:",
        "   python check_external_links.py --all --timeout 15",
        "",
        "5. Combine with other tools:",
        "   python check_internal_links.py file.md --format json | jq '.issues[]'",
        "",
        "6. Create custom scripts:",
        "   # Check and fix in one command",
        "   python check_internal_links.py file.md --format json > issues.json",
        "   # Then process issues.json with custom fix script",
        "",
        "7. Integrate with CI/CD:",
        "   # Exit code 0 = no issues, 1 = issues found",
        "   python check_internal_links.py --all && echo 'All links OK!'",
        "",
        "8. Monitor specific file types:",
        "   find . -name '*.md' -exec python check_internal_links.py {} \\;",
    ]
    
    for tip in integration_tips:
        print(tip)
    
    print("\n" + "="*60)
    print("✅ Demo Complete!")
    print("="*60)
    print("\n🎯 Quick Reference:")
    print("- Internal links: python check_internal_links.py [files/dirs]")
    print("- External links: python check_external_links.py [files/dirs]")
    print("- Formats: --format text|json|markdown")
    print("- Output: --output filename")
    print("- Timeout: --timeout seconds (external links only)")
    print("\n📚 For more details, see README.md in this toolbox directory.")

if __name__ == "__main__":
    main()

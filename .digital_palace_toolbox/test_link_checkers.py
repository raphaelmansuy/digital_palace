#!/usr/bin/env python3
"""
Test script for Digital Palace Link Checkers

This script demonstrates how to use both link checkers and shows example output.
"""

import sys
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """Run a command and display its output"""
    print(f"\n{'='*60}")
    print(f"🔍 {description}")
    print(f"{'='*60}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ SUCCESS")
        else:
            print(f"❌ FAILED (exit code: {result.returncode})")
        
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏱️ TIMEOUT (30 seconds)")
        return False
    except Exception as e:
        print(f"💥 ERROR: {e}")
        return False

def main():
    print("🧰 Digital Palace Link Checker Test Suite")
    print("==========================================")
    
    # Get the toolbox directory
    toolbox_dir = Path(__file__).parent
    base_dir = toolbox_dir.parent
    
    # Test files
    test_files = [
        "README.md",
        "guides/mcp-servers.md"
    ]
    
    success_count = 0
    total_tests = 0
    
    # Test 1: Internal link checker on single file
    total_tests += 1
    if run_command([
        sys.executable, 
        str(toolbox_dir / "check_internal_links.py"),
        "README.md",
        "--format", "text"
    ], "Testing internal links in README.md"):
        success_count += 1
    
    # Test 2: Internal link checker with JSON output
    total_tests += 1
    if run_command([
        sys.executable,
        str(toolbox_dir / "check_internal_links.py"), 
        "guides/mcp-servers.md",
        "--format", "json"
    ], "Testing internal links in MCP guide (JSON output)"):
        success_count += 1
    
    # Test 3: External link checker on single file
    total_tests += 1
    if run_command([
        sys.executable,
        str(toolbox_dir / "check_external_links.py"),
        "README.md", 
        "--format", "text",
        "--timeout", "5"
    ], "Testing external links in README.md"):
        success_count += 1
    
    # Test 4: External link checker with markdown output
    total_tests += 1
    if run_command([
        sys.executable,
        str(toolbox_dir / "check_external_links.py"),
        "guides/mcp-servers.md",
        "--format", "markdown",
        "--timeout", "5"
    ], "Testing external links in MCP guide (Markdown output)"):
        success_count += 1
    
    # Test 5: Check help output
    total_tests += 1
    if run_command([
        sys.executable,
        str(toolbox_dir / "check_internal_links.py"),
        "--help"
    ], "Testing internal link checker help"):
        success_count += 1
    
    total_tests += 1
    if run_command([
        sys.executable,
        str(toolbox_dir / "check_external_links.py"),
        "--help" 
    ], "Testing external link checker help"):
        success_count += 1
    
    # Summary
    print(f"\n{'='*60}")
    print(f"📊 TEST SUMMARY")
    print(f"{'='*60}")
    print(f"✅ Passed: {success_count}")
    print(f"❌ Failed: {total_tests - success_count}")
    print(f"📈 Success Rate: {success_count/total_tests*100:.1f}%")
    
    if success_count == total_tests:
        print("\n🎉 All tests passed! The link checkers are working correctly.")
        return 0
    else:
        print(f"\n⚠️  {total_tests - success_count} test(s) failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Installation verification and dependency checker for Digital Palace Toolbox
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is sufficient"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_package(package_name):
    """Check if a Python package is installed"""
    try:
        # Handle special cases for package imports
        if package_name == 'python-docx':
            import docx
        elif package_name == 'Pillow':
            import PIL
        elif package_name == 'Pygments':
            import pygments
        else:
            __import__(package_name.replace('-', '_'))
        print(f"✅ {package_name}")
        return True
    except ImportError:
        print(f"❌ {package_name} - Run: pip install {package_name}")
        return False

def check_requirements_file(requirements_file):
    """Check all packages in a requirements file"""
    print(f"\n📋 Checking {requirements_file}:")
    
    if not Path(requirements_file).exists():
        print(f"❌ Requirements file not found: {requirements_file}")
        return False
    
    with open(requirements_file, 'r') as f:
        packages = [line.strip().split('>=')[0].split('==')[0] 
                   for line in f.readlines() 
                   if line.strip() and not line.startswith('#')]
    
    all_good = True
    for package in packages:
        if not check_package(package):
            all_good = False
    
    return all_good

def install_missing_packages(requirements_file):
    """Install missing packages from requirements file"""
    print(f"\n🔧 Installing packages from {requirements_file}...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', requirements_file], 
                      check=True)
        print("✅ Installation completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        return False

def main():
    """Main verification function"""
    print("🧰 Digital Palace Toolbox - Installation Verification\n")
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Check markdown_to_docx tool
    md_to_docx_path = Path("markdown_to_docx")
    if md_to_docx_path.exists():
        print(f"\n📝 Markdown to DOCX Converter:")
        requirements_file = md_to_docx_path / "requirements.txt"
        
        if check_requirements_file(str(requirements_file)):
            print("✅ All dependencies installed")
            
            # Test the converter
            print("\n🧪 Testing converter...")
            try:
                sys.path.insert(0, str(md_to_docx_path))
                from markdown_to_docx_converter import MarkdownToDocxConverter
                print("✅ Converter module loads successfully")
            except ImportError as e:
                print(f"❌ Converter test failed: {e}")
                return 1
        else:
            print("❌ Missing dependencies")
            response = input("\n🤔 Install missing packages? (y/N): ")
            if response.lower() == 'y':
                if install_missing_packages(str(requirements_file)):
                    print("✅ Please run the verification again")
                return 1
    else:
        print("❌ Markdown to DOCX tool not found")
        return 1
    
    print("\n🎉 All tools are ready to use!")
    print("\n📖 Next steps:")
    print("   • cd markdown_to_docx")
    print("   • python example_usage.py")
    print("   • python markdown_to_docx_converter.py input.md output.docx")
    
    return 0

if __name__ == "__main__":
    exit(main())

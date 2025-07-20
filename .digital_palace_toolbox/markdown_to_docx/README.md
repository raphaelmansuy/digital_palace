# 📝 Markdown to DOCX Converter with Code Block Images

A powerful Python tool that converts Markdown files to Microsoft Word DOCX documents, with special handling for code blocks which are converted to syntax-highlighted PNG images.

## 🌟 Features

- ✅ **Full Markdown Support**: Headers, lists, bold, italic, inline code
- 🎨 **Syntax Highlighting**: Code blocks converted to beautiful PNG images
- 📝 **Professional Formatting**: Proper DOCX styles and layout
- 🔧 **Configurable**: Easy to modify and extend
- 🚀 **Simple Usage**: Command-line interface and programmatic API
- 🎯 **High Quality**: Preserves formatting and creates publication-ready documents

## 📁 Directory Structure

```
.digital_palace_toolbox/
└── markdown_to_docx/
    ├── markdown_to_docx_converter.py  # Main converter script
    ├── requirements.txt               # Python dependencies
    ├── example_usage.py              # Example usage script
    └── README.md                     # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd .digital_palace_toolbox/markdown_to_docx
pip install -r requirements.txt
```

Or install manually:
```bash
pip install python-docx Pillow Pygments
```

### 2. Basic Usage

Convert a markdown file to DOCX:
```bash
python markdown_to_docx_converter.py input.md output.docx
```

### 3. Run the Example

```bash
# Convert the AI collaboration post (default example)
python example_usage.py

# Convert any custom file
python example_usage.py path/to/your/file.md output.docx
```

## 💡 Usage Examples

### Command Line

```bash
# Basic conversion
python markdown_to_docx_converter.py README.md README.docx

# Convert the AI collaboration post
python markdown_to_docx_converter.py \
  ../../personal/elitizon_linkedin/post_02_95_percent_fail_ai_collaboration.md \
  ../../tmp/ai_collaboration_post.docx

# Verbose output
python markdown_to_docx_converter.py input.md output.docx --verbose
```

### Programmatic Usage

```python
from markdown_to_docx_converter import MarkdownToDocxConverter

# Simple conversion
converter = MarkdownToDocxConverter("input.md", "output.docx")
converter.convert()

# Batch conversion
files_to_convert = [
    ("file1.md", "file1.docx"),
    ("file2.md", "file2.docx"),
]

for input_file, output_file in files_to_convert:
    converter = MarkdownToDocxConverter(input_file, output_file)
    converter.convert()
```

## 🎨 Code Block Conversion

Code blocks are automatically detected and converted to PNG images with:

- ✨ **Syntax highlighting** based on language specification
- 🎨 **Professional color scheme** (default Pygments style)
- 📏 **Proper spacing and padding**
- 🔤 **Monospace font** (Consolas/Monaco)
- 🖼️ **Centered alignment** in document
- 🛡️ **Fallback handling** for unsupported languages

### Supported Languages

The script supports syntax highlighting for all languages supported by Pygments:

- **Popular Languages**: Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust
- **Web Technologies**: HTML, CSS, JSON, XML, YAML
- **Databases**: SQL, PostgreSQL, MySQL
- **Scripting**: Shell/Bash, PowerShell, Batch
- **Data**: CSV, INI, TOML
- **And 500+ more languages...**

### Code Block Examples

**Input Markdown:**
````markdown
```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n"""
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
print(fibonacci(100))
```
````

**Output**: Beautiful syntax-highlighted image in your DOCX file! 🎨

## 📋 Supported Markdown Elements

| Element | Markdown | DOCX Output |
|---------|----------|-------------|
| **Headers** | `# H1`, `## H2`, `### H3` | Word heading styles |
| **Bold** | `**bold text**` | Bold formatting |
| **Italic** | `*italic text*` | Italic formatting |
| **Inline Code** | `` `code` `` | Monospace font |
| **Code Blocks** | ````python code ``` | Syntax-highlighted images |
| **Bullet Lists** | `- item` | Word bullet lists |
| **Numbered Lists** | `1. item` | Word numbered lists |
| **Horizontal Rules** | `---` | Document breaks |

## ⚙️ Configuration

### Customize Image Appearance

Edit the `_create_code_image` method to modify:

```python
formatter = ImageFormatter(
    font_name='Consolas',        # Font family
    font_size=12,               # Font size
    line_numbers=False,         # Show line numbers
    style='default',            # Color scheme
    line_pad=5,                 # Line spacing
    left_pad=10,                # Left padding
    right_pad=10                # Right padding
)
```

### Available Color Schemes

- `default` - Standard highlighting
- `monokai` - Dark theme
- `github` - GitHub-style
- `vs` - Visual Studio
- `colorful` - High contrast
- And many more...

### Custom Document Styles

Modify the `_setup_styles` method:

```python
def _setup_styles(self):
    styles = self.document.styles
    
    # Create custom styles
    code_style = styles.add_style('CodeChar', WD_STYLE_TYPE.CHARACTER)
    code_style.font.name = 'Source Code Pro'  # Custom font
    code_style.font.size = Pt(11)             # Custom size
```

## 🔧 Advanced Features

### Custom Image Size

Modify image dimensions in `_create_simple_text_image`:

```python
# Estimate image dimensions
char_width = 10      # Wider characters
char_height = 18     # Taller lines
padding = 30         # More padding
```

### Error Handling

The script includes comprehensive error handling:

- **Missing dependencies**: Clear installation instructions
- **Invalid markdown**: Graceful fallbacks
- **Font issues**: Automatic fallback fonts
- **Image generation failures**: Text-based fallbacks
- **File permissions**: Clear error messages

### Batch Processing

Create a batch processing script:

```python
import os
from pathlib import Path
from markdown_to_docx_converter import MarkdownToDocxConverter

def batch_convert(input_dir, output_dir):
    """Convert all markdown files in a directory"""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for md_file in input_path.glob("*.md"):
        output_file = output_path / f"{md_file.stem}.docx"
        converter = MarkdownToDocxConverter(str(md_file), str(output_file))
        converter.convert()
        print(f"✅ Converted: {md_file.name}")

# Usage
batch_convert("../../concepts", "../../tmp/docx_output")
```

## 🛠️ Troubleshooting

### Common Issues

1. **"python-docx not installed"**
   ```bash
   pip install python-docx
   ```

2. **"Pillow not installed"**
   ```bash
   pip install Pillow
   ```

3. **Font warnings**
   - Install Consolas or Monaco fonts
   - Or modify the font fallback in the code

4. **Large images**
   - Reduce font size in `ImageFormatter`
   - Modify image dimensions calculation

5. **Memory issues with large files**
   - Process files in smaller chunks
   - Reduce image quality/size

### Debug Mode

Enable verbose output for troubleshooting:

```bash
python markdown_to_docx_converter.py input.md output.docx --verbose
```

## 📊 Performance

**Typical Performance:**
- Small files (< 10KB): < 1 second
- Medium files (10-100KB): 1-5 seconds  
- Large files (100KB-1MB): 5-15 seconds
- Very large files (> 1MB): 15+ seconds

**Optimization Tips:**
- Minimize large code blocks
- Use appropriate image quality settings
- Process files individually for large batches

## 🎯 Use Cases

### Perfect For:

- **Technical Documentation** - Convert README files to Word docs
- **Blog Posts** - Professional formatting for publishing
- **Academic Papers** - Code examples as images
- **Reports** - Technical reports with code snippets
- **Presentations** - Convert markdown notes to Word
- **Portfolio** - Technical writing samples

### Real-World Examples:

1. **AI Collaboration Post** (your example)
   - Headers, lists, code blocks
   - Professional business formatting
   - Ready for publication

2. **Technical Documentation**
   - API documentation with code examples
   - Installation guides with shell commands
   - Configuration files as highlighted blocks

3. **Educational Content**
   - Programming tutorials
   - Code explanations with examples
   - Step-by-step guides

## 🔮 Future Enhancements

Potential improvements:
- [ ] Table support
- [ ] Image embedding
- [ ] Link preservation
- [ ] Math equation support
- [ ] Custom CSS styling
- [ ] Multi-column layouts
- [ ] TOC generation
- [ ] Footnotes support

## 📄 License

This tool is part of the Digital Palace toolbox and can be freely modified and extended for your needs.

## 🤝 Contributing

Feel free to enhance the script by:
- Adding support for more markdown elements
- Improving image generation quality
- Adding configuration options
- Optimizing performance
- Creating additional export formats

---

**Ready to convert your markdown files to professional DOCX documents?** 🚀

Try it with your AI collaboration post:
```bash
python example_usage.py
```

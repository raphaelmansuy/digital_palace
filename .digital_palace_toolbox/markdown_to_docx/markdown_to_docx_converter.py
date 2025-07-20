#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "python-docx",
#     "Pillow",
#     "Pygments"
# ]
# ///
"""
Markdown to DOCX Converter with Code Block to PNG Conversion

This script converts a markdown file to a DOCX document, converting all code blocks
to high-quality PNG images with syntax highlighting (300 DPI for crisp text).

This is a self-installing Python script using UV. No manual dependency installation required!

Usage:
    chmod +x markdown_to_docx_converter.py
    
    # Convert with auto-generated output in ./tmp directory
    ./markdown_to_docx_converter.py input.md
    
    # Convert with specific output file
    ./markdown_to_docx_converter.py input.md output.docx
    
    # Convert with custom output directory
    ./markdown_to_docx_converter.py input.md --output-dir /path/to/output
    
    # Traditional way
    uv run markdown_to_docx_converter.py input.md
"""

import argparse
import os
import re
import tempfile
from pathlib import Path
from typing import List, Tuple, Dict, Any

# Required imports - UV handles these dependencies automatically
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.shared import OxmlElement, qn
from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from pygments.util import ClassNotFound
from pygments.lexers.special import TextLexer


class MarkdownToDocxConverter:
    def __init__(self, input_file: str, output_file: str, style: str = 'default'):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.style = style
        
        # Create image directory alongside the output file
        output_path = Path(output_file)
        self.image_dir = output_path.parent
        self.base_name = output_path.stem  # filename without extension
        
        self.temp_dir = tempfile.mkdtemp(prefix="md2docx_")  # Keep for temp files
        self.image_counter = 0
        self.document = Document()
        self._setup_styles()
    
    def _setup_styles(self):
        """Setup custom styles for the document"""
        styles = self.document.styles
        
        # Create a code style for inline code
        try:
            code_style = styles.add_style('CodeChar', WD_STYLE_TYPE.CHARACTER)
            code_style.font.name = 'Consolas'
            code_style.font.size = Pt(10)
        except Exception:
            pass  # Style might already exist
    
    def _extract_code_blocks(self, content: str) -> Tuple[str, List[Dict[str, Any]]]:
        """Extract code blocks from markdown content and replace with placeholders"""
        code_blocks = []
        placeholder_pattern = "{{{{CODE_BLOCK_{}}}}}"  # Double braces to escape them in format()
        
        # Improved pattern to match fenced code blocks with more flexibility
        # Handles: languages with hyphens, optional newlines, various edge cases
        code_block_pattern = r'```([a-zA-Z0-9_+-]*)\n?(.*?)\n?```'
        
        def replace_code_block(match):
            language = match.group(1) if match.group(1) else 'text'
            code_content = match.group(2)
            
            block_info = {
                'language': language,
                'content': code_content,
                'index': len(code_blocks)
            }
            code_blocks.append(block_info)
            
            return placeholder_pattern.format(len(code_blocks) - 1)
        
        # Replace code blocks with placeholders
        modified_content = re.sub(code_block_pattern, replace_code_block, content, flags=re.DOTALL)
        
        return modified_content, code_blocks
    
    def _create_code_image(self, code: str, language: str = 'text') -> str:
        """Create a high-quality PNG image from code block (300 DPI)"""
        self.image_counter += 1
        # Use persistent naming: outputfile_image001.png
        image_filename = f"{self.base_name}_image{self.image_counter:03d}.png"
        image_path = str(self.image_dir / image_filename)
        
        # Choose styling based on user preference
        if self.style == 'codesnap':
            return self._create_codesnap_image(code, language, image_path)
        else:
            return self._create_default_image(code, language, image_path)
    
    def _create_default_image(self, code: str, language: str, image_path: str) -> str:
        """Create default style syntax highlighted image"""
        try:
            # Get lexer for the specified language
            if language and language.lower() != 'text':
                try:
                    lexer = get_lexer_by_name(language, stripall=True)
                except ClassNotFound:
                    lexer = TextLexer()
            else:
                lexer = TextLexer()
            
            # Configure the image formatter with high-quality settings
            # Scale up for higher resolution (300 DPI equivalent)
            scale_factor = 3  # 3x scale for crisp text
            formatter = ImageFormatter(
                font_name='Monaco',
                font_size=14 * scale_factor,  # Larger font for scaling
                line_numbers=False,
                style='colorful',
                line_pad=10 * scale_factor,
                left_pad=20 * scale_factor,
                right_pad=20 * scale_factor
            )
            
            # Generate the image
            result = highlight(code, lexer, formatter)
            
            # Save the image with high DPI metadata
            with open(image_path, 'wb') as f:
                f.write(result)
            
            # Post-process to add DPI metadata for better quality
            try:
                from PIL import Image as PILImage
                img = PILImage.open(image_path)
                # Resave with DPI metadata
                img.save(image_path, dpi=(300, 300), quality=100)
            except Exception:
                pass  # If post-processing fails, keep original
            
            return image_path
            
        except Exception as e:
            print(f"Warning: Failed to create syntax-highlighted image for {language}: {e}")
            # Fallback: create a simple text image
            return self._create_simple_text_image(code, image_path)
    
    def _create_codesnap_image(self, code: str, language: str, image_path: str) -> str:
        """Create CodeSnap style image with macOS window frame"""
        try:
            from PIL import Image as PILImage, ImageDraw, ImageFont
            
            # Get lexer for syntax highlighting
            if language and language.lower() != 'text':
                try:
                    lexer = get_lexer_by_name(language, stripall=True)
                except ClassNotFound:
                    lexer = TextLexer()
            else:
                lexer = TextLexer()
            
            # Settings for high DPI
            scale = 3
            window_border = 8 * scale
            title_bar_height = 32 * scale
            dot_size = 8 * scale
            dot_spacing = 20 * scale
            content_padding = 20 * scale
            font_size = 14 * scale
            line_height = 20 * scale
            
            # Window colors (dark theme)
            window_bg = (40, 44, 52)      # Dark gray
            title_bar_bg = (60, 63, 65)   # Slightly lighter gray
            content_bg = (40, 44, 52)     # Same as window
            text_color = (220, 220, 220)  # Light gray
            dot_colors = [
                (255, 95, 87),   # Red
                (255, 189, 46),  # Yellow  
                (39, 201, 63)    # Green
            ]
            
            # Calculate text dimensions
            lines = code.split('\n')
            max_line_length = max(len(line.expandtabs(4)) for line in lines) if lines else 50
            
            # Try to load Monaco font, fallback to default monospace
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", font_size)
            except Exception:
                try:
                    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttf", font_size)
                except Exception:
                    font = ImageFont.load_default()
            
            # Calculate image dimensions
            content_width = max_line_length * (font_size // 2) + 2 * content_padding
            content_height = len(lines) * line_height + 2 * content_padding
            
            total_width = content_width + 2 * window_border
            total_height = content_height + title_bar_height + 2 * window_border
            
            # Create image
            img = PILImage.new('RGB', (total_width, total_height), window_bg)
            draw = ImageDraw.Draw(img)
            
            # Draw title bar
            draw.rectangle([
                window_border, 
                window_border, 
                total_width - window_border, 
                window_border + title_bar_height
            ], fill=title_bar_bg)
            
            # Draw window dots (traffic lights)
            dot_y = window_border + title_bar_height // 2
            dot_start_x = window_border + dot_spacing
            
            for i, color in enumerate(dot_colors):
                dot_x = dot_start_x + i * dot_spacing
                draw.ellipse([
                    dot_x - dot_size//2, 
                    dot_y - dot_size//2,
                    dot_x + dot_size//2, 
                    dot_y + dot_size//2
                ], fill=color)
            
            # Draw content area
            content_y_start = window_border + title_bar_height
            draw.rectangle([
                window_border,
                content_y_start,
                total_width - window_border,
                total_height - window_border
            ], fill=content_bg)
            
            # Draw code with simple syntax highlighting (basic approach)
            y_pos = content_y_start + content_padding
            for line in lines:
                # Basic syntax highlighting colors
                line_color = text_color
                if line.strip().startswith('#'):  # Comments
                    line_color = (128, 128, 128)
                elif any(keyword in line for keyword in ['def ', 'class ', 'import ', 'from ']):  # Keywords
                    line_color = (255, 123, 114)
                elif '"' in line or "'" in line:  # Strings (simple detection)
                    line_color = (152, 195, 121)
                
                draw.text(
                    (window_border + content_padding, y_pos),
                    line.expandtabs(4),
                    fill=line_color,
                    font=font
                )
                y_pos += line_height
            
            # Save with high DPI
            img.save(image_path, dpi=(300, 300), quality=100)
            return image_path
            
        except Exception as e:
            print(f"Warning: Failed to create CodeSnap image for {language}: {e}")
            # Fallback to default style
            return self._create_default_image(code, language, image_path)
    
    def _create_simple_text_image(self, code: str, image_path: str) -> str:
        """Create a simple text image as fallback with high DPI"""
        try:
            # Calculate image size based on text with high DPI scaling
            lines = code.split('\n')
            max_line_length = max(len(line) for line in lines) if lines else 50
            
            # High DPI settings (300 DPI equivalent)
            dpi_scale = 4  # 4x scale for 300 DPI quality
            char_width = 9 * dpi_scale
            char_height = 18 * dpi_scale
            padding = 25 * dpi_scale
            
            width = max(500 * dpi_scale, max_line_length * char_width + padding * 2)
            height = max(120 * dpi_scale, len(lines) * char_height + padding * 2)
            
            # Create high-resolution image
            img = Image.new('RGB', (width, height), color='white')
            draw = ImageDraw.Draw(img)
            
            # Try to use a high-quality monospace font
            font_size = 16 * dpi_scale
            try:
                font = ImageFont.truetype('/System/Library/Fonts/Monaco.ttc', font_size)
            except Exception:
                try:
                    font = ImageFont.truetype('Monaco', font_size)
                except Exception:
                    try:
                        font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', font_size)
                    except Exception:
                        # Use default but scale it
                        font = ImageFont.load_default()
            
            # Draw text with high quality
            y_offset = padding
            for line in lines:
                draw.text((padding, y_offset), line, fill='black', font=font)
                y_offset += char_height
            
            # Add border
            border_width = 2 * dpi_scale
            draw.rectangle([0, 0, width-border_width, height-border_width], 
                         outline='gray', width=border_width)
            
            # Save with high DPI metadata (300 DPI)
            img.save(image_path, dpi=(300, 300), quality=100)
            return image_path
            
        except Exception as e:
            print(f"Error creating fallback image: {e}")
            return None
    
    def _process_markdown_element(self, line: str):
        """Process different markdown elements"""
        line = line.strip()
        
        if not line:
            # Empty line
            self.document.add_paragraph()
            return
        
        # Check for code block placeholder
        placeholder_match = re.match(r'\{\{CODE_BLOCK_(\d+)\}\}', line)
        if placeholder_match:
            # This will be handled separately
            return
        
        # Headers
        if line.startswith('#'):
            level = 0
            while level < len(line) and line[level] == '#':
                level += 1
            
            if level <= 6:
                header_text = line[level:].strip()
                if level == 1:
                    heading = self.document.add_heading(header_text, level=1)
                elif level == 2:
                    heading = self.document.add_heading(header_text, level=2)
                elif level == 3:
                    heading = self.document.add_heading(header_text, level=3)
                else:
                    heading = self.document.add_heading(header_text, level=4)
                
                # Ensure heading text is black
                for run in heading.runs:
                    run.font.color.rgb = RGBColor(0, 0, 0)  # Black color
                return
        
        # Horizontal rule
        if line.strip() == '---':
            # Add spacing before the horizontal rule
            self.document.add_paragraph()
            # Create a proper horizontal line using a paragraph with bottom border
            p = self.document.add_paragraph()
            p_format = p.paragraph_format
            p_format.space_before = Pt(12)
            p_format.space_after = Pt(12)
            # Get the paragraph format
            pPr = p._element.get_or_add_pPr()
            # Create border element
            pBdr = OxmlElement('w:pBdr')
            # Add bottom border
            bottom = OxmlElement('w:bottom')
            bottom.set(qn('w:val'), 'single')
            bottom.set(qn('w:sz'), '24')  # Thicker border size
            bottom.set(qn('w:space'), '4')
            bottom.set(qn('w:color'), '000000')  # Black color
            pBdr.append(bottom)
            pPr.append(pBdr)
            # Add spacing after the horizontal rule
            self.document.add_paragraph()
            return
        
        # Lists
        if re.match(r'^[\s]*[-\*\+]\s+', line):
            # Bullet list
            text = re.sub(r'^[\s]*[-\*\+]\s+', '', line)
            p = self.document.add_paragraph(text, style='List Bullet')
            self._apply_text_formatting(p, text)
            return
        
        if re.match(r'^[\s]*\d+\.\s+', line):
            # Numbered list
            text = re.sub(r'^[\s]*\d+\.\s+', '', line)
            p = self.document.add_paragraph(text, style='List Number')
            self._apply_text_formatting(p, text)
            return
        
        # Regular paragraph
        p = self.document.add_paragraph()
        self._apply_text_formatting(p, line)
    
    def _apply_text_formatting(self, paragraph, text: str):
        """Apply bold, italic, and inline code formatting"""
        # Clear existing text
        paragraph.clear()
        
        # Improved pattern to match formatting - order matters!
        # 1. **bold** (must come before *italic* to avoid conflicts)
        # 2. *italic* 
        # 3. `code`
        # Using non-greedy matching and proper escaping
        pattern = r'(\*\*[^*]+?\*\*|\*[^*]+?\*|`[^`]+?`)'
        parts = re.split(pattern, text)
        
        for part in parts:
            if not part:
                continue
                
            if part.startswith('**') and part.endswith('**') and len(part) > 4:
                # Bold text - ensure it's actually bold formatting
                content = part[2:-2]
                run = paragraph.add_run(content)
                run.bold = True
            elif part.startswith('*') and part.endswith('*') and len(part) > 2 and not part.startswith('**'):
                # Italic text - ensure it's not bold and has content
                content = part[1:-1]
                run = paragraph.add_run(content)
                run.italic = True
            elif part.startswith('`') and part.endswith('`') and len(part) > 2:
                # Inline code - ensure it has content
                content = part[1:-1]
                run = paragraph.add_run(content)
                try:
                    run.style = 'CodeChar'
                except Exception:
                    run.font.name = 'Consolas'
                    run.font.size = Pt(10)
            else:
                # Regular text
                paragraph.add_run(part)
    
    def convert(self):
        """Convert the markdown file to DOCX"""
        try:
            # Read the markdown file
            with open(self.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract code blocks
            modified_content, code_blocks = self._extract_code_blocks(content)
            
            # Create images for code blocks
            code_images = {}
            for i, block in enumerate(code_blocks):
                image_path = self._create_code_image(block['content'], block['language'])
                if image_path:
                    code_images[i] = image_path
            
            # Process markdown content line by line
            lines = modified_content.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i]
                
                # Check for code block placeholder
                placeholder_match = re.match(r'\{\{CODE_BLOCK_(\d+)\}\}', line.strip())
                if placeholder_match:
                    block_index = int(placeholder_match.group(1))
                    if block_index in code_images:
                        # Add the code block image
                        paragraph = self.document.add_paragraph()
                        run = paragraph.add_run()
                        try:
                            run.add_picture(code_images[block_index], width=Inches(6))
                            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        except Exception as e:
                            print(f"Warning: Could not add image for code block {block_index}: {e}")
                            # Fallback: add as text
                            self.document.add_paragraph(f"[Code Block - {code_blocks[block_index]['language']}]")
                            self.document.add_paragraph(code_blocks[block_index]['content'])
                else:
                    self._process_markdown_element(line)
                
                i += 1
            
            # Save the document
            self.document.save(self.output_file)
            print(f"Successfully converted {self.input_file} to {self.output_file}")
            if self.image_counter > 0:
                print(f"Generated {self.image_counter} code block images: {self.base_name}_image001.png to {self.base_name}_image{self.image_counter:03d}.png")
            
        except Exception as e:
            print(f"Error during conversion: {e}")
            raise
        finally:
            # Cleanup temporary files
            self._cleanup()
    
    def _cleanup(self):
        """Clean up temporary files"""
        try:
            import shutil
            shutil.rmtree(self.temp_dir)
        except Exception as e:
            print(f"Warning: Could not clean up temporary directory: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown to DOCX with code blocks as images'
    )
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('output', nargs='?', default=None, help='Output DOCX file (optional if --output-dir is used)')
    parser.add_argument('--output-dir', '-o', 
                       help='Output directory (defaults to ./tmp relative to input file)')
    parser.add_argument('--style', choices=['default', 'codesnap'], default='codesnap',
                       help='Code block image style: default or codesnap (macOS window style)')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Verbose output')
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' does not exist")
        return 1
    
    # Determine output file path
    input_path = Path(args.input)
    
    if args.output:
        # If output file is explicitly provided, use it
        output_file = args.output
        output_dir = os.path.dirname(output_file)
    elif args.output_dir:
        # If output-dir is provided, use it for output location
        output_dir = args.output_dir
        output_filename = input_path.stem + '.docx'
        output_file = os.path.join(output_dir, output_filename)
    else:
        # Default: output file is input filename with .docx extension in same directory
        output_file = str(input_path.with_suffix('.docx'))
        output_dir = input_path.parent
    
    # Create output directory if it doesn't exist
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        if args.verbose:
            print(f"Created output directory: {output_dir}")
    
    if args.verbose:
        print(f"Converting: {args.input} -> {output_file}")
    
    # Convert the file
    try:
        converter = MarkdownToDocxConverter(args.input, output_file, args.style)
        converter.convert()
        return 0
    except Exception as e:
        print(f"Conversion failed: {e}")
        return 1


if __name__ == '__main__':
    # This script is now self-installing thanks to UV!
    # Usage examples:
    # ./markdown_to_docx_converter.py input.md                    # -> input_dir/tmp/input.docx
    # ./markdown_to_docx_converter.py input.md output.docx        # -> output.docx
    # ./markdown_to_docx_converter.py input.md -o /custom/dir     # -> /custom/dir/input.docx
    # UV will automatically handle all dependency installation and environment setup
    exit(main())

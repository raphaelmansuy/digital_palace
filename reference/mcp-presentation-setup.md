# MCP Server Presentation Setup

## Using the Marp Presentation

The file `mcp-server-presentation.md` is a complete Marp presentation about MCP servers.

### Prerequisites

1. **Install Marp CLI** (if you want to export):
   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. **Or use Marp for VS Code Extension**:
   - Install the "Marp for VS Code" extension
   - Open the presentation file
   - Use the preview feature

### Usage Options

#### Option 1: VS Code Extension (Recommended)
1. Install "Marp for VS Code" extension
2. Open `mcp-server-presentation.md`
3. Click the Marp preview button or use `Ctrl+Shift+P` → "Marp: Open Preview"
4. Present directly from VS Code

#### Option 2: Export to HTML/PDF
```bash
# Export to HTML (interactive)
marp mcp-server-presentation.md --html

# Export to PDF
marp mcp-server-presentation.md --pdf

# Export to PowerPoint
marp mcp-server-presentation.md --pptx
```

#### Option 3: Live Server
```bash
# Start a live server for presentation
marp -s mcp-server-presentation.md
```

### Presentation Features

- **17 slides** covering MCP servers comprehensively
- **Professional styling** with pastel colors and good contrast
- **Interactive diagrams** using Mermaid
- **Responsive layout** with columns and grids
- **Smooth transitions** between slides

### Slide Navigation
- **Arrow keys** or **click** to navigate
- **F** for fullscreen
- **Escape** to exit fullscreen
- **P** for presenter mode (if supported)

### Customization

The presentation uses:
- Custom CSS styling for professional appearance
- Mermaid diagrams (may need internet connection for rendering)
- Grid layouts for better content organization
- Highlight boxes for important information

Enjoy your presentation! 🎯

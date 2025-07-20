

# TIL: How to Create Script-Based Commands in Raycast (2024-03-18)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Automate Mac workflows with custom Raycast scripts** – Create script commands in any language to trigger automations, control your Mac, and boost productivity directly from Raycast.

---

## The Pain Point

Repetitive tasks like toggling settings, triggering deployments, or running complex workflows require switching between apps and remembering commands. Raycast script commands eliminate this friction.

---

## Step-by-Step Guide

### 1. Write Your Script

Create a script in any language (Bash, Python, AppleScript, Swift):

```bash
#!/bin/bash
echo "Hello, World!"
```

Make it executable:

```bash
chmod +x your-script.sh
```

### 2. Add Metadata Block

Add Raycast metadata at the top of your script:

```bash
#!/bin/bash
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Hello World
# @raycast.mode fullOutput
# Optional parameters:
# @raycast.icon 🤖
# @raycast.author Your Name
# @raycast.description Prints Hello World

echo "Hello, World!"
```

### 3. Save and Organize

Place your scripts in a dedicated folder:

```bash
mkdir ~/raycast-scripts
mv your-script.sh ~/raycast-scripts/
```

### 4. Add Script Directory to Raycast

- Open Raycast → Preferences → Extensions → Script Commands
- Click "Add Script Directory"
- Select your `~/raycast-scripts/` folder

### 5. Run Your Command

- Open Raycast (⌘ + Space)
- Type your script's title
- Press Enter to execute

## Troubleshooting

### Script Not Appearing in Raycast

- Verify the script file has executable permissions: `chmod +x your-script.sh`
- Check the metadata block syntax (no typos in `@raycast.` fields)
- Ensure the script directory is properly added to Raycast preferences

### Script Execution Errors

- Test the script directly in Terminal first
- Use `shellcheck` to validate Bash scripts for common errors
- Check that all required dependencies are installed and in PATH

### Permission Issues

- Scripts may need full disk access permissions for certain operations
- Grant necessary permissions in System Preferences → Security & Privacy

## Related Resources

- [Raycast Script Commands Repository](https://github.com/raycast/script-commands) - Community collection of scripts
- [Raycast Manual: Script Commands](https://manual.raycast.com/script-commands) - Official documentation
- [Script Command Templates](https://github.com/raycast/script-commands/tree/master/templates) - Ready-to-use templates
- [ShellCheck](https://www.shellcheck.net/) - Bash script linting tool


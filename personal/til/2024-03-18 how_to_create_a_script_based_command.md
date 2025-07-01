

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

# 🚀 How to Create a Script-Based Command in Raycast

> **Raycast Script Commands** let you trigger custom scripts from anywhere on your Mac, boosting productivity for repetitive or complex tasks.

---

## What Are Script Commands?

Script Commands are small scripts (Bash, Python, AppleScript, etc.) that you can run directly from Raycast. They are perfect for:
- Automating daily workflows
- Controlling your Mac (e.g., toggling hidden files)
- Triggering dev tasks (e.g., git actions, deployments)
- Integrating with APIs or home automation

---

## Step-by-Step: Create Your Own Script Command

1. **Write Your Script**
   - Use Bash, Python, AppleScript, Swift, etc.
   - Make it executable (`chmod +x your-script.sh`).

2. **Add Metadata Block** (at the top of your script):
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

3. **Save the Script**
   - Place it in a folder (e.g., `~/raycast-scripts/`).

4. **Add Script Directory to Raycast**
   - Open Raycast → Preferences → Extensions → Script Commands → Add Script Directory → Select your folder.

5. **Run Your Command**
   - Open Raycast, type your script's title, and run it!

---

## Metadata Block Explained

The metadata block (comments starting with `# @raycast.`) configures how Raycast displays and runs your script. Key fields:
- `@raycast.schemaVersion` (required): Always set to 1.
- `@raycast.title` (required): Name shown in Raycast.
- `@raycast.mode` (required): `fullOutput`, `inline`, or `compact` (controls output display).
- `@raycast.icon`: Emoji, file path, or URL for icon.
- `@raycast.author`, `@raycast.description`: For documentation.

See [full metadata docs](https://github.com/raycast/script-commands#metadata).

---

## Best Practices

- **Use ShellCheck** to lint Bash scripts for errors.
- **Keep scripts simple and fast.**
- **Handle errors**: Exit with non-zero status and print a helpful message.
- **Use arguments** for flexible commands (see Raycast docs for details).
- **Add icons and descriptions** for clarity.

---

## Example: Bash Script Command

```bash
#!/bin/bash
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Show Date
# @raycast.mode inline
# Optional parameters:
# @raycast.icon 📅
# @raycast.author Jane Doe
# @raycast.description Shows the current date and time
date
```

---

## Resources

- [Raycast Script Commands Repo](https://github.com/raycast/script-commands)
- [Raycast Manual: Script Commands](https://manual.raycast.com/script-commands)
- [Script Command Templates](https://github.com/raycast/script-commands/tree/master/templates)

---

**Now you can automate anything on your Mac with just a script and Raycast!**


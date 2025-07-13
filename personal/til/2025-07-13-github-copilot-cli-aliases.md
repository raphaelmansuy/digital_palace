# TIL: GitHub Copilot CLI Aliases Setup (2025-07-13)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Quick CLI productivity boost** - Set up GitHub Copilot CLI aliases for faster command-line AI assistance

## The Pain Point

Typing `gh copilot suggest` and `gh copilot explain` repeatedly when you need AI help in the terminal gets tedious fast. The official GitHub Copilot CLI supports convenient aliases that reduce these to simple `ghcs` and `ghce` commands.

## What Are GitHub Copilot CLI Aliases?

GitHub Copilot CLI aliases allow you to:
- **`ghcs`** instead of `gh copilot suggest` - Get AI-powered command suggestions
- **`ghce`** instead of `gh copilot explain` - Get explanations for commands
- **Automatic execution** - Copilot can run commands directly with confirmation

Perfect for developers who live in the terminal and want AI assistance without breaking their flow.

---

## Quick Setup Guide

### Prerequisites

Ensure you have GitHub CLI and Copilot CLI installed:
```bash
# Install GitHub CLI (if not already installed)
brew install gh  # macOS
# or: winget install --id GitHub.cli  # Windows

# Install Copilot CLI extension
gh extension install github/gh-copilot
```

### Shell-Specific Setup

Choose your shell and run the appropriate command:

#### **Bash**
```bash
echo 'eval "$(gh copilot alias -- bash)"' >> ~/.bashrc
source ~/.bashrc
```

#### **Zsh** (macOS default)
```bash
echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc
source ~/.zshrc
```

#### **PowerShell** (Windows)
```powershell
$GH_COPILOT_PROFILE = Join-Path -Path $(Split-Path -Path $PROFILE -Parent) -ChildPath "gh-copilot.ps1"
gh copilot alias -- pwsh | Out-File ( New-Item -Path $GH_COPILOT_PROFILE -Force )
echo ". `"$GH_COPILOT_PROFILE`"" >> $PROFILE
```

---

## Real-World Usage Examples

### 1. Get Command Suggestions (`ghcs`)
```bash
# Instead of typing: gh copilot suggest
ghcs "find all Python files larger than 1MB"
# Returns: find . -name "*.py" -size +1M

ghcs "compress all log files from last week"
# Returns: find . -name "*.log" -mtime -7 -exec gzip {} \;

ghcs "show disk usage by directory, sorted"
# Returns: du -sh */ | sort -hr
```

### 2. Explain Complex Commands (`ghce`)
```bash
# Instead of typing: gh copilot explain
ghce "find . -type f -name '*.js' -exec grep -l 'useState' {} \;"
# Returns: Detailed explanation of the find command with grep

ghce "docker run -it --rm -v $(pwd):/app node:18-alpine sh"
# Returns: Breakdown of Docker command flags and options
```

### 3. Interactive Mode
```bash
# Start interactive session
ghcs
# Copilot will prompt you to describe what you want to do
# Then provide suggestions with options to execute directly
```

---

## Advanced Configuration

### Enable Auto-Execution (Use Carefully)

Configure default execution behavior:
```bash
gh copilot config
```

Options:
- **Default value for confirming command execution**: Choose "Always", "Never", or "Prompt"
- **Optional Usage Analytics**: Opt in/out of data collection

### Usage Analytics Control

Disable analytics if desired:
```bash
gh copilot config
# Select "Optional Usage Analytics" 
# Choose "No" to opt out
```

---

## Pro Tips for Terminal Productivity

### 1. Combine with Git Aliases
Use alongside efficient Git aliases (see [Git Aliases TIL](2024-07-27-git-alias.md)):
```bash
# Use ghcs to learn new Git patterns
ghcs "rebase interactive last 3 commits"
# Then create alias: alias gri="git rebase -i HEAD~3"
```

### 2. Learning Complex Tools
```bash
# Great for exploring new tools
ghcs "docker compose setup for Node.js app with Redis"
ghce "kubectl get pods --all-namespaces -o wide"
```

### 3. Quick System Administration
```bash
ghcs "monitor system resources continuously"
# Returns: top -d 1 or htop

ghcs "kill all processes using port 3000"
# Returns: lsof -ti:3000 | xargs kill -9
```

---

## Integration with VS Code

These CLI aliases work perfectly alongside VS Code Copilot:
- Use **CLI aliases** for terminal-based tasks
- Use **[VS Code Agent Mode](2025-01-09-vscode-agent-mode-standard-tools.md)** for code editing
- Use **[MCP servers](2025-01-09-vscode-mcp-server-configuration.md)** for enhanced AI capabilities

### Workflow Example
```bash
# 1. In terminal: Get deployment command suggestion
ghcs "deploy Next.js app to Vercel with environment variables"

# 2. In VS Code: Use Agent Mode to prepare deployment files
# 3. Back to terminal: Execute the suggested deployment command
```

---

## Troubleshooting

### Aliases Not Working?
```bash
# Check if aliases are properly set
which ghcs
# Should return: ghcs: aliased to gh copilot suggest

# Reload shell configuration
source ~/.zshrc  # or ~/.bashrc
```

### GitHub CLI Authentication
```bash
# Ensure you're logged in
gh auth status

# Login if needed
gh auth login
```

### Extension Issues
```bash
# Check installed extensions
gh extension list

# Reinstall if needed
gh extension remove github/gh-copilot
gh extension install github/gh-copilot
```

---

## Security Considerations

1. **Review Before Execution**: Always review suggested commands before running them
2. **Sensitive Operations**: Be cautious with commands involving passwords or sensitive data
3. **Auto-Execution**: Use auto-execution mode carefully, especially in production environments
4. **Analytics**: Consider privacy implications of usage analytics

---

## Related Resources

- **[Efficient Git Aliases](2024-07-27-git-alias.md)** → Terminal productivity with Git
- **[VS Code Agent Mode Tools](2025-01-09-vscode-agent-mode-standard-tools.md)** → AI assistance in VS Code
- **[MCP Server Configuration](2025-01-09-vscode-mcp-server-configuration.md)** → Enhanced AI capabilities
- **[Command Line Tools](../../tools/ai-tools-master-directory.md#command-line-tools)** → AI CLI tools directory

### External Links
- **[Official GitHub Copilot CLI Documentation](https://docs.github.com/en/copilot/how-tos/personal-settings/configuring-github-copilot-in-the-cli)** → Complete setup guide
- **[GitHub CLI](https://cli.github.com/)** → GitHub CLI installation and docs
- **[Copilot CLI Extension](https://github.com/github/gh-copilot)** → Extension repository

---

*⚡ Pro tip: Combine these aliases with [efficient Git aliases](2024-07-27-git-alias.md) for maximum terminal productivity!*

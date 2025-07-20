# TIL: Mirroring Bitbucket to GitHub Repository Synchronization (2024-09-13)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Sync Bitbucket and GitHub repos** – Create a complete mirror of a Bitbucket repository to GitHub, preserving branches, tags, commit history, and enabling ongoing synchronization.

---

## The Pain Point

Moving or synchronizing code between Bitbucket and GitHub can be challenging when you need to:

- Preserve complete commit history and all branches
- Maintain ongoing synchronization between repositories
- Transfer large repositories with multiple contributors
- Keep tags and metadata intact during migration
- Automate the sync process for continuous updates

Simple repository cloning often loses important metadata and doesn't maintain the connection for future updates.

---

## Summary

Mirroring a Bitbucket repository to GitHub with `git clone --mirror` ensures all branches, tags, and commit history are preserved. Ongoing sync can be automated with scripts, cron jobs, or CI/CD workflows. This guide covers setup, troubleshooting, and security best practices for seamless migration and continuous updates.

---

## Step-by-Step Guide

### 1. Create a Mirror Clone of Bitbucket Repository

```bash
# Create a complete mirror clone (includes all branches, tags, and history)
git clone --mirror https://bitbucket.org/username/repository-name.git

# Navigate to the cloned directory
cd repository-name.git
```

The `--mirror` flag ensures all refs (branches, tags, remotes) are copied exactly.

### 2. Create New GitHub Repository

```bash
# Using GitHub CLI (if available)
gh repo create username/repository-name --public --clone=false

# Or create manually via GitHub web interface
# - Go to github.com
# - Click "New repository"
# - Enter repository name
# - DO NOT initialize with README, .gitignore, or license
```

### 3. Configure Remote and Push Mirror

```bash
# Set GitHub as the push destination
git remote set-url --push origin https://github.com/username/repository-name.git

# Push the complete mirror to GitHub
git push --mirror

# Verify all branches and tags were transferred
git ls-remote origin
```

### 4. Set Up Ongoing Synchronization

```bash
# Create a sync script for regular updates
cat > sync-repos.sh << 'EOF'
#!/bin/bash
set -e

echo "Fetching updates from Bitbucket..."
git fetch -p origin

echo "Pushing updates to GitHub..."
git push --mirror

echo "Sync completed successfully!"
EOF

chmod +x sync-repos.sh
```

### 5. Automate with Cron (Optional)

```bash
# Add to crontab for daily sync at 2 AM
crontab -e

# Add this line:
# 0 2 * * * cd /path/to/repository-name.git && ./sync-repos.sh >> sync.log 2>&1
```

### 6. Advanced: Two-way Sync Setup

```bash
# For bidirectional sync, add Bitbucket as second remote
git remote add bitbucket https://bitbucket.org/username/repository-name.git
git remote add github https://github.com/username/repository-name.git

# Sync from Bitbucket to GitHub
git fetch bitbucket
git push github --mirror

# Sync from GitHub to Bitbucket (if needed)
git fetch github  
git push bitbucket --mirror
```

### 7. Using CI/CD for Automated Sync

```yaml
# GitHub Actions workflow (.github/workflows/sync-bitbucket.yml)
name: Sync from Bitbucket
on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Mirror sync
        run: |
          git clone --mirror ${{ secrets.BITBUCKET_REPO_URL }} temp-repo
          cd temp-repo
          git remote set-url --push origin ${{ secrets.GITHUB_REPO_URL }}
          git push --mirror
```

---

## Troubleshooting

### Large Repository Issues

- Use `git lfs migrate` for repositories with large files
- Consider `--depth` flag for initial clone if full history isn't needed
- Break down very large repositories into smaller components

### Authentication Problems

```bash
# Set up credential caching
git config --global credential.helper cache

# Use SSH keys for authentication
ssh-keygen -t ed25519 -C "your_email@example.com"
# Add to both Bitbucket and GitHub SSH keys

# Or use personal access tokens
git config --global credential.helper store
```

### Sync Conflicts

- Use `git fetch --all` to get all remote references
- Resolve conflicts manually if branches diverge
- Use `--force` flag cautiously: `git push --mirror --force`

### Permission Errors

- Ensure you have admin access to both repositories
- Check organization policies for repository creation
- Verify API rate limits aren't being exceeded

---

## Security Considerations

1. **Use SSH keys or personal access tokens** for authentication to both Bitbucket and GitHub.
2. **Limit repository access** to trusted users and teams.
3. **Audit sync scripts and workflows** for credential exposure.
4. **Monitor for unauthorized pushes** and repository changes.
5. **Rotate credentials** regularly and remove unused keys/tokens.

---

## Related Resources


*⚡ Pro tip: Automate sync with cron or CI/CD to keep both repositories up-to-date and reduce manual effort!*
 
- [GitHub Repository Duplication Guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository) - Official GitHub documentation
- [Git Mirror Documentation](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---mirror) - Git mirror clone options
- [Bitbucket Import Guide](https://support.atlassian.com/bitbucket-cloud/docs/import-a-repository/) - Importing to Bitbucket
- [GitHub CLI Reference](https://cli.github.com/manual/) - Command-line tool for GitHub operations
- [Git LFS Migration](https://git-lfs.github.io/) - Handling large files in Git repositories
- [GitHub Repository Duplication Guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository) - Official GitHub documentation
- [Git Mirror Documentation](https://git-scm.com/docs/git-clone#Documentation/git-clone.txt---mirror) - Git mirror clone options
- [Bitbucket Import Guide](https://support.atlassian.com/bitbucket-cloud/docs/import-a-repository/) - Importing to Bitbucket
- [GitHub CLI Reference](https://cli.github.com/manual/) - Command-line tool for GitHub operations
- [Git LFS Migration](https://git-lfs.github.io/) - Handling large files in Git repositories

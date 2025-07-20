
## Install Git

First, you'll need to install Git on your computer if you don't already have it.

- On Linux, Git usually comes pre-installed.
- On Mac, install Git via Homebrew with `brew install git`.
- On Windows, download and install Git from [git-scm.com](https://git-scm.com/download/win).

## Configure Git

Once Git is installed, you'll want to configure your name and email since Git embeds this information in commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

## Initialize a Git Repository

To start using Git, you first need to initialize it in the project directory. Do this by running `git init`:

```bash
mkdir myproject
cd myproject
git init
```

This creates a `.git` subdirectory that contains all the Git metadata for the repo.

## Check File Status

```bash
git status
# On branch master
# No commits yet
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
# README.md
```

## Add Files

To start tracking files, use `git add`:

```bash
git add README.md
git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
# new file:   README.md
```

You can also use `git add .` to add all untracked files in the current directory and subdirectories.

## Commit Changes

Once files are staged, you can commit them to the repo with `git commit`:

```bash
git commit -m "Initial commit with README"
[master (root-commit) d32cf1f] Initial commit with README
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

The `-m` flag lets you provide a commit message.

## Push Commits to Remote Repo

To share your code, you'll need to push your commits to a remote repository like GitHub:

```bash
git remote add origin https://github.com/user/myproject.git
git push -u origin master
```

This links the local and remote repositories and pushes the code.

## Pull Latest Code

To get the latest code from the remote repo, use `git pull`:

```bash
git pull origin master
```

This fetches and merges any new commits from the remote into your local branch.

## Create a Branch

To create a new branch, use `git branch`:

```bash
git branch new-feature
git checkout new-feature
# Switched to branch 'new-feature'  
```

Now you can make commits on the new branch.

## Merge a Branch

Once you're done with a feature branch, you can merge it into master:

```bash
git checkout master
git merge new-feature
```

This will combine the branch into master and integrate the code.

And that covers the basics of using Git for version control! Let me know if you have any other questions.
# TIL: Git Tutorial for Beginners (2023-09-28)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](../README.md)

> **Git is a distributed version control system** – Track changes, collaborate, and manage code history for any project.

---

## The Pain Point

Managing code changes and collaboration without version control leads to lost work, merge conflicts, and difficulty tracking history. Git solves these problems with distributed version control and powerful branching.

---

## Summary

Git enables developers to track changes, collaborate, and manage code history efficiently. This guide covers installation, configuration, basic commands, troubleshooting, and security best practices for beginners.

---

## Troubleshooting

- If Git commands fail, check your installation and PATH configuration.
- For merge conflicts, use `git status` and `git mergetool` to resolve issues.
- If commits are missing, check your branch and use `git log` to review history.

---

## Security Considerations

- Never commit secrets, credentials, or sensitive data to your repository.
- Use `.gitignore` to exclude files that shouldn't be tracked.
- Review commit history before pushing to public repositories.

---

## Related Resources

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Guides](https://guides.github.com/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

---

*⚡ Pro tip: Use branches for feature development and pull requests for code review to keep your main branch stable!*

## Git Tutorial for Beginners

## Informations

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 28/09/2023 | 28/09/2023 | 1.0.0   |

## What is Git?

Git is a distributed version control system that allows multiple developers to work on the same codebase. It tracks changes to code over time so you can review and revert to previous versions if needed.

## Install Git

First, you'll need to install Git on your computer if you don't already have it.

- On Linux, Git usually comes pre-installed.
- On Mac, install Git via Homebrew with `brew install git`.
- On Windows, download and install Git from [git-scm.com](https://git-scm.com/download/win).

## Configure Git

Once Git is installed, you'll want to configure your name and email since Git embeds this information in commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```bash

## Initialize a Git Repository

To start using Git, you first need to initialize it in the project directory. Do this by running `git init`:

```bash
mkdir myproject
cd myproject
git init
```bash

This creates a `.git` subdirectory that contains all the Git metadata for the repo.

## Check File Status

```bash
git status
# On branch master
# No commits yet
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
# README.md
```bash

## Add Files

To start tracking files, use `git add`:

```bash
git add README.md
git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
# new file:   README.md
```bash

You can also use `git add .` to add all untracked files in the current directory and subdirectories.

## Commit Changes

Once files are staged, you can commit them to the repo with `git commit`:

```
git commit -m "Initial commit with README"
[master (root-commit) d32cf1f] Initial commit with README
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

The `-m` flag lets you provide a commit message.

## Push Commits to Remote Repo

To share your code, you'll need to push your commits to a remote repository like GitHub:

```
git remote add origin https://github.com/user/myproject.git
git push -u origin master
```

This links the local and remote repositories and pushes the code.

## Pull Latest Code

To get the latest code from the remote repo, use `git pull`:

```
git pull origin master
```

This fetches and merges any new commits from the remote into your local branch.

## Create a Branch

To create a new branch, use `git branch`:

```
git branch new-feature
git checkout new-feature
# Switched to branch 'new-feature'  
```

Now you can make commits on the new branch.

## Merge a Branch

Once you're done with a feature branch, you can merge it into master:

```
git checkout master
git merge new-feature
```

This will combine the branch into master and integrate the code.

And that covers the basics of using Git for version control! Let me know if you have any other questions.


# [![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](../README.md)
# Git Tutorial for Beginners

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

```
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

## Initialize a Git Repository

To start using Git, you first need to initialize it in the project directory. Do this by running `git init`:

```
mkdir myproject
cd myproject
git init
```

This creates a `.git` subdirectory that contains all the Git metadata for the repo.

## Check File Status

```
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

```
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


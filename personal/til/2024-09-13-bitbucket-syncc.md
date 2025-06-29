# Mirroring Bitbucket to GitHub: A Step-by-Step Guide to Repository Synchronization

### Step 1: Create a Mirror Clone of Your Bitbucket Repository

1. Open your terminal.
2. Use the following command to create a mirror clone of your Bitbucket repository:

   ```bash
   git clone --mirror <bitbucket-repo-url>
   ```

   This command will clone the entire repository including all branches and commit history.

### Step 2: Create a New Repository on GitHub

1. Log in to your GitHub account.
2. Create a new empty repository where you will push the mirrored content. Note the URL of this new repository.

### Step 3: Push the Mirror Clone to GitHub

1. Navigate into the directory of the cloned repository:

   ```bash
   cd <repository-name>.git
   ```

2. Set the GitHub repository as the new remote:

   ```bash
   git remote set-url --push origin <github-repo-url>
   ```

3. Push the mirror to GitHub:

   ```bash
   git push --mirror
   ```

### Step 4: Keeping the Repositories Synchronized

To keep both repositories updated, you can periodically fetch updates from Bitbucket and push them to GitHub. Use the following commands:

1. Fetch updates from Bitbucket:

   ```bash
   git fetch -p origin
   ```

2. Push the updates to GitHub:

   ```bash
   git push --mirror
   ```

### Important Notes

- Using the `--mirror` option ensures that all branches, tags, and commit history are preserved when cloning and pushing.
- This method does not create a link between the two repositories, so you will need to manually push updates whenever changes are made in Bitbucket.
- If you prefer a more automated solution, consider using CI/CD tools or scripts to handle the synchronization process.

By following these steps, you can successfully maintain a copy of your Bitbucket project on GitHub while keeping both repositories synchronized with their commit histories intact[1][4][6].

Citations:
[1] https://community.atlassian.com/t5/Bitbucket-questions/I-have-the-requirement-of-copying-the-bitbucket-project-from/qaq-p/1781148
[2] https://community.atlassian.com/t5/Bitbucket-questions/Copy-repository-into-another-project/qaq-p/424320
[3] https://github.com/orgs/community/discussions/84308
[4] https://tommcfarlin.com/migrating-from-bitbucket-to-github/
[5] https://gist.github.com/lsloan/ce704da0d62ce3808dbc12e5a37ba8fc
[6] https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository
[7] https://stackoverflow.com/questions/71262061/copy-git-repository-and-keep-timeline-file-history
[8] https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/copying-an-existing-project
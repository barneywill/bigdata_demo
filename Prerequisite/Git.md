# Git
Git is an essential tool for developers, enabling efficient version control, collaboration, and project management.

| |Index|
|---|---|
|1|[Scenarios](#scenario)|
|2|[Commands(clone, commit, pull, fetch, push, branch, merge, rebase, log, reset)](#command)|

![Git](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git.jpg)

## 1 <a id='scenario'></a>Scenarios
```
git checkout master
git pull origin master
git checkout -b feature
# do your work on branch feature
git status
git add .
git commit -am  "complete a new feature"
git checkout master
git pull origin master
git merge --no-ff feature
git branch -d feature
git push origin master
```

### 1.1 Local changes to remote
- Local changes/Working directory -> [add] -> Staging area/Snapshot -> [commit] -> Local branch -> [push] -> Remote branch
### 1.2 Remote changes to local
- Remote branch -> [pull] -> Working directory
### 1.3 Merge changes between branches
- Local branch -> [checkout] -> Another local branch -> [merge] -> Merged local branch(generate a new merge commit, potential conflicts) -> [push] -> Remote branch
### 1.4 PR: Pull Request
A pull request is a proposal to merge a set of changes from one branch into another. In a pull request, collaborators can review and discuss the proposed set of changes before they integrate the changes into the main codebase.

## 2 <a id='command'></a>Commands

### 2.1 Clone
```
# retrieve an entire repository from a hosted location via URL
git clone $url
```

### 2.2 Commit to Local branch
Smaller, focused commits are easier to review and revert.
```
# show modified files in working directory, staged for your next commit
git status

# diff of what is changed but not staged
git diff

# add a file as it looks now to your next commit (stage)
git add $file_name
# add all changed files
git add .

# commit your staged content as a new commit snapshot
git commit -m 'commit message'
```

### 2.3 Pull & Fetch, Push
Pull before you push
```
# add a remote repository
git remote add origin $url

# fetch and merge any commits from the tracking remote branch
git pull origin $branch_name

# fast forward only, bail out if it can not fast forward
git pull --ff-only origin $branch_name

# Transmit local branch commits to the remote repository branch
git push origin $branch_name

# fetch down all the branches from that Git remote
git fetch
```

#### fetch vs pull
- fetch: git fetch updates your remote-tracking branches under refs/remotes/<remote>/. This operation is safe to run at any time since it never changes any of your local branches under refs/heads.
- pull: git pull brings a local branch up-to-date with its remote version, while also updating your other remote-tracking branches.
- Difference
  - The key difference between git fetch and pull is that git pull copies changes from a remote repository directly into your working directory, while git fetch does not.
  - git pull runs git fetch with the given parameters and then depending on configuration options or command line flags, will call either git rebase or git merge to reconcile diverging branches.

### 2.4 Branch
Create branches for features, fixes, and experiments.
```
# list your branches. a * will appear next to the currently active branch
git branch

# create a new branch at the current commit
git branch $branch_name

# switch to another branch and check it out into your working directory
git checkout $branch_name

# merge the specified branch’s history into the current one
git merge $other_branch_name

# The --no-ff flag prevents git merge from executing a "fast-forward" if it detects that your current HEAD is an ancestor of the commit you're trying to merge.
git merge --no-ff $other_branch_name

# replay commits from current branch one by one on other_branch_name
git rebase $other_branch_name

# delete a branch
git branch -d $branch_name

# compare branches
git diff $branch1..$branch2
```

### 2.5 Log
```
# show the commit history for the currently active branch
git log
```

### 2.6 Undo changes
```
# file-level: discard unstaged changes
git checkout -- $file_name

# file-level: unstage a file while retaining the changes in working directory
git reset $file_name

# commit-level: move HEAD back to commit_id to inspect old snapshots
git checkout $commit_id

# commit-level: clear staging area, rewrite working tree from specified commit, --soft, --mixed, --hard
git reset --hard HEAD

# apply any commits of current branch ahead of specified one
git rebase -i HEAD~1
```

#### HEAD
Git resolves HEAD in one of two ways:
- if .git/HEAD contains a branch name, it’ll be the latest commit on that branch (for example by reading it from .git/refs/heads/main)
- if .git/HEAD contains a commit ID, it’ll be that commit ID

Other HEAD: ORIG_HEAD, FETCH_HEAD, MERGE_HEAD

#### three trees
- Working directory
- Staged snapshot
- Commit history

![Git 3 Trees](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git_3_trees.jpg)

#### reset
- --soft: The staged snapshot and working directory are not altered in any way.
- --mixed: Default. The staged snapshot is updated to match the specified commit, but the working directory is not affected.
- --head: The staged snapshot is updated to match the specified commit, but the working directory is not affected. This is the default option.

### 2.7 Conflicts
Decide if you want to keep only your branch's changes, keep only the other branch's changes, or make a brand new change.
```
If you have questions, please
<<<<<<< HEAD
open an issue
=======
ask your question in IRC.
>>>>>>> branch-a
```

![Git Conflicts](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git_conflicts.jpg)

#### 2.7.1 Merge
- --ff: default
- --ff-only: force git to abort the merge if it can't just replay the commits (ie if any additional commits have been made on the main branch since you took the current branch).
- --no-ff: force git to create a new "merge commit" in the feature branch that ties together the histories of both branches.
```
git checkout feature
git merge master
```

![Git Merge](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git_merge.jpg)

```
git checkout master
git merge feature
```

![Git Merge](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git_merge2.jpg)

#### 2.7.2 Rebase, Merge
- Only rebase on a private or temporary branch
- Replay commits from feature one by one on the top of the master branch. 
- Re-write the project history by creating brand new commits for each commit in the original branch.
```
git checkout feature
git rebase master
```

![Git Rebase](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git_rebase.jpg)

```
git checkout master
git merge feature
```

![Git Rebase & Merge](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git_rebase_merge.jpg)

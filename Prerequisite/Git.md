# Git
Git is easy to learn and has a tiny footprint with lightning fast performance.

![Git](https://github.com/barneywill/bigdata_demo/blob/main/imgs/git.jpg)

## 1 Scenarios
### 1.1 Local changes to remote
- Changes -> [add] -> Staging area, Snapshot -> [commit] -> Local branch -> [push] -> Remote branch
### 1.2 Remote changes to local
- Remote branch -> [pull] -> Local branch
### 1.3 Merge changes between branches
- Local branch -> [checkout] -> Another local branch -> [merge] -> Merged local branch -> [push] -> Remote branch
### 1.4 PR: Pull Request
A pull request is a proposal to merge a set of changes from one branch into another. In a pull request, collaborators can review and discuss the proposed set of changes before they integrate the changes into the main codebase.

## 2 Commands

### 2.1 Clone
```
# retrieve an entire repository from a hosted location via URL
git clone $url
```

### 2.2 Commit
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

### 2.3 Pull & Push
Pull before you push
```
# add a remote repository
git remote add origin $url

# fetch and merge any commits from the tracking remote branch
git pull origin $branch_name

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
# discard unstaged changes
git checkout -- $file_name

# unstage a file while retaining the changes in working directory
git reset $file_name

# clear staging area, rewrite working tree from specified commit
git reset --hard HEAD

# apply any commits of current branch ahead of specified one
git rebase -i HEAD
```
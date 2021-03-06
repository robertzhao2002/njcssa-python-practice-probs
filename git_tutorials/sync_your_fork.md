# Guide on how to sync your fork to the most updated version of the repository

Forks need to be syncronized periodically to the main repository they are forking. Otherwise they will get behind or ahead of the repository. This can lead to conflicts when trying to merge changes into the main repository.

This guide assumes you have already forked the main repository into your own copy and installed Git.

When you get behind or ahead of the main njcssa repository, github will tell you on your forked version. It will look like this:

![](/git_tutorials/sync_fork_imgs/commits_behind.png)

If your repository is behind you just need to follow the following steps. If it is ahead that means you have been working on something. If you are done working on it submit a pull request to incorporate it into the main njcssa repository.

There are two ways to do it: manually everytime or using scripts.
# Manually:
## Steps
### 1. Open up Git Bash on your PC
Search for "git bash" in your windows search bar

![](/git_tutorials/sync_fork_imgs/search_program.PNG)

Git Bash looks like this 

![](/git_tutorials/sync_fork_imgs/git_bash.PNG)

### 2. use the CD command to cd into your cloned directory
![](/git_tutorials/sync_fork_imgs/cd_directory.PNG)
### 3. Add the remote repository as an upstream
Skip this step and they next if you have already added the upstream before.

You need to get the .git link to the repository. In this case it will look like https://github.com/njcssa/njcssa-python-practice-probs.git

Now enter the following command when you are in the forked directory
![](/git_tutorials/sync_fork_imgs/addupstream.PNG)

### 4. Verify the new upstream repository you've specified for your fork.
![](/git_tutorials/sync_fork_imgs/check_remote.PNG)

### 5. Fetch the remote repository
![](/git_tutorials/sync_fork_imgs/fetch_upstream.PNG)
### 6. Checkout master branch
![](/git_tutorials/sync_fork_imgs/checkout_master.PNG)
### 7. Merge the upstream branch from main repository into your master branch
There should not be a merge conflict because people should be working on separate parts. If there is a merge conflict dm Ben C. so he can sort it out.

![](/git_tutorials/sync_fork_imgs/merge_upstream.PNG)
### 8. push new commits to master branch of your forked version
![](/git_tutorials/sync_fork_imgs/push_origin.PNG)

You should now be up to date with the main repository!

<br />

# Using scripts (Windows)
This should do everything above except much easier for you.

## 1. You can either use Update.bat or Update2.bat.
If you use Update2.bat, you will need to enter your NJCSSA location every single time to sync your fork. If don't want to do that, read ahead.

### 2. Copy & edit the Update.bat
First, make a copy of the Update.bat file outside of this folder. Once you do so, edit it in whatever text editor (Notepad, Notepad++). Then, where it says "cd C:/njcssa-python-practice-probs", replace the "C:/njcssa-python-practice-probs" with the absolute path to your cloned directory (where the "njcssa-python-practice-probs" folder is).

### 3. Run it
Now, double click on the .bat file, and you know have a script that automates updating the fork for you!


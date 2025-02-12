#################################################
#
# ----To perform a normal push to git----
#
#################################################
## ALWAYS begin with
git pull origin
## or
git pull origin main



##################################################
#
# ----To establish/overhaul git----
#
# Issue these commands one by one in the terminal
# Do not run this file as a script!
# See how_to_set_github_credentials.pdf for instructions
# on personal access tokens
#
# Author: M Joyce
#
#################################################

## navigate to the repository on your computer that
## you want to link with your PHYS4840 repository on GitHub
git init 

git checkout -b main

## change this url to YOUR github repo address
git remote add origin https://github.com/mjoyceGR/PHYS4840.git
git remote -v

 # should return: 
 # origin	https://github.com/mjoyceGR/PHYS4840.git (fetch)
 # origin	https://github.com/mjoyceGR/PHYS4840.git (push)

## pull the material from the remote host to your machine
git pull origin main --allow-unrelated-histories
## this avoids conflicts with any existing history on GitHub 


## should return something like:
# remote: Enumerating objects: 6, done.
# remote: Counting objects: 100% (6/6), done.
# remote: Compressing objects: 100% (3/3), done.
# remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
# Unpacking objects: 100% (6/6), 1.82 KiB | 1.82 MiB/s, done.
# From https://github.com/mjoyceGR/PHYS4840
#  * branch            main       -> FETCH_HEAD
#  * [new branch]      main       -> origin/main

git branch --show-current  # Should return "main"

## set your upstream branch to "main" to avoid 
## pushing to "master" by accident
git branch --set-upstream-to=origin/main main
## should return:
#	Branch 'main' set up to track remote branch 'main' from 'origin'.


## prepare a file for subimssion; aka "track" the file
git add <name_of_your_file.py>


## commit the file and DESCRIBE what you are doing
git commit -m "I am committing my_file.py because ..."

## as part of completing the "push" step, you will have to
## generate your personal access token and enter your login credentials
## follow the instructions on my slide (Lecture 6) to do this

## push the commit to the main branch
git push origin

#----------------------------------------------------------------
#
# TROUBLESHOOTING
#
# If you keep encountering issues, REMOVE git from your
# directory on your computer and restart this protocol
# from the beginning. Here are the steps to un-git a repository
#
#----------------------------------------------------------------

## (1) navigate to the repository you want to un-git in the terminal
## (2) issue the following commands:
rm -rf .git
rm -rf .gitignore

## if you have successfully removed .git and .gitingore, the command
git status
## should return
## 		fatal: not a git repository (or any of the parent directories): .git
##
## if this is NOT returned, you may have recursive versions of git!
## In this case, run
##      find . -name ".git" -type d
## 		find . -name ".gitignore" -type d
##
## and un-git the repositories this returns as well
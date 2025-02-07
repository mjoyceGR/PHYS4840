##################################################
#
# Issue these commands one by one in the terminal
# Do not run this file as a script!
# See the 
#
# Author: M Joyce
#
#################################################

## navigate to the repository on your computer that
## you want to link with your PHYS4840 repository on GitHub
git init -b main

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



## prepare a file for subimssion; aka "track" the file
git add 'my_file.py'


## commit the file and DESCRIBE what you are doing
git commit -m "I am committing my_file.py because ..."


## as part of completing the "push" step, you will have to
## generate your personal access token and enter your login credentials
## follow the instructions on my slide (Lecture 6) to do this

## push the commit to the main branch
git push origin

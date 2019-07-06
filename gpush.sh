#!/bin/bash
user="mmark0v"
pass=""
repo="https://github.com/mmark0v/ELS"
git config --global credential.helper "cache --timeout 7200"
git pull $repo
git add .
git commit -m "Directory Update"
git push origin master

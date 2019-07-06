#!/bin/bash
user="mmark0v"
pass="Ivan4ovapolqna"
repo="https://github.com/mmark0v/ELS"

git pull $repo
git add .
git commit -m "$1"
git push origin master
$user
$pass

#!/usr/bin/env bash

ROOT="$( cd "$(dirname "$0")" ; pwd -P )"/../server

cd $ROOT 

rm Dockerfile
rm git_push.sh 
rm README.md 
rm requirements.txt
rm tox.ini
rm setup.py
rm test-requirements.txt 
rm -r test 
rm .dockerignore 
rm .gitignore 
rm .travis.yml

mv swagger_server/* .
rmdir swagger_server

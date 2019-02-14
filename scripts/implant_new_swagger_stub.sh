#!/usr/bin/env bash

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )" 
ROOT=$SCRIPT_PATH/../server
unzip ~/Downloads/python-flask-server-generated.zip -d $ROOT
rm ~/Downloads/python-flask-server-generated.zip

cd $ROOT 

rm Dockerfile
rm git_push.sh 
rm README.md 
rm requirements.txt
rm tox.ini
rm setup.py
rm test-requirements.txt 
rm .dockerignore 
rm .gitignore 
rm .travis.yml

rm -r controllers swagger models
mv swagger_server/* .
rmdir swagger_server 
rm -r test 

python3 $SCRIPT_PATH/fix_imports.py
python3 $SCRIPT_PATH/populate_controllers.py 
cp $SCRIPT_PATH/data/__main__.py $ROOT

# Python project scaffold
This repo contains starter code for python projects

# Files Contained
1. makefile
2. requirements.txt
3. factorial.py
4. test_factorial.py
5. virtual env

# Connecting to github via SSH
- There are other ways to connect but this is preferred
1. Set up keys in server
  `ssh -keygen -t rsa`
2. Print out the public key
  `cat`
3. Register public key in github

# Virtual Environment
- Why use a virtual environment? 

Purpose is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

## Install venv
`python3 -m pip install virtualenv`

## Creating virtual environment 
Good practice to give it the same name as your repo

Create virtual envrionment with python 3 as base `python 3 -m venv ~/.python_scaffold`

## Activating virtual environment
Activate virtual environment `source ~/.python_scaffold/bin/activate`

Check the python version and path using `which python`

# Github actions / Continuous integration
Running a series of 'actions' when you push to the master/main branch

## Use your makefile to run steps

## <Add other uses of Github actions>

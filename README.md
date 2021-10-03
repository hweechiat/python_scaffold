# Python project scaffold
This repo contains starter code for python projects

# Files Contained
1. makefile
2. requirements.txt
3. hello.py
4. test_hello.py
5. virtual env

# Connecting to github via SSH
- There are other ways to connect but this is preferred
1. Set up keys in server
  `ssh -keygen -t rsa`
2. Use `cat` to print out the public key
3. Register public key in github

# Virtual Environment
- Why use a virtual environment? Purpose is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.

## Creating virtual environment 
- good practice to give it the same name as your repo
`python 3 -m venv ~/.python_scaffold`

## Activating virtual environment
`source ~/.python_scaffold/bin/activate`
check the python version and path using `which python`

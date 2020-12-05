# Git commands

git clone "whatever the name of your repo is"
(Wherever you want it to be) and then cd into the repo name)

git pull
(Pulls the latest change, if any, down to your machine)

git checkout -b your_branch_name
(Create branch and check it out)

git checkout your_branch_name
(Check out branch)

git branch
(To see a list of your branches and the branch you are on:

git push origin your_branch_name
(Push up your branch to remote (Github))
For example: git push origin master

git branch -d your_branch_name
(To delete a local branch)

git merge branch_name
(To merge a branch with another)


# Terminal/Git Bash commands

ls
(Will list all of the files and directories in the current directory)

cd your_directory
(Will change the current directory to "your_directory")

cd ..
(Will go back one directory)

pwd
(Will show you the full path of your current directory)

cd directoryfilename
(Will change to the directory directoryfilename)
For example, if Desktop is in your current directory you can change to the Desktop with:
cd Desktop

mkdir PythonStuff
(Will make a new directory/folder called PythonStuff on the desktop.)

cd PythonStuff 
(Will move to the newly created folder called PythonStuff)

touch first_file.py 
(Will create a file called first_file.py)

touch second_file.py 
(Will create a second file called second_file.py.)

clear
Clears the screen

`open .` on a Mac or `explorer .` in PC will open the current folder

# Conda commands

#### Creating an "environment" called PythonData (but you can create other conda enviroments with different names)
conda create -n PythonData python=3.6 anaconda

#### Listing out your conda environments. A "*" will be next to the one that is active:
conda env list

#### Activating a conda environment called PythonData:

source activate PythonData

or 

conda activate PythonData

#### Checking conda version:
conda --version

#### To make sure condas environment can be used in Jupyter Notebook
conda install -c anaconda nb_conda_kernels

# Python

#### To check your version:
python --version

#### To check which version of Python you are running:
which python

#### To run Python commands at the command prompt (REPL):
python

#### To exit the command version of Python:
exit()

#### To run a python file called "example.py"
python example.py


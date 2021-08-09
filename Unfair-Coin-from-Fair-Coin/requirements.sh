#!/bin/bash

# - Author: Soheil Esmaeilzadeh
# - Created on: 08/08/2021
# - Email: soes@alumni.stanford.edu

echo "======================================="
echo "installing 'virtual env' ..."
echo "======================================="
pip install virtualenv 

if [ ! -d "./virtual_env_unfair_coin/" ] 
then
    echo "======================================="
    echo "creating a virtual environment named 'virtual_env_unfair_coin' ..."
    echo "======================================="
    virtualenv virtual_env_unfair_coin
    source virtual_env_unfair_coin/bin/activate
else
    echo "======================================="
    echo "a virtual environment named 'virtual_env_unfair_coin' already exists!"
    echo "======================================="
fi

echo "======================================="
echo "activating the virtual environment named 'virtual_env_unfair_coin' ..."
echo "======================================="
source virtual_env_unfair_coin/bin/activate


printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'matplotlib' ..."
echo "============================="
pip install matplotlib

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
echo "installing 'logging' ..."
echo "============================="
pip install logging


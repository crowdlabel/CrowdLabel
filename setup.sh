#!/bin/bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt upgrade -y
sudo apt install python3.11 python3.11-distutils python3-pip npm

python3.11 -m pip install -r src/backend/requirements.txt
#npm 
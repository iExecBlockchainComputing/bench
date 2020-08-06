#!/bin/bash

apt update

apt install ansible curl -y

curl -o ./install.sh https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh 

chmod +x install.sh

./install.sh < "/dev/null"

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

nvm install 10

npm i ethers
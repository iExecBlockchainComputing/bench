#!/bin/bash

if [ $1 != "" ] 
then

  ssh -i ~/.ssh/grid5000 npayre@frontend.lyon.grid5000.fr

  scp -r -i ~/.ssh/bench ./poa-deployment-bench/ root@$1:. < "/dev/null"
  scp -r -i ~/.ssh/bench ~/.ssh/bench* root@$1:.ssh/ < "/dev/null"
  
  ssh -i ~/.ssh/bench root@$1 apt update
  ssh -i ~/.ssh/bench root@$1 apt install ansible -y < "/dev/null"

  ssh -i ~/.ssh/bench root@$1 export ANSIBLE_HOST_KEY_CHECKING=False
fi

# ansible-playbook -i hosts site.yml
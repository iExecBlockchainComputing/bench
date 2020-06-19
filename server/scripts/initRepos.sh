#!/bin/bash
USER='nathPay'

if [ -d "./repos/poa-deployment-bench" ]; then
  cd ./repos/poa-deployment-bench;
  git pull;
else
  cd ./repos && git clone https://github.com/$USER/poa-deployment-bench.git
fi
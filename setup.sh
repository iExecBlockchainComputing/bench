#!/bin/bash

oarsub -I -l nodes=3,walltime=0:30 -t deploy

kadeploy3 -f $OAR_NODE_FILE -e ubuntu1804-x64-min -k ~/.ssh/bench.pub
#!/bin/bash

scp -r ./server/repos/poa-deployment-bench/ npayre@frontend.lyon.grid5000.fr:. < "/dev/null"
scp -r ./server/scenarios/ npayre@frontend.lyon.grid5000.fr:. < "/dev/null"
scp -r ./server/scripts/ npayre@frontend.lyon.grid5000.fr:. < "/dev/null"
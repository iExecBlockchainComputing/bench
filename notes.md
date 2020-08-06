# Starting Bench 

frontend$ oarsub -I -l "nodes=5,walltime=00:40:00" -t deploy -p "cluster='taurus'"
frontend$ kadeploy3 -f $OAR_FILE_NODES -e debian10-x64-base -k ~/.ssh/bench.pub

host$ scp -r ./repos/poa-deployment-bench/ npayre@frontend.lyon.grid5000.fr:.
host$ scp -r ./scenarios/* npayre@frontend.lyon.grid5000.fr:.

frontend$ scp -r -i .ssh/bench .ssh/bench* root@taurus-1.lyon.grid5000.fr:.ssh/
frontend$ scp -r -i .ssh/bench poa-deployment-bench/ root@taurus-1.lyon.grid5000.fr:.
 
frontend$ taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast put { ./? } { ./ }

frontend$ taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast exec [ "mv ./?/* ." ]

moc$ export ANSIBLE_HOST_KEY_CHECKING=False
moc$ cd poa-deployment-bench && ansible-playbook -i hosts site.yml

frontend$ taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast exec [ "npm i ethers" ]

# After Bench:

frontend$ mkdir results

frontend$ taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast get { ./? } { ./results/ }

frontend$ taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast get { /tmp/logs/ } { ./results/ }

host$ scp -r npayre@frontend.lyon.grid5000.fr:./results ./saves/name

# Starting Bench 

frontend$ 
oarsub -I -l "nodes=32,walltime=03:00:00" -t deploy -p "cluster='gros'"

frontend$ 
kadeploy3 -f $OAR_FILE_NODES -e debian10-x64-base -k ~/.ssh/bench.pub

host$ 
scp -r ./repos/poa-deployment-bench/ npayre@frontend.lyon.grid5000.fr:.

host$ 
scp -r ./scenarios/* npayre@frontend.lyon.grid5000.fr:.

frontend$ 
scp -r -i .ssh/bench .ssh/bench* root@nova-1.lyon.grid5000.fr:.ssh/

frontend$ 
scp -r -i .ssh/bench poa-deployment-bench/ root@nova-1.lyon.grid5000.fr:.
 

frontend$
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast put { .ssh/id_rsa } { .ssh/id_rsa }

frontend$
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast put { .ssh/id_rsa.pub } { .ssh/id_rsa.pub }

frontend$
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast exec [ "apt update && apt install ansible -y" ]

frontend$
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast put { ./13 } { ./ }

frontend$ 
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast exec [ "mv ./13/* ." ]

moc$ 
export ANSIBLE_HOST_KEY_CHECKING=False

moc$ 
ansible-playbook -i hosts site.yml

frontend$ 
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast exec [ "npm i ethers" ]

# After Bench:

frontend$ 
mkdir results

frontend$ 
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast get { ./0 } { ./ }

frontend$ 
taktuk -l root -s -o connector -o status -o output='"$host: $line\n"' -f <( uniq $OAR_FILE_NODES ) broadcast get { /tmp/logs/ } { ./ }

host$ scp -r npayre@frontend.lyon.grid5000.fr:./results ./saves/name
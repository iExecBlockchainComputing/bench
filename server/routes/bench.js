var express = require('express');
var router = express.Router();
var fs = require('fs');
var fsPromise = require('fs').promises;
var path = require('path');
var async = require('async');
var shell = require('shelljs');
var yml = require('yaml');

router.post('/poaMocGroup', function(req, res) {
  var path = "./repos/poa-deployment-bench/";
  var poaDeployementRepo = req.body.poaDeployementRepo;
  var mocParsed = {};
  var bootnodeParsed = {};
  var validatorParsed = {};
  // fs.writeFile('./getBootnode.sh', `curl -H "Content-Type: application/json" -k --data '{ "method": "parity_enode", "params": [], "id": 1, "jsonrpc": "2.0" }' -X POST taurus-13.lyon.grid5000.fr:8545 | jq ".result" > bootnode.txt`, )
  shell.exec('./scripts/initRepos.sh', (code, stdout, stderr) => {
    // shell.mkdir('./repos/poa-deployment-bench/group_vars/');
    shell.cp('./repos/poa-deployment-bench/group_vars_tpl/*', './repos/poa-deployment-bench/group_vars/');
    
    //Modifying groups
    fsPromise.readFile('./encryptedWallet/wallet.json', 'utf8', (err) => {
      if(err) throw err;
    }).then(encryptedWallet => {
      //bootnode
      fsPromise.readFile(path + 'group_vars_tpl/poa-bootnode-group.yml', "utf8", (err2) => {
        if(err2) throw err2;
      }).then(data => {
        bootnodeParsed = yml.parse(data);
      }).then(() => {
        bootnodeParsed.SCRIPTS_MOC_BRANCH = req.body.chainName + '-init';
        bootnodeParsed.MAIN_CHAINSPEC_REPO_FETCH = req.body.repoFetch;
        bootnodeParsed.GENESIS_BRANCH = req.body.chainName;
        bootnodeParsed.GENESIS_NETWORK_NAME = req.body.chainName;
        bootnodeParsed.MOC_ADDRESS = req.body.mocAddress;
        bootnodeParsed.NODE_FULLNAME = req.body.chainName + '-bootnode';
        bootnodeParsed.NODE_ADMIN_EMAIL = req.body.mail;
        // bootnodeParsed.NETSTATS_SERVER = req.body.netstatIp;
      }).then(() => {
        bootnodeParsed = yml.stringify(bootnodeParsed);
      }).then(() => {
        fsPromise.writeFile(path + 'group_vars/poa-bootnode-group.yml', bootnodeParsed, (err3) => {
          if(err3) throw err3;
        })
      })

      req.body.otherHost.forEach((el, index) => {
        fsPromise.readFile(path + 'group_vars_tpl/poa-validator-group.yml', "utf8", (err2) => {
          if(err2) throw err2;
        }).then(data => {
          validatorParsed = yml.parse(data);
        }).then(() => {
          validatorParsed.SCRIPTS_MOC_BRANCH = req.body.chainName + '-init';
          validatorParsed.MAIN_CHAINSPEC_REPO_FETCH = req.body.repoFetch;
          validatorParsed.GENESIS_BRANCH = req.body.chainName;
          validatorParsed.GENESIS_NETWORK_NAME = req.body.chainName;
          validatorParsed.MOC_ADDRESS = req.body.mocAddress;
          validatorParsed.NODE_FULLNAME = req.body.chainName + '-validator' + index;
          validatorParsed.NODE_ADMIN_EMAIL = req.body.mail;
          validatorParsed.bootnode_host = req.body.bootnodeHost;
          // validatorParsed.NETSTATS_SERVER = req.body.netstatIp;
        }).then(() => {
          validatorParsed = yml.stringify(validatorParsed);
        }).then(() => {
          fsPromise.writeFile(path + 'group_vars/poa-' + index + '-group.yml', validatorParsed, (err3) => {
            if(err3) throw err3;
          })
        })
      });

      //MOC
      fsPromise.readFile(path + 'group_vars_tpl/poa-moc-group.yml', "utf8", (err2) => {
        if(err2) throw err2;
      }).then(data => {
        mocParsed = yml.parse(data);
      }).then(() => {
        mocParsed.SCRIPTS_MOC_BRANCH = req.body.chainName + '-init';
        mocParsed.MAIN_CHAINSPEC_REPO_FETCH = req.body.repoFetch;
        mocParsed.GENESIS_BRANCH = req.body.chainName;
        mocParsed.GENESIS_NETWORK_NAME = req.body.chainName;
        mocParsed.MOC_ADDRESS = req.body.mocAddress;
        mocParsed.NODE_FULLNAME = req.body.chainName + '-moc';
        mocParsed.NODE_ADMIN_EMAIL = req.body.mail;
        mocParsed.bootnode_host = req.body.bootnodeHost;
        // mocParsed.NETSTATS_SERVER = req.body.netstatIp;
        mocParsed.MOC_KEYFILE = encryptedWallet;
      }).then(() => {
        mocParsed = yml.stringify(mocParsed);
      }).then(() => {
        fsPromise.writeFile(path + 'group_vars/poa-moc-group.yml', mocParsed, (err3) => {
          if(err3) throw err3;
        }).then(() => {
          var permanent = `
[bootnode]
poa-bootnode

[moc]
poa-moc
          
[poa:children]
bootnode
moc
validator`;

          var moc = `
[poa-moc-group]
poa-moc

[poa-moc-group:vars]
ansible_ssh_host=${req.body.mocHost}
ansible_ssh_private_key_file=~/.ssh/bench
ansible_ssh_user=root
ansible_sudo_pass=""`;
          
            var bootnode = `
[poa-bootnode-group]
poa-bootnode

[poa-bootnode-group:vars]
ansible_ssh_host=${req.body.bootnodeHost}
ansible_ssh_private_key_file=~/.ssh/bench
ansible_ssh_user=root
ansible_sudo_pass=""`;
            var eof = '';
            var validators = `
[validator]`;
            var ubuntu = `
[ubuntu]
poa-bootnode
poa-moc`;
            req.body.otherHost.forEach((validatorAddress, index) => {
              ubuntu = ubuntu + `
poa-${index}`
              validators = validators + `
poa-${index}`;
              eof = eof + `
[poa-${index}-group]
poa-${index}

[poa-${index}-group:vars]
ansible_ssh_host=${validatorAddress}
ansible_ssh_private_key_file=~/.ssh/bench
ansible_ssh_user=root
ansible_sudo_pass="" ` + "\n";
            });
            var hosts = permanent + "\n" + validators + "\n" + ubuntu + "\n" + moc + "\n" + bootnode + "\n" + eof;
          
            fsPromise.writeFile( "./repos/poa-deployment-bench/hosts", hosts, (err4) => {
              if(err4) throw err4;
            }).then(() => {
              res.send();
            })
        })
      })
    })

  })

});

router.post('/genSpec', function(req, res) {
  var path = "./repos/poa-deployment-bench/";
  fsPromise.writeFile(path + 'spec.json', JSON.stringify(req.body.spec), (err) => {
    if(err) throw err;
  }).then(() => {
    res.send(JSON.stringify({type: "success", msg:"spec file generated"}))
  })
})

router.post('/genScenarioData', function(req, res) {
  var ips = {
    'bootnode': req.body.bootnodeIP,
    'moc': req.body.mocIP,
    'validators': req.body.otherHostIP
  };

  fsPromise.writeFile('./scenariosTpl/ips.json', JSON.stringify(ips), (err) => {
    if(err) throw err;
  })

  fsPromise.writeFile('./scenariosTpl/wallets.json', JSON.stringify(req.body.wallets), (err) => {
    if(err) throw err;
  })
  res.send(JSON.stringify({type: "success", msg:"Scenario preparation generated"}))
})

module.exports = router;
var express = require('express');
var router = express.Router();
var fs = require('fs');
var fsPromise = require('fs').promises;
var path = require('path');
var shell = require('shelljs');
const ethers = require('ethers');

var scenariosDirectory = "./scenarios";

function txPerSecTpl(time, priority, nbTx, timeBetween, wallets, it) {
  let ips = JSON.parse(fs.readFileSync('./scenariosTpl/ips.json'));
  let process = ``;
  wallets.forEach((el, index) => {
    if(ips.safeNodes != null) {
      process = process + `
  # ${nbTx} Tx spaced by ${timeBetween} at ${time}
  s.enter(${time}, ${priority}, process, argument=(${timeBetween}, "${el.signingKey.address}.json", ${it}, "${ips.safeNodes[index%ips.safeNodes.length]}"))
  `
    } else {
      process = process + `
  # ${nbTx} Tx spaced by ${timeBetween} at ${time}
  s.enter(${time}, ${priority}, process, argument=(${timeBetween}, "${el.signingKey.address}.json", ${it}, "${ips.noBootnode[index%ips.noBootnode.length]}"))
  `
    }
  });

  return process;
}

function killNodeTpl(time, priority, nbValidators, bootnode, validators, reUpAt) {
  switch (bootnode) {
    case true:
      bootnode = "True";
      break;
    case false:
      bootnode = "False"
      break;
    default:
      break;
  }
  switch (validators) {
    case true:
      validators = "True";
      break;
    case false:
      validators = "False"
      break;
    default:
      break;
  }
  let ips = JSON.parse(fs.readFileSync('./scenariosTpl/ips.json'));
  let res = ``;
  let safeNodes = [];
  safeNodes.push(ips.moc);
  if(bootnode === "True") {
    res = res + `
  #Killing bootnode at ${time} and reUp at ${reUpAt}
  s.enter(${time}, ${priority}, killNodes, argument=(${time}, "${ips.bootnode}"))
  s.enter(${reUpAt}, ${priority}, reUpNodes, argument=(${time}, "${ips.bootnode}"))
    `
  } else {
    safeNodes.push(ips.bootnode);
  }
  if(validators === "True") {
    for (let i = 0; i < nbValidators; i++) {
      res = res + `
  #Killing ${ips.validators[i]} at ${time} and reUp at ${reUpAt}
  s.enter(${time}, ${priority}, killNodes, argument=(${time}, "${ips.validators[i]}"))
  s.enter(${reUpAt}, ${priority}, reUpNodes, argument=(${time}, "${ips.validators[i]}"))`
    }
    for (let i = ips.validators.length; i > nbValidators; i--) {
      safeNodes.push(ips.validators[i - 1]);
    }
  }
  ips["safeNodes"] = safeNodes;
  fs.writeFileSync('./scenariosTpl/ips.json', JSON.stringify(ips));
  return res;
}

function networkDegradeTpl(time, priority, nbValidators, bootnode, validators, restoreAt, latency, download, upload, packetLoss) {
  switch (bootnode) {
    case true:
      bootnode = "True";
      break;
    case false:
      bootnode = "False"
      break;
    default:
      break;
  }
  switch (validators) {
    case true:
      validators = "True";
      break;
    case false:
      validators = "False"
      break;
    default:
      break;
  }
  let ips = JSON.parse(fs.readFileSync('./scenariosTpl/ips.json'));
  let res = ``;
  if(bootnode === "True") {
    res = res + `
  #Degrating bootnode Network at ${time} and restore at ${restoreAt}
  s.enter(${time}, ${priority}, networkDegrade, argument=(${time}, "${ips.bootnode}", "${latency}", "${download}", "${upload}", "${packetLoss}"))
  s.enter(${restoreAt}, ${priority}, restoreNetwork, argument=(${time}, "${ips.bootnode}", "${latency}", "${download}", "${upload}", "${packetLoss}"))
    `
  }
  if(validators === "True") {
    for (let i = 0; i < nbValidators; i++) {
      res = res + `
  #Degrating ${ips.validators[i]} Network at ${time} and restore at ${restoreAt}
  s.enter(${time}, ${priority}, networkDegrade, argument=(${time}, "${ips.validators[i]}", "${latency}", "${download}", "${upload}", "${packetLoss}"))
  s.enter(${restoreAt}, ${priority}, restoreNetwork, argument=(${time}, "${ips.validators[i]}", "${latency}", "${download}", "${upload}", "${packetLoss}"))
  `
    }
  }
  return res;
}

function genTransactionsArray(nbTx, timeBetween2Tx, during, scenarioNumber) {
  return new Promise((resolve, reject) => {
    let tx = {};
    fsPromise.readFile(scenariosDirectory + "/" + scenarioNumber + "/wallets.json", (err) => {
      if (err) throw err;
    })
    .then(data => JSON.parse(data.toString()))
    .then((wallets) => {
      wallets.forEach(el => {
        tx[el.address] = {};
        tx[el.address].txs = [];
        tx[el.address].privKey = el.privKey;
        tx[el.address].timeBetween2Tx = timeBetween2Tx;
      });
      wallets.forEach(el => {
        let j = 0;
        for (let i = 0; i < nbTx * during; i++) {
          tx[el.address].txs.push({
            'to': ethers.utils.hexlify(ethers.utils.randomBytes(20)),
            'value': "0x0",
            'nonce': Math.trunc(j)
          });
          j = j + 1;
        }
      });
    })
    .then(() => resolve(tx))
  })
}

router.post('/genScenario', function (req, res) {
  var events = [];
  var scenario = "";
  req.body.events.forEach((event, it) => {
    switch (event.type) {
      case 1:
        events.push(killNodeTpl(
          event.time,
          event.priority,
          event.nbNodes,
          event.bootnode,
          event.validators,
          event.reUpAt
        ));
        break;
      case 2:
        events.push(networkDegradeTpl(
          event.time,
          event.priority,
          event.nbNodes,
          event.bootnode,
          event.validators,
          event.restoreAt,
          event.latency,
          event.download,
          event.upload,
          event.packetLoss
        ));
        break;
      default:
        break;
    }
  });
  req.body.events.forEach((event, it) => {
    switch (event.type) {
      case 0:
          events.push(txPerSecTpl(
          event.time,
          event.priority,
          event.nbTx,
          Math.trunc(100 / ((event.nbTx / req.body.wallets.length) / 10)),
          req.body.wallets,
          it
        ));
        break;
      default:
        break;
    }
  });
  events.forEach(event => {
      scenario = scenario + `${event}
`
  });
  fsPromise.readdir(scenariosDirectory, (err, dirs) => {
    if (err) throw err;
  }).then((dirs) => {
    fsPromise.mkdir(path.join(scenariosDirectory, (dirs.length + 1).toString()), (err) => {
      if (err) throw err;
    }).then(() => {
      var data =
        `import sched, time, json
import subprocess

s = sched.scheduler(time.time, time.sleep)

def printTime(a='default'):
  print("From print_time", time.time(), a)

def process(timeBetween, fileName, eventNumber, ip):
  print("process: " + str(eventNumber))
  subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "node", "./process.js", str(fileName), str(timeBetween), str(eventNumber), str(ip)])

def getResultTx(time, ip):
  print("getResultsTx: " + str(time))
  subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "node", "./postProcess.js", str(time)])

def killNodes(time, ip):
  print("KillNodes:" + str(time))
  subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "service", "poa-parity", "stop"])

def reUpNodes(time, ip):
  print("reUpNodes:" + str(time))
  subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "service", "poa-parity", "start"])

def networkDegrade(time, ip, latency, download, upload, packetLoss):
  print("networkDegrade:" + str(time))
  if(latency or packetLoss != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc qdisc add dev enp5s0f0 root netem delay " + str(latency) + "ms"])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper enp5s0f0 " + str(upload) + " " + str(download)])

def restoreNetwork(time, ip, latency, download, upload, packetLoss):
  print("restoreNetwork:" + str(time))
  if(latency or packetLoss != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc qdisc del dev enp5s0f0 root netem"])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper clear enp5s0f0"])



def startScenario():
  print(time.time())
  ${scenario}
  s.run()

startScenario()
`
      fs.writeFileSync(scenariosDirectory + "/" + (dirs.length + 1).toString() + "/scenario.py", data)
      let filePath = scenariosDirectory + "/" + (dirs.length + 1).toString();
      shell.cp('./scenariosTpl/wallets.json', filePath + "/wallets.json")
      shell.cp('./scenariosTpl/ips.json', filePath + "/ips.json")
      shell.cp('./scenariosTpl/postProcess.js', filePath + "/postProcess.js")
      shell.cp('./scenariosTpl/process.js', filePath + "/process.js")

      req.body.events.forEach(async (event, index) => {
        if(event.type === 0) {
          let nbTx = event.nbTx / req.body.wallets.length;
          let timeBetween2Tx = Math.trunc(100 / (nbTx / 10))
          shell.mkdir(filePath + "/" + index);
          let txArray = await genTransactionsArray(
            nbTx, 
            timeBetween2Tx,
            event.during,
            dirs.length + 1
          )
          req.body.wallets.forEach(async (el, it) => {
            // var arrayFiles = JSON.stringify(txArray[el.signingKey.address])
            var rawTxArray = [];
            for (let i = 0; i < txArray[el.signingKey.address].txs.length; i++) {
              rawTxArray.push(
                new Promise (async (resolve, reject) => {
                  let signer = new ethers.Wallet(txArray[el.signingKey.address].privKey);
                  let raw = await signer.signTransaction({...txArray[el.signingKey.address].txs[i], 'gasPrice': 0, 'gasLimit': 21000});
                  resolve(raw.toString());
              }))
            }
            Promise.all(rawTxArray).then(resolved => {
              fs.writeFileSync(filePath + '/' + index + '/' + el.signingKey.address + '.json', JSON.stringify(resolved.slice(',')));
            });
          });
        }
      });
    })
  }).then(() => {
    res.send(JSON.stringify({type: "success", msg:"Scenario preparation generated"}));
  })
});

module.exports = router;
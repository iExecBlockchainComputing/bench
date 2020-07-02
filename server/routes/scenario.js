var express = require('express');
var router = express.Router();
var fs = require('fs');
var fsPromise = require('fs').promises;
var path = require('path');
var shell = require('shelljs');
const { schedulingPolicy } = require('cluster');

var scenariosDirectory = "./scenarios";

function txPerSecTpl(time, priority, nbTx, timeBetween) {
  return `
  # ${nbTx} Tx spaced by ${timeBetween} at ${time}
  s.enter(${time}, ${priority}, txPerSec, argument=(${timeBetween}, ${time}))`
}

function killNodeTpl(time, priority, nbNodes, bootnode, moc, validators, timeBeforeReUp) {
  return `
  #Kill ${nbNodes} Nodes at ${time} and reUp at ${timeBeforeReUp}
  s.enter(${time}, ${priority}, killNodes, argument=(${nbNodes}, ${bootnode}, ${moc}, ${validators}, ${time} ))
  s.enter(${time + timeBeforeReUp}, ${priority}, reUpNodes, argument=(${time},))`
}

function genTransactionsArray(nbTx, scenarioNumber, time) {
  return new Promise((resolved) => {
    let tx = [];
    fsPromise.readFile(scenariosDirectory + "/" + scenarioNumber + "/wallets.json", (err) => {
      if (err) throw err;
    })
    .then(data => JSON.parse(data.toString()))
    .then((wallets) => {
      for (let i = 0; i < nbTx; i++) {
        tx.push({
          'to': wallets[i%wallets.length].address,
          'value': "0x0",
          'nonce': wallets[i%wallets.length].nonce
        })
        wallets[i%wallets.length].nonce = wallets[i%wallets.length].nonce + 1;
      }
    })
    .then(() => resolved(tx))
  })
}

router.post('/genScenario', function (req, res) {
  var events = [];
  var scenario = "";
  req.body.events.forEach(event => {
    switch (event.type) {
      case 0:
        events.push(txPerSecTpl(
          event.time,
          event.priority,
          event.nbTx,
          event.timeBetween2Tx
        ));
        break;
      case 1:
        events.push(killNodeTpl(
          event.time,
          event.priority,
          event.nbNodes,
          event.bootnode,
          event.moc,
          event.validators,
          event.timeBeforeReUp
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
from subprocess import call

s = sched.scheduler(time.time, time.sleep)

def printTime(a='default'):
  print("From print_time", time.time(), a)

def txPerSec(timeBetween, time):
  print("txPerSec: " + str(time))
  call(["node", "./txPerSec.js", str(time), str(timeBetween)])

def killNodes(nbNodes, bootnode, moc, validators, time):
  print("KillNodes")

def reUpNodes(time):
  print("reUpNodes")

def startScenario():
  print(time.time())
  ${scenario}
  print(time.time())
  s.run()

startScenario()
`
      fsPromise.writeFile(scenariosDirectory + "/" + (dirs.length + 1).toString() + "/scenario.py", data)
      
      let filePath = scenariosDirectory + "/" + (dirs.length + 1).toString();
      shell.cp('./scenariosTpl/wallets.json', filePath + "/wallets.json")
      shell.cp('./scenariosTpl/ips.json', filePath + "/ips.json")
      shell.cp('./scenariosTpl/txPerSec.js', filePath + "/txPerSec.js")
      req.body.events.forEach(event => {
        if(event.type === 0) {
          genTransactionsArray(
            event.nbTx, 
            dirs.length + 1,
            event.time
          ).then(resolved => {
            if(fs.existsSync(filePath + "/transactions.json")) {
              fsPromise.readFile(filePath + "/transactions.json", (err) => {
                if (err) throw err;
              })
              .then(data => {
                data = JSON.parse(data.toString());
                data[event.time] = {...data[event.time], 'interval': event.timeBetween2Tx, 'txs': resolved};
                fsPromise.writeFile(filePath + "/transactions.json", JSON.stringify(data), (err2) => {
                  if (err2) throw err2;
                });
              });
            } else {
              let base = {};
              base[event.time] = {'interval': event.timeBetween2Tx, 'txs': resolved};
              fsPromise.writeFile(filePath + "/transactions.json", JSON.stringify(base), (err2) => {
                if (err2) throw err2;
              });
            }
          })
        }
      });
    })
  })
  .then(() => {
    res.send(JSON.stringify({type: "success", msg:"Scenario preparation generated"}));
  })
});

module.exports = router;
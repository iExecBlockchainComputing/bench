var express = require('express');
var router = express.Router();
var fs = require('fs');
var fsPromise = require('fs').promises;
var path = require('path');
var async = require('async');
var shell = require('shelljs');
var yml = require('yaml');

var scenariosDirectory = "./scenarios";

function txPerSecTpl(time, priority, nbTx, timeBetween) {
  return `
  # ${nbTx} Tx spaced by ${timeBetween} at ${time}
  s.enter(${time}, ${priority}, txPerSec(${nbTx}, ${timeBetween}))`
}

function killNodeTpl(time, priority, nbNodes, bootnode, moc, validators, timeBeforeReUp) {
  return `
  #Kill ${nbNodes} Nodes at ${time} and reUp at ${timeBeforeReUp}
  s.enter(${time}, ${priority}, killNodes(${nbNodes}, ${bootnode}, ${moc}, ${validators} ))
  s.enter(${time+timeBeforeReUp}, ${priority}, reUpNodes())`
}

router.post('/genScenario', function(req, res) {
  var getNbDirectories = "";
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
    events.forEach(event => {
      scenario = scenario + `${event}
      `
    });
  });
  fsPromise.readdir(scenariosDirectory, (err, dirs) => {
    if(err) throw err;
  }).then((dirs) => {
    fsPromise.mkdir(path.join(scenariosDirectory,  (dirs.length + 1).toString()), (err) => {
      if(err) throw err;
    }).then(() => {
      var data = 
`import sched, time, json

s = sched.scheduler(time.time, time.sleep)

def printTime(a='default'):
  print("From print_time", time.time(), a)

def txPerSec(nbTx, timeBetween):
  print("txPerSec")

def killNodes(nbNodes, typeOfNodes):
  print("KillNodes")

def reUpNodes():
  print("reUpNodes")

def startScenario():
  print(time.time())
  ${scenario}
  print(time.time())
  s.run()

startScenario()
`
      fsPromise.writeFile(scenariosDirectory + "/" + (dirs.length + 1).toString() + "/scenario.py", data)
    })
  })

});

module.exports = router;

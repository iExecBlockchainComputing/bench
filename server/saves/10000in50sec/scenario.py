import sched, time, json
from subprocess import call

s = sched.scheduler(time.time, time.sleep)

def printTime(a='default'):
  print("From print_time", time.time(), a)

def genTx(time):
  print("gen: " + str(time))
  call(["node", "./gen.js", str(time)])

def txPerSec(timeBetween, time):
  print("txPerSec: " + str(time))
  call(["node", "./txPerSec.js", str(time), str(timeBetween)])

def getResultTx(time):
  print("getResultsTx: " + str(time))
  call(["node", "./postProcess.js", str(time)])

def killNodes(nbNodes, bootnode, moc, validators, time):
  print("KillNodes")

def reUpNodes(time):
  print("reUpNodes")

def startScenario():
  print(time.time())
  
  # generating Txs for 5
  s.enter(1, 1, genTx, argument=(5,))

  # 10000 Tx spaced by 5 at 5
  s.enter(5, 1, txPerSec, argument=(5, 5))

  # Gettin results of Txs form 5
  s.enter(120, 1, getResultTx, argument=(5,))

  s.run()

startScenario()

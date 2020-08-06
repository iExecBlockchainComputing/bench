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
  
  # generating Txs for 10
  s.enter(1, 1, genTx, argument=(10,))

  # 4000 Tx spaced by 1 at 10
  s.enter(10, 1, txPerSec, argument=(1, 10))

  # Gettin results of Txs form 10
  s.enter(20, 1, getResultTx, argument=(10,))

  print(time.time())
  s.run()

startScenario()

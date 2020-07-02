import sched, time, json
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
  
  # 2000 Tx spaced by 5 at 1000
  s.enter(1, 1, txPerSec, argument=(5, 1000))

  print(time.time())
  s.run()

startScenario()

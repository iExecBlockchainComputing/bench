import sched, time, json
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

def networkDegrade(time, ip, latency, download, upload):
  print("networkDegrade:" + str(time))
  if(latency or packetLoss != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc qdisc add dev enp5s0f0 root netem delay" + str(latency) + "ms"])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper enp5s0f0" + str(upload) + " " + str(download)])

def restoreNetwork(time, ip, latency, download, upload):
  print("restoreNetwork:" + str(time))
  if(latency or packetLoss != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc qdisc del dev enp5s0f0 root netem"])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper clear enp5s0f0"])

tc qdisc add dev enp5s0f0 root netem delay
def startScenario():
  print(time.time())
  
  #Degrating nova-3.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-3.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-3.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-4.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-4.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-5.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-5.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-6.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-6.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-7.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-7.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-8.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-8.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-9.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-9.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-10.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-10.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-10.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-11.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-11.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-12.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-12.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-13.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-13.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-14.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-14.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-15.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-15.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-16.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-16.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-17.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-17.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-18.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-18.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-19.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-19.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-20.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-20.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-21.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-21.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-22.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-22.lyon.grid5000.fr", "100", "", ", "))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-23.lyon.grid5000.fr", "100", "", ", "))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-23.lyon.grid5000.fr", "100", "", ", "))
  

  #Degrating nova-3.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-3.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-3.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-4.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-4.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-5.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-5.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-6.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-6.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-7.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-7.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-8.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-8.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-9.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-9.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-10.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-10.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-10.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-11.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-11.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-12.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-12.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-13.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-13.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-14.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-14.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-15.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-15.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-16.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-16.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-17.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-17.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-18.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-18.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-19.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-19.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-20.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-20.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-21.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-21.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-22.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-22.lyon.grid5000.fr", "200", "", ", "))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-23.lyon.grid5000.fr", "200", "", ", "))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-23.lyon.grid5000.fr", "200", "", ", "))
  

  #Degrating nova-3.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-3.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-3.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-4.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-4.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-5.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-5.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-6.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-6.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-7.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-7.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-8.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-8.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-9.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-9.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-10.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-10.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-10.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-11.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-11.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-12.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-12.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-13.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-13.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-14.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-14.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-15.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-15.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-16.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-16.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-17.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-17.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-18.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-18.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-19.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-19.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-20.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-20.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-21.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-21.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-22.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-22.lyon.grid5000.fr", "300", "", ", "))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-23.lyon.grid5000.fr", "300", "", ", "))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-23.lyon.grid5000.fr", "300", "", ", "))
  

  #Degrating nova-3.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-3.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-3.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-4.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-4.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-5.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-5.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-6.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-6.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-7.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-7.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-8.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-8.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-9.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-9.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-10.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-10.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-10.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-11.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-11.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-12.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-12.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-13.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-13.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-14.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-14.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-15.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-15.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-16.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-16.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-17.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-17.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-18.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-18.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-19.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-19.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-20.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-20.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-21.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-21.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-22.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-22.lyon.grid5000.fr", "400", "", ", "))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-23.lyon.grid5000.fr", "400", "", ", "))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-23.lyon.grid5000.fr", "400", "", ", "))
  

  #Degrating nova-3.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-3.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-3.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-4.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-4.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-5.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-5.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-6.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-6.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-7.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-7.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-8.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-8.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-9.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-9.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-10.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-10.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-10.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-11.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-11.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-12.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-12.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-13.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-13.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-14.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-14.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-15.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-15.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-16.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-16.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-17.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-17.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-18.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-18.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-19.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-19.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-20.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-20.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-21.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-21.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-22.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-22.lyon.grid5000.fr", "500", "", ", "))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-23.lyon.grid5000.fr", "500", "", ", "))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-23.lyon.grid5000.fr", "500", "", ", "))
  

  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xD7890C0fD47644D25D11e7B32237bE6E966F11e0.json", 0, "nova-1.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x3F70CDeE8fc4A5Ad99daa763E7e44B27DE95211b.json", 0, "nova-3.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xF6CDb43254f5c50C309BF849cE1C7aCE93C90845.json", 0, "nova-4.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x438af89Dc89D267d27cc5994868853EB5686eA92.json", 0, "nova-5.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xE08ba7d70F267218de518CFe602CAe918e8Da545.json", 0, "nova-6.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x4fBA754A791dF438cd168Da47C9668d5769f36C4.json", 0, "nova-7.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x68e182836D229fBb9323d18B4a9B2AbCA26dFf57.json", 0, "nova-8.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x756444413a5EC1242D845c9C2E32A9Ac4Ca6132c.json", 0, "nova-9.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x8496D7d116349f05E9eD789A7a6C887E82409D6e.json", 0, "nova-10.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xbbB24b878F5e973F3cD6627AfBC12438EF370170.json", 0, "nova-11.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x7e72466D358708Bcdfd0288EA74fb9E3c39494Fb.json", 0, "nova-12.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x3fb45BF131366b6c6197781F8435036CC9979639.json", 0, "nova-13.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x47EBdA5faf6716aD5C0E6a868568933BD82673f0.json", 0, "nova-14.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xB4430C0C32Cb6Ed015F26Ad68C12EE8935aB3CEB.json", 0, "nova-15.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x8a1fcc8912A24C38d2298bB0cC9b864cCeA56fEB.json", 0, "nova-16.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x04f1aa61b3ce3B683e423335d5DC400111D5D1c3.json", 0, "nova-17.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x14D11Cf15d2C06528C53406Df4383527f27687Eb.json", 0, "nova-18.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x63C351C3f47F7ac02C953e1Af96FD367388bC72A.json", 0, "nova-19.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x83E96C0eD1dD09d64F18cC2B26842373FaC215e9.json", 0, "nova-20.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x10Ee22c816BAEc8977a9492e242cB019867E7dD4.json", 0, "nova-21.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x654F27123D504bAC0C077b30083A9E61C6334219.json", 0, "nova-22.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xF30a8f73db40EfE284fCD8713D3095cE4de26c33.json", 0, "nova-23.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x6CbA2d65a4b83cb8D683392B1A036A5713c373E2.json", 0, "nova-1.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xaF259DEe20442554055C3975B8C94f06121A187c.json", 0, "nova-3.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xB507e70cA01CC27466fdF9Eb634c17A8727a5F90.json", 0, "nova-4.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x38502E2cE8188667494c5b7F540c8A455d9A3a58.json", 0, "nova-5.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xc6F82a82928e262775139b7a6B8FBC84A8B285Bc.json", 0, "nova-6.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x254A9F4fA444f0323AE40d7e9a592Ab6bf37112F.json", 0, "nova-7.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x145C8e1fA2cA9123B3F1C2F660b50f2042b1e66d.json", 0, "nova-8.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xC00d50d0Fd0F5ea274220D0F983F89e5545b9906.json", 0, "nova-9.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xF846800Fc42B2593875921871404EAa7D8F50de9.json", 0, "nova-10.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x524557E8a8d7D1FB88471585103FCE889f5CaEE4.json", 0, "nova-11.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x6F83Fd5d0aF5bF11Bf28Fe7d327BB2010a2e94ed.json", 0, "nova-12.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x7b548E77e3e18FD6958dD9F3Db5795828E21a837.json", 0, "nova-13.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xFD8D1b939538A935f1CeBd425107D9056d86D9d0.json", 0, "nova-14.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x4bd18d685856DE640480b9902c09a84C0dc36ed5.json", 0, "nova-15.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xe74FBaFcdf652dc11576ff3cE45061AeDf098D9D.json", 0, "nova-16.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x3763f5b78E0466F58Ade190Ff419AaBEF78EA9f1.json", 0, "nova-17.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x5dcad0c1A0646d296C0a7506B94f94070E66eFf0.json", 0, "nova-18.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x52366BC763EBd3BFdfAa6603edeecEFd1ed5eB7E.json", 0, "nova-19.lyon.grid5000.fr"))
  

  s.run()

startScenario()

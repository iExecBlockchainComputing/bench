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
  
  #Degrating nova-10.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-10.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-10.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-11.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-11.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-12.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-12.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-13.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-13.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-14.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-14.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-15.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-15.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-16.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-16.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-17.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-17.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-18.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-18.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-19.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-19.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-20.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-20.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-21.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-21.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-22.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-22.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-23.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-23.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-3.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-3.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-3.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-4.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-4.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-5.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-5.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-6.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-6.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-7.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-7.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-8.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-8.lyon.grid5000.fr", "", "1024", "1024", ""))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 11 and restore at 110
  s.enter(11, 1, networkDegrade, argument=(11, "nova-9.lyon.grid5000.fr", "", "1024", "1024", ""))
  s.enter(110, 1, restoreNetwork, argument=(11, "nova-9.lyon.grid5000.fr", "", "1024", "1024", ""))
  

  #Degrating nova-10.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-10.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-10.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-11.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-11.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-12.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-12.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-13.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-13.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-14.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-14.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-15.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-15.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-16.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-16.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-17.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-17.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-18.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-18.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-19.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-19.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-20.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-20.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-21.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-21.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-22.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-22.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-23.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-23.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-3.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-3.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-3.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-4.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-4.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-5.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-5.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-6.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-6.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-7.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-7.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-8.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-8.lyon.grid5000.fr", "", "512", "512", ""))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 111 and restore at 210
  s.enter(111, 1, networkDegrade, argument=(111, "nova-9.lyon.grid5000.fr", "", "512", "512", ""))
  s.enter(210, 1, restoreNetwork, argument=(111, "nova-9.lyon.grid5000.fr", "", "512", "512", ""))
  

  #Degrating nova-10.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-10.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-10.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-11.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-11.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-12.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-12.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-13.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-13.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-14.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-14.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-15.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-15.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-16.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-16.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-17.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-17.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-18.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-18.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-19.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-19.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-20.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-20.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-21.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-21.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-22.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-22.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-23.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-23.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-3.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-3.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-3.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-4.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-4.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-5.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-5.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-6.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-6.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-7.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-7.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-8.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-8.lyon.grid5000.fr", "", "256", "256", ""))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 211 and restore at 310
  s.enter(211, 1, networkDegrade, argument=(211, "nova-9.lyon.grid5000.fr", "", "256", "256", ""))
  s.enter(310, 1, restoreNetwork, argument=(211, "nova-9.lyon.grid5000.fr", "", "256", "256", ""))
  

  #Degrating nova-10.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-10.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-10.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-11.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-11.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-12.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-12.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-13.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-13.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-14.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-14.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-15.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-15.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-16.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-16.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-17.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-17.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-18.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-18.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-19.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-19.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-20.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-20.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-21.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-21.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-22.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-22.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-23.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-23.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-3.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-3.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-3.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-4.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-4.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-5.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-5.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-6.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-6.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-7.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-7.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-8.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-8.lyon.grid5000.fr", "", "128", "128", ""))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 311 and restore at 410
  s.enter(311, 1, networkDegrade, argument=(311, "nova-9.lyon.grid5000.fr", "", "128", "128", ""))
  s.enter(410, 1, restoreNetwork, argument=(311, "nova-9.lyon.grid5000.fr", "", "128", "128", ""))
  

  #Degrating nova-10.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-10.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-10.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-11.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-11.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-11.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-12.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-12.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-12.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-13.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-13.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-13.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-14.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-14.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-14.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-15.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-15.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-15.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-16.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-16.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-16.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-17.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-17.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-17.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-18.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-18.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-18.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-19.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-19.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-19.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-20.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-20.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-20.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-21.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-21.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-21.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-22.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-22.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-22.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-23.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-23.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-23.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-3.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-3.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-3.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-4.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-4.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-4.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-5.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-5.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-5.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-6.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-6.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-6.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-7.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-7.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-7.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-8.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-8.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-8.lyon.grid5000.fr", "", "64", "64", ""))
  
  #Degrating nova-9.lyon.grid5000.fr Network at 411 and restore at 510
  s.enter(411, 1, networkDegrade, argument=(411, "nova-9.lyon.grid5000.fr", "", "64", "64", ""))
  s.enter(510, 1, restoreNetwork, argument=(411, "nova-9.lyon.grid5000.fr", "", "64", "64", ""))
  

  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xd701c89BD35263Be3D555ae7B0C94d6c792aC93a.json", 0, "nova-1.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xB5Ed33fa7Cc73529e019B410582A3eF19fd102a6.json", 0, "nova-10.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xfc7545B873ccAE32942391a0226c3A3B3De382D0.json", 0, "nova-11.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x0541d32995BC79CD370dA6F2Ee5cE4184a63bb81.json", 0, "nova-12.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x6802a57bDE94B2004474941dBa65fF64023b480A.json", 0, "nova-13.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x131F1e261fD7eA86f2FF9eB733A4a68680DF76eF.json", 0, "nova-14.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x3A18A214Cc62748E6ae485FDe3f09B83C46adc73.json", 0, "nova-15.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xD427910d036310Ee5213A37f12bBD59c13a041F2.json", 0, "nova-16.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xdF9c8643E6291596976FBF146740F282b6c291e3.json", 0, "nova-17.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x0AB1E465cFD1444Cd0DC01bb40086716Ecb561A4.json", 0, "nova-18.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xad36aBB1B38D6edf420fEb7cf04F2D4BEE6aD374.json", 0, "nova-19.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xc16402aCF178a121ec59dBB74615a318f240a7cb.json", 0, "nova-20.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x35b965b2b360E0f89756a3A8A9E2F5c77723aE5d.json", 0, "nova-21.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xEb1D1AB83D652e99cE950652c6d87480C4BD025E.json", 0, "nova-22.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x72f47ab7e506ca1A220dBEBb10046721298B9866.json", 0, "nova-23.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x8807c95Aae42aa304716233cD4d77D3FD9b5D602.json", 0, "nova-3.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x49A2163E7bf6F5e3c344872a83147Db34C45B4Af.json", 0, "nova-4.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x19Ad9263C9B1F66dCf23ddAa6f3F555e3E268e6e.json", 0, "nova-5.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xe998F7cdCf274b46c8e86A5642Db32eB19056A0e.json", 0, "nova-6.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x7Ec447e500B5c9D3Ad376Be0bdF824A7E65E70ee.json", 0, "nova-7.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xc6e5832016e806F33cc183B2221e88d2A92d6478.json", 0, "nova-8.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xd11899e85e78563445465AA595a69362d2D0ac8f.json", 0, "nova-9.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xAeDBF908748d867134c08aaE211974c87067BA8b.json", 0, "nova-1.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x0789e07bb23b5A2C3de5864440d5A3FEd09f2e07.json", 0, "nova-10.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x947f57309EC7Ce2f293a9dCA8e3b760de2d822A3.json", 0, "nova-11.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x46CCb227915c803B253368cA9ae375d60b992702.json", 0, "nova-12.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x12E70376Bf598b619E0561278f67193bc5eC39C9.json", 0, "nova-13.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0xa7e9873B83055824B614341C88323d84F1E520a8.json", 0, "nova-14.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x5Ef2A706b57cAFDe9C153eF5e6A0a86B91083634.json", 0, "nova-15.lyon.grid5000.fr"))
  
  # 64 Tx spaced by 468 at 10
  s.enter(10, 1, process, argument=(468, "0x4886D6eCECb99AB8F571177192f55d411c1E1804.json", 0, "nova-16.lyon.grid5000.fr"))
  

  s.run()

startScenario()

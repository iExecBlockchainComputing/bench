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
  if(latency != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc", "qdisc", "add", "dev", "enp68s0f0", "root", "netem", "delay", latency])
  if(download or upload != "")
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper", "enp68s0f0", upload, download])

def restoreNetwork(time, ip, latency, download, upload):
  print("restoreNetwork:" + str(time))
  if(latency != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc", "qdisc", "del", "dev", "enp68s0f0", "root", "netem"])
  if(download or upload != "")
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper", "clear", "enp68s0f0"])


def startScenario():
  print(time.time())
  
  #Degrating taurus-12.lyon.grid5000.fr Network at 20 and restore at 100
  s.enter(20, 1, networkDegrade, argument=(20, "taurus-12.lyon.grid5000.fr", "100", "1024", "1024"))
  s.enter(100, 1, restoreNetwork, argument=(20, "taurus-12.lyon.grid5000.fr", "100", "1024", "1024"))

  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0xAa772F66bb698Fbd0e5417145024F857a2a7141F.json", 0, "taurus-3.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x17B5A3B0fbdbBDB542fF0D604f0B97815336A20A.json", 0, "taurus-12.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x6483bD07F17EDfF52d01DAec602abc86997fFB82.json", 0, "taurus-3.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x68C86fafa1F9D8890c59BEB112cdE4E7BB7E50d3.json", 0, "taurus-12.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x4c71019c40dFD8697033Dd6DE503C19f66Bf884f.json", 0, "taurus-3.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x6a9B62529E535DD492cA63305aAD9a5edffb6446.json", 0, "taurus-12.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x1f24eA8dEB31C6adB24AE9b0eeC7A8b8D4277c2c.json", 0, "taurus-3.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0xe9d2d20DAf69E6BBFc37264e67058ca250a0260D.json", 0, "taurus-12.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x07E68a8c4CA2E53D8094e7226aed275d296c256C.json", 0, "taurus-3.lyon.grid5000.fr"))
  
  # 67 Tx spaced by 149 at 10
  s.enter(10, 1, process, argument=(149, "0x3F5aDEB3F98b1Ac3667841E1160c13C62D1bda3d.json", 0, "taurus-12.lyon.grid5000.fr"))
  

  s.run()

startScenario()

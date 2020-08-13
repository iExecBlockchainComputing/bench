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
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc", "qdisc", "add", "dev", "enp68s0f0", "root", "netem", "delay", str(latency)])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper", "enp68s0f0", str(upload), str(download)])

def restoreNetwork(time, ip, latency, download, upload):
  print("restoreNetwork:" + str(time))
  if(latency != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc", "qdisc", "del", "dev", "enp68s0f0", "root", "netem"])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper", "clear", "enp68s0f0"])


def startScenario():
  print(time.time())
  
  #Killing gros-70.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-70.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-70.nancy.grid5000.fr"))
  #Killing gros-71.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-71.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-71.nancy.grid5000.fr"))
  #Killing gros-72.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-72.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-72.nancy.grid5000.fr"))
  #Killing gros-73.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-73.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-73.nancy.grid5000.fr"))
  #Killing gros-74.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-74.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-74.nancy.grid5000.fr"))
  #Killing gros-75.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-75.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-75.nancy.grid5000.fr"))
  #Killing gros-76.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-76.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-76.nancy.grid5000.fr"))
  #Killing gros-77.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-77.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-77.nancy.grid5000.fr"))
  #Killing gros-78.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-78.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-78.nancy.grid5000.fr"))
  #Killing gros-79.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-79.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-79.nancy.grid5000.fr"))
  #Killing gros-80.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-80.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-80.nancy.grid5000.fr"))
  #Killing gros-81.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-81.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-81.nancy.grid5000.fr"))
  #Killing gros-82.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-82.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-82.nancy.grid5000.fr"))
  #Killing gros-83.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-83.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-83.nancy.grid5000.fr"))
  #Killing gros-84.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-84.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-84.nancy.grid5000.fr"))
  #Killing gros-85.nancy.grid5000.fr at 300 and reUp at 500
  s.enter(300, 1, killNodes, argument=(300, "gros-85.nancy.grid5000.fr"))
  s.enter(500, 1, reUpNodes, argument=(300, "gros-85.nancy.grid5000.fr"))

  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe0a1E355612CEcAAe59589cE10cF4059da592C80.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe2F797b58D8FC961F26E77c8b06a0C281234eae1.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x9d0b7b958c891ED5eCaa705E62cC96A099180Ed7.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x6E9D8CAB08e9ccaeeDbe905D99444b5e2862Ee86.json", 0, "gros-98.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xedA4f14155B156280398165c0403B46635E67d10.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe16fBE273433777780d28078a5088997e6cCFFd5.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xCb131f261FC15cA1b46880E69033565aB6b90B1E.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xd5F435f942681D0740de7E128586BC21d6cA1A74.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb0b846cEcbAAE9B37254849C8923fb6995EDc280.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xDfb856C9e68A6e55308a271CCf72d4e82F0F73b5.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x5FaB538e612494d99fb861478F766463e146Bbf1.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xa19e5B1694D1da1F095100ADE9810d470df76E3c.json", 0, "gros-90.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf3484D275E06AA0c68e9c062A5aFCA97FA56f52c.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x6973462893067a2124fc1F7B10B8538A5451AfFD.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x27Db556D36529e6282b2B174a13772D42fa8D57F.json", 0, "gros-87.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xDB3dfD8Ab5dE8897B547B7C04c7b870F80Db0C43.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x429745fb2Bf3Ef4839e91013dD2b42c951c1476e.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xc712605e9386536464A1B002d206B28176FC1626.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xFCC0045938763048FF7fB879B5d61e3ef4498B75.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x6279f59b04F36a119Fa853086Ba5698D4634D31A.json", 0, "gros-98.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe5d84ec1F25b575B076440bD6195635C52d564d1.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x94dD0bC77A0B00F513247a593018cF3495B10786.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x40589A8699b6Cdb75a165F15A672767526b05606.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x8F1D7ef6eB117fA49d824319D2CeE11d3D0AeD64.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x306C0C49C580613C81e27B0F0d0DfaB36feF086D.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x48B7B3fEa63B9e0636F7c917Dd5f4C57955EB03c.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xC2cCF8Ee9F8f16D5ab7f680513C1F88dA39922aC.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x91BD9E3a17f7562819E544648282d57588143D1E.json", 0, "gros-90.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x5f90CCEE588610ee7E4fd0c2846DAAfd2f57b678.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xC45c6a5E9b88b667c482cd5bd1B3C59e3af2fFf6.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x3C825f2aF1a1803B277BC8b47B65a38C502390A1.json", 0, "gros-87.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x50bf669E9e39D30F80f635602e24E2678F39DaC4.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x3430385cf450440e5E5b30750EA4f5E1Fafbb409.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x7Fc357912c0a65735D867D2BE093AB8bfCc57835.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x4F03fc0514a669BcCB0Eeb84cea54Da84e5066a2.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x3C15A787b46ACF21180df1d23c16d9C804516B9F.json", 0, "gros-98.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x19A027E09E03e04dCe85Dc553DA08b9F2E93C6fe.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x149Fc8216A700f90B71548A31bD2B2DB3607E0b6.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x416dF95ad8cCEceab36967569De627a546Ebb0EA.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xB380f0EB97a61F6217940CC12DD7A610387eCedE.json", 0, "gros-94.nancy.grid5000.fr"))
  

  s.run()

startScenario()

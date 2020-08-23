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
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc", "qdisc", "add", "dev", "enp68s0f0", "root", "netem", "delay", str(latency)])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper", "enp68s0f0", str(upload), str(download)])

def restoreNetwork(time, ip, latency, download, upload):
  print("restoreNetwork:" + str(time))
  if(latency or packetLoss != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "tc", "qdisc", "del", "dev", "enp68s0f0", "root", "netem"])
  if(download or upload != ""):
    subprocess.Popen(["ssh", "-i", "~/.ssh/bench", "root@" + ip, "wondershaper", "clear", "enp68s0f0"])


def startScenario():
  print(time.time())
  
  #Killing gros-8.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-8.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-8.nancy.grid5000.fr"))
  #Killing gros-52.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-52.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-52.nancy.grid5000.fr"))
  #Killing gros-53.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-53.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-53.nancy.grid5000.fr"))
  #Killing gros-54.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-54.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-54.nancy.grid5000.fr"))
  #Killing gros-55.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-55.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-55.nancy.grid5000.fr"))
  #Killing gros-56.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-56.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-56.nancy.grid5000.fr"))
  #Killing gros-57.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-57.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-57.nancy.grid5000.fr"))
  #Killing gros-58.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-58.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-58.nancy.grid5000.fr"))
  #Killing gros-59.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-59.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-59.nancy.grid5000.fr"))
  #Killing gros-60.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-60.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-60.nancy.grid5000.fr"))
  #Killing gros-61.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-61.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-61.nancy.grid5000.fr"))
  #Killing gros-62.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-62.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-62.nancy.grid5000.fr"))
  #Killing gros-63.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-63.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-63.nancy.grid5000.fr"))
  #Killing gros-64.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-64.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-64.nancy.grid5000.fr"))
  #Killing gros-65.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-65.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-65.nancy.grid5000.fr"))
  #Killing gros-66.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-66.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-66.nancy.grid5000.fr"))

  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x088F8CAb642b6b305f1f65c52B69d151FB0E381c.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb7cC895e9cE3e1E658e9d28Bd21A2B5079B748b3.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x16a79E4A5261FeD38590D772Cb2c915d0c210D2e.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x991004a90e971A1cCFc8CAf6f2d47cEb9995C1c9.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x5DF3cA30941A84461108E30Bc9d57001C96FA428.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xEdCb2836c6e46171219A4D7A42A7ecd8A0b181fC.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe99306f71EDABC430050aFeE19FF8523cD4c84E4.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xB1EC41F4afc90d1cA9d8673F1ACa952B9Eb16eC8.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf884c68ffF955E793ec8121e5A1166026089e6e1.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xc11ac35e20404A1F4Ad7b8934227A15bfAD9F3Cb.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x23889baa09De86B680C3E00A49A6b9791ef94091.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x8138a0127E9Ec286e2486Cc6258287a384193E49.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x595FbA2d3075723a962385eAC5F9B9D35F2C9148.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf6D3BCaDE1102043d1412CAa291608512824fAe0.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb24BF5Cd33f2c55Fd3Bdb5556819468b0dcaef73.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xbBBc6F734576b96E7E3596369976a3505ab45eAe.json", 0, "gros-67.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x5562742E46b43afB66eCc11007ED65616a0bad79.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x7e24CC9Ca28FbA4EBFE0496053616769525cDDB8.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x733e77DC24e2abd44011466163935C5dC88556eC.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb51369F8c230457f1e0AEb2B998037fB875febe1.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x9bB6E372a9C0Cc11799064D8290B9e5459a7384B.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x989948CEc6cF3ce68A96052A7246A820473C1bD3.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb7c2Cc8cF26C01C499BaA20949Cc3c52e4690A6B.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xB61Fa712658b093f2a494953E1896E16a8Ee90C9.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb1BA558A9867dEdf1D30dD9b3F3DA6f2C872e28b.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x3922Bad4C6e2C279530306A1bE4A2d7141c95A52.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf628d4D4935b899D644644a3C18f02f62A9ee468.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x6682F7573573f88445AaFA42Fe4a9c01e5dd7b73.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x9EFf27d6fBdE27E52367c156B2E8909641FC21f6.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x771f5111fD85456D7a7B31DEb05bb4Dd22B14F47.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xE282EA175384726f1a37BA613b42F210402bAA7c.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xF11b4B7D9268f19a9A591330abB19647e476b5aD.json", 0, "gros-67.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x603b440752b11d077ceC4e17226b0e439e69CBb1.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x928DA869B15B806f55E08f79acE947f0480264Af.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe41a003Ab87D829DB547763eFcB5f71008b5fB00.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x8a0e2de29a2523Eff239bF659ab1316bB7C9d7A6.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xc5d5f85a74Eec275A64669d8b0C4B3d675a83360.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe3CC00cdD06486E4EDbD5E31bFa87f15AC969602.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x15e1465075a37a26880B865B22639DbaE33C3617.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x682777A4dcdE6abe3E78dFed17E471AdC23424D0.json", 0, "gros-75.nancy.grid5000.fr"))
  

  s.run()

startScenario()

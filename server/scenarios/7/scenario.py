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
  #Killing gros-6.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-6.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-6.nancy.grid5000.fr"))
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
  #Killing gros-67.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-67.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-67.nancy.grid5000.fr"))
  #Killing gros-68.nancy.grid5000.fr at 60 and reUp at 200
  s.enter(60, 1, killNodes, argument=(60, "gros-68.nancy.grid5000.fr"))
  s.enter(200, 1, reUpNodes, argument=(60, "gros-68.nancy.grid5000.fr"))

  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x75CFa37eD284F1E2c6Eb6aF893B28bE420FA441a.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x947c526c344318cEE51c69ecb77d59802Ae23926.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe9f0f8e347E31ae9E57d868e591aD90c84E3520E.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x6dD4f6eFe60fF246C961Ad0b1620808ad90E9ADD.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x33D025Ea699b9F3859D487064444e9d8Ec31Fe8F.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x728A222A48d19934A65adC26e21E204104A78264.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x93Afd9f5BeDffE8EF507F3B1F2E77934f3c21f52.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x1a5E5ab1968fdAEc52539D4643B2469E81f4351b.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xe5A4F30d9ea3355C7a87F2DEE20049a3d1405591.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb6c6991CF4E4Bfb7A4dC7824f1A09B7e3E5C099a.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x030FED86975b698E9184eD33c420d76Fb5de36b3.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x034c7D2508DDC94Bd80BA57351e31E17Cd31E1C7.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x242a9D59b7B07d12bBF9177fee269438D891D14B.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xB02843463d8D448206013EC4E0587Cd34abAA47A.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x614e3ad6ADbEC2d98f7b38F310f2a1439e6b0061.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf7edC65111cF15397edBD5e2209DC66134100284.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x118c2DF91e60D6c87b97584e66fd297e93d1a3c8.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x1Aba77cb8d23f510ea484069f03D46ce16527589.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x8Bf0B098b51dF1601407434285aD92d93a2C2d27.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xCA66c7C8F25D341fa4A316C9416540c5c4068b68.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x21e13A1856eF8574C03D4c5FCB711E55b5Ab82C3.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x42D252c04D72601bE78D558BcA9329DD368E40c3.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x8a0E0421a787133B3c881e8e0957Ec56f09508Dc.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x907325fb0A00a3C8447d7B4e7e413A99bd6211A4.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xfeA510a0687dBc98DfcCa2b4c1D242A2fD2ec9De.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x03dD0c551e0357D5f25382574c2F1c820004649C.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x95Eae37AeCb38A337F989055645C0B0baA5e9791.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xA89dfb528920e12bbc142e686d71edEF35b4d598.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x12e364453D487230663a624C321d54Fe82EE0e7f.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xF2d1903d5d9C4bf6886A9D25a539644cF9250eea.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xF9e2185a2B2495E9953C3A629F4CCD51d00E3d1A.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x33672c7a150BD6F526549B4F3aE88e141c117aD5.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xc4FeC1bc340CA2443cf6c8bAf06816fd4689Bc38.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x32cD3418E9f4a08468d81E7201B130ACc6cc4F61.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xA9549683C1E0642855d164A5487b6FB4FD6D2EF0.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x27C870Cc8Ba961e16f73536D7A82Df60B4Aa8cdF.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x907726F694F8EcA2AbCEc77305EB9ba35f9BdD34.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x0154d86c0Fe15E2920230661ae3aA0476204e588.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xd4Ff908882C8209094360BDbC98EDDDFc24e24AF.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x75Db2526Ba1b9Ec991f1b2a643F1Cd163fd8e44B.json", 0, "gros-76.nancy.grid5000.fr"))
  

  s.run()

startScenario()

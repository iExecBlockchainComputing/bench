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
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x00F4FfD2ce0cC2EdA15560C46503Ab3c2a30Eeac.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xb891582deC67fa2E0A269E4Dc62211e9A626bf64.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xE2cf3B2c23276AbDa03f724c673C0235A5377E07.json", 0, "gros-62.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xceE4a665dC8F5E89AF0fBf77478211f1B7764Be9.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x74d734ee5Ef792Aa6650B95ee48c342A38dcA5d6.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x8fBF593c604493271d0b104dB6F97E51fbF47f90.json", 0, "gros-65.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xBE1B02912944c592762B0FF57FFE3bc22Aa56745.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xf8e7540446c9fF27F66812e9d843DFEAAde16301.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x2ba1E38a19A1f09bEeeb8eEf1b68296C7E26C753.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x5C0872deB780865453c3C0F0eBC9c39DEfd3ddc1.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x5D34F5907E3ddD40cd20da2f01bd11632BD27F27.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x5Dcc2B3c028071bc9497CA951977184c00bfBdc4.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xb4635601cB26202A24952F8C09dea06B71e69693.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x1C6754b3fe8b2dec72585Be9AB01D57F35443fEc.json", 0, "gros-81.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x79E26C6EF41Aa60414B64B39809d71Ca8b3dE557.json", 0, "gros-82.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x3ac0fA7c571bDd6F893f01A85A6d1EA41C1aDe54.json", 0, "gros-83.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x8c07A11E0E998a2816cb07FCA0F024f97E6de8A9.json", 0, "gros-84.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xF5d75fC9B14D973ffeDb62bbeC82Cc9c31a74101.json", 0, "gros-85.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x712Feb193f67CC45A2c639E0CEAfb93C1d7B4f34.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xd227231fd618793B4721160C8f7e4D3ebA59Eb7C.json", 0, "gros-87.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x1Da9429644dDB1F06A852c4cD5545226EcF21241.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x8F0b2F8F2a4283c6a6075a7E7795D01929f7e259.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x29EAc1517b01634Cba1264A976bABaD8Aa864F42.json", 0, "gros-90.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x72d32024EF90f6311616005314e945F75A806b5F.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x319b3Ca0c1532F27b341456984E2A22293fa2CfD.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x96826Ae1750dD7b7C1148D2D9FB1478123536d4c.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x2E55EF76A0a60064Fe3A55Ba58765A1d6e9812Ed.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xB3E09B2Ae7880803077c2f30Cd83B8fED38597dC.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x9E7a8b03c5D16DDF0A835fb94238Ae2Cb705b999.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x6c1e04938Bb018fAE19354b45312f8570B649bFd.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xb41438E3A367eE9A0694878127aC9c4000B091Eb.json", 0, "gros-98.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x6E514139cd6345eA56cCECD319163BccbE52BD71.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x1c90A7ebbDf8C0c96F42C4B731e61F3b3728ba83.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xFC70e96E66161158D0a7Eec578Cbe1f9fbC58F51.json", 0, "gros-62.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xc890016958a0D7984df6baF9AfbC1a711A789782.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xEad1A0Be13BffE9eb519669eBa59969F0D194378.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x2fB82aCDC3a133b3d88bc1b3be69bBB4b1E49CB1.json", 0, "gros-65.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0xB9b84f64E3b2D0C123Dd21D3Bef8243dC720071b.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x392de0F0871E48A3130b8EF949Af7be2bBC5bd6A.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 64 Tx spaced by 625 at 10
  s.enter(10, 1, process, argument=(625, "0x16D6962c78FB4D660970ec113B176F66e726A99B.json", 0, "gros-76.nancy.grid5000.fr"))
  

  s.run()

startScenario()

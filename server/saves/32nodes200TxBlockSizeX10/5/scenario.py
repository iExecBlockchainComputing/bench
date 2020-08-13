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
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x6087fA2b0266AE54cFb1C06B95E4891D3C47A368.json", 0, "gros-5.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xA3F5AC26767A805Be34b90CC700fA1e282Ed904b.json", 0, "gros-40.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x14A6E7B837f0310518e0fFf5F4bB9a8e7790c7cb.json", 0, "gros-41.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x303eb064723Fe462ae7357d984CB302C353e9Fc2.json", 0, "gros-42.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x265d6DF7432b749D770975e7921E705EA8f2ec78.json", 0, "gros-43.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x5d70d1A03D067752f51fEe62833aEDFe82Ba952D.json", 0, "gros-44.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xAf326003fF31D5237c00bC0726AD341598792363.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x04ca4C60df6129d88acE2927023beC53a493C760.json", 0, "gros-46.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x8A5a53c66Dd5B56F036785907eAAd073A4c2A5cE.json", 0, "gros-47.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x82f2B9AE4961770b0Fe6d2F4513B5E415aC7F8B5.json", 0, "gros-48.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xD007F912bfe1Fc50713b51B7C8E68289F983dE60.json", 0, "gros-49.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x22fc989114E4203525Edade01096a7E521d97f1b.json", 0, "gros-50.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x58e6d3b83fd24180dfb2ca9be250ab807BDFd0FB.json", 0, "gros-51.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x0aF259fe593827c488B004966743518099dC0547.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x5aE1da5659B931B4B7A93aaDD47ED4a222103000.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x59c8d36e015a3eEe3790Ad56cA7a11B8f43057C8.json", 0, "gros-54.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x27EaBbC8304546418D088a3fa2F9018F6EaE8Ae3.json", 0, "gros-55.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x2c72EB8Ea2ada6cC5D09bfF1CCb2D0449e8d1914.json", 0, "gros-56.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xb5dCc73d01B88d1E9a1225A04b01F14A5020E5d7.json", 0, "gros-57.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x6b3E26BFB1B58Fd77C3fAbBa1d6655c00038bB47.json", 0, "gros-58.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xe8E5D219b2C397c5F87a9Ebf81d51Ad601e850de.json", 0, "gros-59.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xCE5e49B5001D17434c264ea747F226cbD10b2E2D.json", 0, "gros-60.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x7F1CDdfBb8b5968F003842f44D2441191DeC2F25.json", 0, "gros-61.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xF10289389b0E4E90da7a5878eC68F4f754779f24.json", 0, "gros-62.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xdF5c266348D42c223Ae406092d2713A7b95B0b6F.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x405325D9F60968916cd79FD5c6F07C65855386AF.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x8d6a43AEEFb2bDFc45fddcd3DD8550dA3288081a.json", 0, "gros-65.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x6036614d1e6a48A8E41d5463f930E9a3CCBE6A99.json", 0, "gros-66.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x1395Fa090eada15Ef796cfc8234f33C18A0198c0.json", 0, "gros-67.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x890c5c3d79C4d21C5133757A536114279B353067.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x55b55aBF9fE88624FE25cA76CA878F1bfA87Ce76.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x62051b9B84881341426dc871f47c7e60D829a528.json", 0, "gros-5.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xCBC3C23263b82B94F3F0815Fc062c4A35EF3b9ee.json", 0, "gros-40.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xe3CA0E67Cc7829ff76F277A319d1bAc53642eb35.json", 0, "gros-41.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0xb18cbd20e473179BFD45b4a2c81FE65dbb6ded46.json", 0, "gros-42.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x51815baBa2092d0e008a9a82111bFf9620568BAa.json", 0, "gros-43.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x1F0397CFF86eD1adA8f39B058B3a74505965120A.json", 0, "gros-44.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x65936DfB352A436Fa4fD5924F7fb80b0C751CA0a.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x39ae6f3B5B79c5EC46f66b7bAc0B1C8f1b3cf1a5.json", 0, "gros-46.nancy.grid5000.fr"))
  
  # 200 Tx spaced by 200 at 10
  s.enter(10, 1, process, argument=(200, "0x3446629D6fa0E87b20ED890b8b4de5b8c3821B4e.json", 0, "gros-47.nancy.grid5000.fr"))
  

  s.run()

startScenario()

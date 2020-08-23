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
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xBDbC8e4b486e3F44071d797cACc5834F61E9Cd0E.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x68dCa06FF803DE06d5e5Ec6f54F827cD10ad508E.json", 0, "gros-21.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x8AAf10C86f7B1A6cD7153c4A416cD60bCE0282F0.json", 0, "gros-22.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x95AE60c7305E1a5DA2eF7078cfE844b66a69c036.json", 0, "gros-32.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x893973413808128E1F908E88b56dA47d23288edd.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x7144c1A8fDF74c0ECd8509fFE78f86449Af6915D.json", 0, "gros-46.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xEb32D9AD1E2299ace0F912B042fF50C2528df368.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xbA7203a35a44372c8deca9A211B34bFa3d08CF28.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x784fCC8bDda1D4455225D6a77B8111B1e50F64d7.json", 0, "gros-65.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xb7C80e572f8d58D73776B1321325bAa9F8950a7F.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x7CBC37F2B88EfEcAefe747F2e244965b57fcA6D1.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xC4f61f2a89F1BC8FeDF14e1c022D6c719f4fdDee.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xB7296461fD87e7aCfA0CAdBd02494479B31205Ec.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x454237d39ce2536cFEA26591c23e85a41Ac6daCd.json", 0, "gros-81.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x933279BFE7954f0531C3bef688213bB4FBAFA1db.json", 0, "gros-82.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf95eF999d8c9099317C64F184209614D2A2C411A.json", 0, "gros-83.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xde2e49aded6471811aC10032d7dE71d3A6ecFe6a.json", 0, "gros-84.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xd11Ce22092D2A364A55c749e5e20489Ac5CAcB0A.json", 0, "gros-85.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x543FFF0f799870BbB31DD696737F6079D646359D.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x5D708C2e20286Dfe112B05FcdBA9140cC665eF3a.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x0107BF87689700C69CeD20bf9209454e97995209.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x2db0BEe6Db69Ab687990149bE899E183C96a4936.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xBeD6B912fe1042dcF0758a74Aa4002F0a1721a0f.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xfcaf72F47DbAD1aC9c3dd1A2122331FEF065eB11.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xC2Bd08799eb93E7E8D9B208078561988361154e8.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x849068d53722651287eCE7611c7d4dEfd7d8a022.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf4B6b402CE1c50CC8eEdcbDA297c0619E511dcD8.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xf1710f0911e8377fB8d52CF6e71c8E7d0Add7553.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x610c83C9aC8d3B68b2F46195FbC96bC257ac13Ce.json", 0, "gros-98.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x354546dbA689D4E40b4231Ef443d1938635D3E03.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x61D8565c39e2C57AC308e2b15543122dFa123910.json", 0, "gros-119.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x212B09Db1be4E9d9EF04ec543925bbeA72A60898.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xc49dD5e3F0723faCA596182496DcfD5D88cf4121.json", 0, "gros-21.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x65704619d76CFb39501bfE4c988c0FF392A6C850.json", 0, "gros-22.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xB7932fA830aDbdB75395b86A0F52d85A711a9f3d.json", 0, "gros-32.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x896d714A25Edc972980477EC5771f3164115252e.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xCa7eFE06eF7f6D5b51A00aBCAce9C5Eb37e237e5.json", 0, "gros-46.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0xD5B93bd39592dCdBD14FC131cF685e85E1e9433C.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x9a7e65B165893D9188C998458eeD2fA2e1A0665d.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 666 at 10
  s.enter(10, 1, process, argument=(666, "0x02f998fF4803502779d816bFD4e26f009BFfb9D0.json", 0, "gros-65.nancy.grid5000.fr"))
  

  s.run()

startScenario()

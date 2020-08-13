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
  
  #Killing gros-7.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-7.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-7.nancy.grid5000.fr"))
  #Killing gros-8.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-8.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-8.nancy.grid5000.fr"))
  #Killing gros-9.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-9.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-9.nancy.grid5000.fr"))
  #Killing gros-42.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-42.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-42.nancy.grid5000.fr"))
  #Killing gros-43.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-43.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-43.nancy.grid5000.fr"))
  #Killing gros-44.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-44.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-44.nancy.grid5000.fr"))
  #Killing gros-45.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-45.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-45.nancy.grid5000.fr"))
  #Killing gros-46.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-46.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-46.nancy.grid5000.fr"))
  #Killing gros-47.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-47.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-47.nancy.grid5000.fr"))
  #Killing gros-48.nancy.grid5000.fr at 30 and reUp at 100
  s.enter(30, 1, killNodes, argument=(30, "gros-48.nancy.grid5000.fr"))
  s.enter(100, 1, reUpNodes, argument=(30, "gros-48.nancy.grid5000.fr"))

  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x3BC4BdbB94d493656865c1775eD4a5F16579a480.json", 0, "gros-5.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x6D44CD2C817fDc276555c5635F5de89B01263626.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xbe22f10e44EBd18879cA67a6de428b8D3805dA43.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x3432b15B4a0E88996Ba1e241539C1Cd70C391cEe.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x9c67dFA6242385C7F61710227aB84f0459BD7429.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x4106a113602fC7500f704C71C3b4AF1D1905be99.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x9978A9A736C1B66E21308Dcf99a0DD5159b23215.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x9B9252Fc1096C70Cb170765BE82168547cc55153.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xB6DEA0879cAA346e71c5D8749D8A41AB103aeE45.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x9a38a0586C1d4591032883A4b7CD088322979a73.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xb27ae0781bb6654e7A78B732Eb7cfFee71Ef122D.json", 0, "gros-90.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x2ddc3230b789b90474f7EC27268646519d9C0903.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xFbe752754eB821Cdd3cbd968Cd59Ef2F82FaA41E.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x0AD6EdE4D0fA02f6890789bbd7B52fe50ccb6f8D.json", 0, "gros-87.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xc2d06b49717Ec374f8830A4d87a4EfF5cF11D45a.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xDD4505917e671fd1666Dafe7Ec6D6FBAe7B61cA7.json", 0, "gros-85.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xf25F71459d0da55a21df5d532177F39887C5E261.json", 0, "gros-84.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x7F3431C55cd70A90E62982431219e7A565B88e8E.json", 0, "gros-83.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x0345d920D0da03e54951DeC19770a3223AA84C99.json", 0, "gros-82.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x0982Aa8A9c92eDA9cc80663e676A10F10bBB0700.json", 0, "gros-81.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xF8DA7C6dbeEF5d9263C18C49DC0A1E2112141028.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x5356124241E0e93167F1dc6B8b0327e2bfe2ed26.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x36bd8aE03dc07d6A63C65576178AA67773673e73.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xBf16ABcd0e128BA2D6BFeFF9187c929b3E1974D6.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xC9b1D3f16Ad5027A561180228e8E3744e2C5a94B.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xB492cD5b0AE4eeAcf14bF0A8a593f8224AeFebaB.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x7D6adad79894B8D090915F1093002F44b5C7baC5.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x53E05d0Ff778eD914F6BF7CCC932e5C4d4363cBf.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x1924Ff8c55484Df4B85540c669b40fDEA57C021c.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x4767307383F6fA97216959c93E6d7D4CfEc83046.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x4769CF3129B9D3b0A5AdE57223801bAaa1f29494.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xbb18F67e3C135Afc5f7D524ae12fc6c218b3962B.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xD1EA9F9Eb6dC942bf5DfD4f7e2972748eE19B903.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xde93c2de5eeC1cB57324C7CaBd0d86D3b66B2160.json", 0, "gros-67.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xFc0742d756dAA64ADd9D4193083cb32E9e008AF2.json", 0, "gros-66.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x7012434152548925c834407A28afF3abB8a7bD3B.json", 0, "gros-65.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xaF02bdd7F91E0532fC9d9325b0A6b08ac47Dde32.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x55d27a196b1C798F0703C321914Fd63069B1C80e.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x2045c408EDE455F1E91b5385E319f02C0bC74B79.json", 0, "gros-62.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xd1c01Ae39765811b964AAfC3792e811629fB6Bf0.json", 0, "gros-61.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x6eF5339361Cb01a729BE94C5726ab51bb4877D3a.json", 0, "gros-60.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xAe0C9E6aa73578aEa417499612Dc363ebf33f517.json", 0, "gros-59.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xE79222b799517f45Bd6e8AfE6fc6b98887548615.json", 0, "gros-58.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x53bAaaC8CcEd2112d735452CAa41bD317994222D.json", 0, "gros-57.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xb6A9496AB5A762db9492188726084CdeF4ec02F6.json", 0, "gros-56.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xAD46203BD46017f1f2167A7524d4059A05A7243d.json", 0, "gros-55.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xE24E2A5Beee458D66F1DfA6040bf231f76a4361d.json", 0, "gros-54.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x348040dAEc02eDF46F0CCe30ae192b27a025D10D.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xa85CcFdb6B03Eb45B27704518D940CF06BbE80e5.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x6605e4abdb7798706690ae45C74087E467b59510.json", 0, "gros-51.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x58034e2F406809e7a3bfb988B9b5973dd98CFE89.json", 0, "gros-50.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x9f5749646BBF9e3b677d1127c50b0256A26578CB.json", 0, "gros-49.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x56E444f5b9Cf56d6f9824cD7EAA2603FcA1Bd431.json", 0, "gros-5.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xc928B506f30D577231317d5CE1bDAc9A2dDc185A.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xA24432CE437F81AF80Ae69279Cd8891665aefbe5.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x2296Dec967Bc11779222BE9c8Eb2C6fd276216cB.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xe7a65acAD9d445df860D86516bEf01Fdf34CeC88.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x8eD8826939412AE11dC1194930FBF8b96421b299.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x03f25FDD1A2E695d75C22656f518a97EbAE84aB8.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x316a4eCA012100dd1Ab0b8b97767cB4F8Bd2fD2b.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x3f8E97b58Ef8ac6F7305844E924423B3c40Dc6C0.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x9D25Ac7e4Ff746c5366e3dBb3c804E4311d5b536.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x4cBee17B6B7e4D47e889533E77Cd71911D89A920.json", 0, "gros-90.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x705755Fb631235F4EBA8cE048f12290EF5811aeA.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x8144974066187a80d7cCaceD717d7143086475D5.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x486FE69252CD12bA29071F85A6dEAdd1d96e9799.json", 0, "gros-87.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x6C91b5ABD1697Db20b03672612a2689CD3939b8a.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x8F94610aA2Da57706C59B2d2CB242111e61264c0.json", 0, "gros-85.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0x61E6CBA21F78c38f98B700B5fA6A2bbF4D175881.json", 0, "gros-84.nancy.grid5000.fr"))
  
  # 100 Tx spaced by 700 at 10
  s.enter(10, 1, process, argument=(700, "0xeDded59E3b8ea15af0F6849E4977A3534E0662a1.json", 0, "gros-83.nancy.grid5000.fr"))
  

  s.run()

startScenario()

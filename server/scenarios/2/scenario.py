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
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x350f12a5D208802843572be574A144cD04bDD821.json", 0, "gros-4.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x21E2F08ea7DB448c1403DcbEdE77511c609E8EC0.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xf59673aFF49e274B64c5f6a93d7AFc304E6973B0.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x86302F1fd3F16636687562D21633C91E32f19DaB.json", 0, "gros-10.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xFe5B45DeF690B24c8883efff08E2Db9Eb89C3ff1.json", 0, "gros-11.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x54c7d647E02f56792a265dE42a2184Ce9424B17A.json", 0, "gros-13.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xa00797fa96361810d0e50E4492C38AD981DBb59e.json", 0, "gros-14.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xb2762f2444b4460bDac1D69379e867FC8773ef17.json", 0, "gros-15.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xE34dafA3c1CF3E1c351C3291138B92D64dbD4690.json", 0, "gros-16.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xF921fb6C0791635124a158aEd3cb79ba82918944.json", 0, "gros-18.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x92139490D458B1d1cd7c76B53CA4fd33c028785D.json", 0, "gros-19.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x54f79FE8D85fc66DD2c942aB20b1cbf9CBCb5124.json", 0, "gros-27.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x48604c701B35C47c05e21b2E3Fc6C9CD79f05c39.json", 0, "gros-32.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x887b6336c1124Bb3ce47a16D99F0edeA638b5aB1.json", 0, "gros-33.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xFCa280a62F08858034c8c5A5EE1914bF62EAa926.json", 0, "gros-39.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x5933f330104693565C08f7E3765f741129d20957.json", 0, "gros-40.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x97d362DDA171e7e37Ee77a4ac12F389eC8bc3Bb3.json", 0, "gros-43.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x20a1e96E8B9cB12cd69082179D91Bb46F639E493.json", 0, "gros-44.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x95918A1D44b94050BC36c852CF202fCB992Fb9b5.json", 0, "gros-48.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x44877e07dedC5E619cd66a7b237547b06f9Ae409.json", 0, "gros-49.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xeB06773F6e921d9e6EF362721Eab59EC8658F81C.json", 0, "gros-50.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x4491ec642C3bA54D0C908724F5ef5656E3DD8FD0.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x45ca9867542Bb98De5196CFc879BA790d2F43c5A.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x161c74B8de51f336247509DcDb0054B1B44df28A.json", 0, "gros-54.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x20B753C271D0979e1669C7BbEe9c3cdd15E42193.json", 0, "gros-55.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xD24274416b6a3ce8b8be3D70A40B04FBfc68b92D.json", 0, "gros-59.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x287F84e6B3C70D6837a4425aAbeDf956aB102923.json", 0, "gros-60.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x45299A58a4Cb056D7F0cC851a08CeF3902850d05.json", 0, "gros-61.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xed9cF866457bC90b727Ca24B512Af9CA85b35AbC.json", 0, "gros-66.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x5E3d19FF792fEf5290AE28884b51A2714d59e27D.json", 0, "gros-67.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x21748Ef2A3800d9d2af8fDDceff98D17477fff40.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x12c2C0aa5551F3B4D6D7a9755842eDBCd0902Bf9.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xfB18Bb160d3F0Fb5E3c880e5AA2a51d08E867d6C.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xC51dA4a4aFE328348f867d87B35F68f4147B6b0A.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x134FB1722a490A34731b6CaAe8441dE30B36DC64.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x6b21d0B6A6b4D335bD89F31d2056cf36e60a4cb2.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x475aA6D7610e6d6a5615BAce5192c5e0523667b1.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xFAD66CDDCAc2EC5D4aDB59E6e4b3cd601436d500.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xFdcA586CdC3F6AeFB7F5b74B5b9716100dd45Da1.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x55DAD0Aaa5683A6879ffc346b114e2570e09ca65.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xdeC87B8517f3ADa24d22B6c9De81DCa27ddebcC3.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x3cd898AA6eAe5067164C6E382d990D73F5c09b7B.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x5951593EB976dE6701D664F4cF19FBEcab0065B0.json", 0, "gros-81.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xE129Da38043dF29F5586Fa538b8eb7C581709066.json", 0, "gros-82.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xb3419332f0d5901DdEb5b8B90D33B9d30c87EF96.json", 0, "gros-83.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x42aBc6E9d0e9d01eb25673D8AbaCc952791f53fa.json", 0, "gros-85.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xA986f716D0B87Af7b2EefCd2c3E342390a62015E.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x7Fa2ad9F8E3Af3dC006859C4E217A2dD6D55A886.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xC9DDEd25Db763fdA2f4DBd5e2866D0fD521Cf262.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x1F528eC8fcc78C6F8375a5833dC81C379b28885C.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x634CcccABCe80124A923f279400B99F8935Fa5E1.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xBc2e4D8377DD2A6B05C36de62aA544A6DC1D2Dce.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x5780232308D7e9ADF456D72D6dcFce02d2658c29.json", 0, "gros-100.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xC5B7916BcCDA18812C354a909fCae5511E007306.json", 0, "gros-101.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xD71351f167a142705fc10e5394f4F005D71C36C3.json", 0, "gros-102.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x9755F2e55B4AcD9f931fa461342c95528C9a1309.json", 0, "gros-108.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x2dbFf46D5AaE74A906ae4e7C01E50Ce2D34C14f6.json", 0, "gros-110.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x8187C4934DFdF69bD0093F39721F7b91B2709b5C.json", 0, "gros-117.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x75Aa3ec26B4F21E01EA8252d3224B96ae22b3129.json", 0, "gros-122.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x2cb7b813378DDCb19635759F7D2b80fc68a1dCb0.json", 0, "gros-123.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x1Ea87499A077FB2E0638E22f0fACf62C73E6b2d6.json", 0, "gros-124.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x999443fb3cde4CAc8dc4736c657fC0F7CfdFf6a0.json", 0, "gros-4.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x6D6913797Ce5749d56e2d04BAF612b3196a8a682.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xdf19dd90f8e147b79C4cFB67Be55365131a1D3E5.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x3A6a16a30de37CcF87c8BAAD49257173640B27c9.json", 0, "gros-10.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xbcA397A1e3320C6d5272f3e3e4556e548748cc5A.json", 0, "gros-11.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x1a72630dfd0e3Fd84B6824590c5b5fB25a41c2fF.json", 0, "gros-13.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x8654c69d63566899638E378900010fdbc646AB10.json", 0, "gros-14.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0x10df27700452a9c2d265b59EaE2d22E0784A7DF7.json", 0, "gros-15.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1166 at 10
  s.enter(10, 1, process, argument=(1166, "0xD3853aC7eE0B3dB9fDc7dc22a786Fd61E1231f52.json", 0, "gros-16.nancy.grid5000.fr"))
  

  s.run()

startScenario()

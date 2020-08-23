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
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xb1ff6DA142D83bfD8663b8C6B1D797982987Cfc9.json", 0, "gros-2.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xf25f16eF6Fa6537971d8A5612EB1928A19200127.json", 0, "gros-4.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x8430A061311C779d950d8d798E8Dd8A4970dF7ae.json", 0, "gros-5.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x7c823D633fF7B2c44C500B22cc766bCe4251Cf47.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x642cF936d08ef0347A6c84b4E983566cec87E5e6.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xfcA0c9c52871BD5A500225ce5bC8FC690D8026BA.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xdb1a65750e50378a2917b7A5Ac888448Ed545DF7.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xC3b4593D9031dE47025627F5A4665EF94d1B18c2.json", 0, "gros-11.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x9aec88038C9e265bc4e69bA8b286364CB2534Ce1.json", 0, "gros-12.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x4bFda6D9639d135c5C314C2F80781c0c0Ca92522.json", 0, "gros-13.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xF288e058C04E3a3B620EeDBCD10a1b6dCb79Cc06.json", 0, "gros-14.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xEdDfeF1aEe5b75d06b556f21b3fA195ff58B2Fad.json", 0, "gros-15.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x24D9bb653e8f30E1b1E55141367dA4FA54147CdB.json", 0, "gros-16.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x0a1794aF67584EFb251C9a38e495eC7aa55787BC.json", 0, "gros-17.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xd32F235FAe53f18984Cb188f7977c1755E1A0fA9.json", 0, "gros-18.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x12f8812f6FC8dba9c6c27Eeac84052fAbe86BE19.json", 0, "gros-19.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x7b08751e23692ED6C2eF6F8AAc43151bF88Ef3ea.json", 0, "gros-20.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x724CA87b85d5129eBa5d65B8a93F8E04b0b7DD9E.json", 0, "gros-21.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x770364E22508a93F9d1F6ff5185529b0d564f3A2.json", 0, "gros-22.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x4270C6Ec3fe290417ddb2F03988f5ba68D55fcD9.json", 0, "gros-23.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x6F84042CffA9A8B6D4Fa7ee6387264CAEDD70160.json", 0, "gros-24.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x21040580034e28d1Cd32B44507aF117a8F2ccE95.json", 0, "gros-25.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x41b2067618Bf32c7E14484db859AAbE73Ab9D9f0.json", 0, "gros-26.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x26323C71fe57BcB7F189b997D356a238363C8fd6.json", 0, "gros-27.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x8adeF062fe83C682b81ECB69dF022b09B9cCf631.json", 0, "gros-28.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x47CdE5d6E497cFA5Ad469BB9A679582C6F773BC8.json", 0, "gros-29.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x8f8DC4624F4bBb732Ce6a90AE57E3DE34C63A067.json", 0, "gros-30.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x57b77c31C125A9BE4B0440fe2a7aB05761851dc4.json", 0, "gros-31.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x6cF1BB2be1a8A20Db36796Ef4D43457da49D671F.json", 0, "gros-32.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x297a2bA3a4561904dC02377C5efdB233dd2B2058.json", 0, "gros-33.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x1A348B74004226Ff90DB6f0ad71ecd2ddAA49D56.json", 0, "gros-34.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xD29ef13E78Ca5B6a3D8B8A33678a8196ddeF6dE5.json", 0, "gros-35.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x6802089F6931512F4317Da7FBef4de0495e8BF34.json", 0, "gros-36.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xEDACC67fec5a6311097859364BD2c0BC69DdAc3a.json", 0, "gros-37.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x64319EF5037fd7AF7d9836FE4102c60Bed5dCB2A.json", 0, "gros-38.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xEb1614648a614052a7BAe5ef1F403BeF2E793F83.json", 0, "gros-39.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x0E66baE97E9C00943DB01948941792E695761486.json", 0, "gros-40.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x8F3c72F65Af1cD0ebB6D4AD3B3be87fBA1e9EBc5.json", 0, "gros-41.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xE309035Db0Ab06778F75a430f37eC13216caC2DF.json", 0, "gros-42.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xAe6A2be68539a40803F9b012dCe51BfeC481a2C4.json", 0, "gros-43.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x3aAe37BBDAac8E794FD49054157765Bc755F30cB.json", 0, "gros-44.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xb93ECb80EA1603f2Df8A8E785bE9409B716cB052.json", 0, "gros-45.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xe50027EB2413567Fc51A431a98C6C41390664Bf3.json", 0, "gros-46.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x82D9304EcCE38344d8744200689315F0CD09755f.json", 0, "gros-47.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x5A96C3d06eA459040e21088035979C184C0dF2e6.json", 0, "gros-48.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xEF6397386C2DF08afC8944764e5f5d6709921227.json", 0, "gros-49.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x1b60e458E6B61bEf321CA50eE151Fda4b31Fb234.json", 0, "gros-50.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x000d92a0fA90A3d36c650E077654e9cdf20f74f4.json", 0, "gros-51.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x4DaeF96324e5EdEB29648Df14194039bd043B624.json", 0, "gros-52.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x170c62e4eb88f1e7864f968e55baF990CAbc118c.json", 0, "gros-53.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xA273e0bF2D7fd4Ca9402D921761C97885998F131.json", 0, "gros-54.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x58e679841014a4F6Beb7486617f0b1ce960f7A13.json", 0, "gros-55.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x01BEd0C0C974E1C2796D4b64A40077414B589D44.json", 0, "gros-56.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x2bB345aFA057F5Ebc540AD5C1a54319DD75D4Ab0.json", 0, "gros-57.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x462DCE4f9Ee39024490519aC65c6e2D855a32722.json", 0, "gros-58.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xc739BDb1D88EAdc7ed0eAb06152b85a06FeEE10D.json", 0, "gros-59.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xDbDcb8eb5e603525E6f51B29D8D8d257580b7484.json", 0, "gros-60.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xf9b87c9eF91c5fbDfdbb2DFD04EFe150a0867F43.json", 0, "gros-61.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x815092AcC04761556a3c18a0F0c099a898549cF6.json", 0, "gros-62.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xAbbf59A47F055e6e816D29476D9Bd87569D85FAc.json", 0, "gros-63.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x8A97978Dbc90D71F4797C46Fda73426A0b8CFCA7.json", 0, "gros-64.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x6a0eE18BbF606EF5EbFB779e451a07Eec7CCa8bA.json", 0, "gros-65.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x182e035a56FB5884Ab114809440DC15294650D3c.json", 0, "gros-66.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x807E73847AF17Da7155f4Db1Ca0c10D25F5bbb99.json", 0, "gros-67.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xeEBFB7Ea9D3c5B3dAfA372b34cEe829857faa5b1.json", 0, "gros-68.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x4E6903a73345c7d8Cc24C7966CbE98dfad5263CA.json", 0, "gros-69.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x6F7CF0ba30989A1A51e8B1627b7cADb09956C1c0.json", 0, "gros-70.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xbAb37e27dbd8924c03CaBf97F4a1a17B175B3956.json", 0, "gros-71.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x5c9Ee5005258a28d5BAC62fE0Dbb24C80AC13561.json", 0, "gros-72.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xEab07f53A1FeB4F0a066043896891b97093083b9.json", 0, "gros-73.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xF359EB5Ba04d124B9E162a93D04c538B5f1B07E6.json", 0, "gros-74.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x07B73854a7b927A24751c77264AC00Ce985e5404.json", 0, "gros-75.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x538323fcb5d971D88a38F1965e9419De2564535a.json", 0, "gros-76.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x0da3d64642BCdEf66d2436e23C1cF948006b5532.json", 0, "gros-77.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x362bADD9258360946d0d8b49DdC89be9Cd6e27A5.json", 0, "gros-78.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x221dEb5B904dDef2fDBAE183cAfc0f9A70660E3b.json", 0, "gros-79.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x3D8Ad917976A3Fcc86C0705f7aA83A92176E063B.json", 0, "gros-80.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x2a2e93aFc025d6379c8E9A310Df72699232aF07e.json", 0, "gros-81.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x0d2d8887a0921c2046e91c14a6c7bA9bD287bD79.json", 0, "gros-82.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xca2d2e3Ad6a38769674BE37E7f1b21Af4666d92d.json", 0, "gros-83.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xc13e868E8274b9A2a7aE70826979CBFeCFdbBBdF.json", 0, "gros-84.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x603dBbA7a89bcDe35620d350348a9425095A6293.json", 0, "gros-85.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x5BaAdd0445e4111333CD13596eA572E9C5869DC7.json", 0, "gros-86.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xF671a6F344304730b401775ff677Af9864623b8a.json", 0, "gros-87.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x82B5e20498b8F9aEE903b70Af297E6875223dCCC.json", 0, "gros-88.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xAB2eaf4d790Bc91a4e24051600D60b421c437808.json", 0, "gros-89.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xe3d166e3F7a290dB3Cb30c9e6c208c374b7D795B.json", 0, "gros-90.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x7D6f06528CEbE653C5A32132dD5C9553f38835A1.json", 0, "gros-91.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x4EFfe733bB32402fF5EB9Bc1ceaB33442ceAa152.json", 0, "gros-92.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x3Dd1Be83f6e41FF35B2418087e077b3e73d0FC95.json", 0, "gros-93.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xA6A232F802562e7B0Af47578774098E6899977D3.json", 0, "gros-94.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xF72D87Ba42c41923AC2F82274C5aaaCaD05368A4.json", 0, "gros-95.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x54536408a37294C91324e4A08B3660aC2fD85fa7.json", 0, "gros-96.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x400a0a1058830Ac333008e66B053A01810116980.json", 0, "gros-97.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x3aE56526AC9846F5b9e7917DCb3eef9C433A06c6.json", 0, "gros-98.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x9a124A1CFF008Ad3a43C1C55a431deCd8d3F87B3.json", 0, "gros-99.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x9e4A8d3816B9636D4D71EE41f4d603C849f1Fed7.json", 0, "gros-2.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x37b9342028204969fd09ac5203600F08Ff993081.json", 0, "gros-4.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x9d7C7b50259AB94fF05594cfb59d12De0e0595E8.json", 0, "gros-5.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xCcbF5F92c217110Bc227d5BFe6648d1440CA086d.json", 0, "gros-6.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x2Cc0ABe6F80Ee3187aCd63576ffb7495A9D7A8ef.json", 0, "gros-7.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x389027D5Ba7fd424407f25B236D12bbf14d7FE85.json", 0, "gros-8.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xC63646933A3C5F1d06A42118c098eB35804AdE9e.json", 0, "gros-9.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x8806121626077FE55F347F8a34f2E330eAE8c133.json", 0, "gros-11.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0xCD94A365b8c24FD149E359F4C4814E3a0d4ed894.json", 0, "gros-12.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x35A14dE371FF7B6f9c9eD57EE887D6B9884a2Fa7.json", 0, "gros-13.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x09223d53b45561FfCfDbfC267fF0A487C84CE3E9.json", 0, "gros-14.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x663501FfF3EDD5cE0dC96DE216A04cCAdAC896a7.json", 0, "gros-15.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x7036a9dbc8dA6036f13C8A11c6617Da04af0F6A8.json", 0, "gros-16.nancy.grid5000.fr"))
  
  # 60 Tx spaced by 1833 at 10
  s.enter(10, 1, process, argument=(1833, "0x63bA401D1D4cA9BaB0aF8eC8cefb67508757D495.json", 0, "gros-17.nancy.grid5000.fr"))
  

  s.run()

startScenario()

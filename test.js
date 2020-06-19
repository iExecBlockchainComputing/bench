const ethers = require("ethers");

let web3 = new ethers.providers.JsonRpcProvider("http://localhost:8545")

let wallet = new ethers.Wallet("0xaadbffbda78a7b1e7e98acb801cfe9fac326f0ce0c9c90a48fc9535fb83d7b76", web3);


let tx = wallet.signTransaction({
  to: "0x1f23f42c865d7D580C5850fCf13518307C2fa567",
  value: ethers.utils.parseEther("0x1"),
});

Promise.resolve(tx)
  .then(wallet.sendTransaction(tx));
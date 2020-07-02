const fs = require('fs');
const ethers = require("ethers");
var now = require("performance-now");

var wallets = JSON.parse(fs.readFileSync('./wallets.json'));
var transactions = JSON.parse(fs.readFileSync('./transactions.json'));
var ips = JSON.parse(fs.readFileSync('./ips.json'));

var args = process.argv.slice(2);

var time = args[0];
var delay = args[1];

function sleep(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, ms) 
    });
}

function sendTransactions(transaction, i, ip, wallet) {
    return new Promise(async (resolve, reject) => {
        try {
            console.log("start " + i + ": " + now())
            let deb = now()
            let provider = new ethers.providers.JsonRpcProvider("http://" + ip + ":8545")
            let signer = new ethers.Wallet(wallet.privKey, provider);
            const tx = await signer.sendTransaction(transaction)
            console.log("Hash " + i + " : " + tx.hash);
            const res = await tx.wait()
            console.log('res'+ i + " : " + res)
            resolve({
                'transactionResponse': res, 
                'start': deb,
                'end': now(),
                'executionTime': now() - deb
            })
        }
        catch (e) {
            console.error(e.message);
            resolve(e.message);
        }
    })
}

let txArray = transactions[time].txs;

let results = txArray.map((tx, i) => {
    return new Promise ( async (resolve, reject) => {
        await sleep(delay*i)
        const res = await sendTransactions(
            tx,
            i,
            ips.moc,
            wallets[i%wallets.length]
        )
        resolve(res);
    });
})

Promise.all(results).then(res => {
    fs.writeFileSync("./results.json", JSON.stringify(res));
})

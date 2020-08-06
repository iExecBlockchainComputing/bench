const { ethers } = require('ethers');
const fs         = require('fs');

var args = process.argv.slice(2);
var txFileNumber = args[0];
var eventNumber = args[1];

var arrayFiles = fs.readdirSync('./' + eventNumber)
var transactions
arrayFiles.forEach(el => {
    transactions = JSON.parse(fs.readFileSync(el));
});

// var transactions = JSON.parse(fs.readFileSync('./' + eventNumber + '/tx'+ txFileNumber +'.json'));

let txArray = transactions.txs;
var privKey = transactions.privKey;

let rawTxArray = txArray.map((tx, i) => {
    return new Promise (async (resolve, reject) => {
        let signer = new ethers.Wallet(privKey);
        let raw = await signer.signTransaction({...tx, 'gasPrice': 0, 'gasLimit': 21000});
        resolve(raw.toString());
    })
})

Promise.all(rawTxArray).then(resolved => {
    fs.writeFileSync('./' + eventNumber + '/' + txFileNumber + '.json', JSON.stringify(resolved.slice(',')));
});
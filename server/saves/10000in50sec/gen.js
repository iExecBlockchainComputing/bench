'use strict';

const { ethers } = require('ethers');
const fs         = require('fs');

var transactions = JSON.parse(fs.readFileSync('./transactions.json'));
var wallets = JSON.parse(fs.readFileSync('./wallets.json'));
var ips = JSON.parse(fs.readFileSync('./ips.json'));
var args = process.argv.slice(2);
var time = args[0];

let txArray = transactions[time].txs;

let rawTxArray = txArray.map((tx, i) => {
    return new Promise (async (resolve, reject) => {
        let signer = new ethers.Wallet(wallets[i%wallets.length].privKey);
        let raw = await signer.signTransaction({...tx, 'gasPrice': 0, 'gasLimit': 21000});
        resolve(raw.toString());
    })
})

Promise.all(rawTxArray).then(resolved => {
    fs.writeFileSync('./raw' + time + '.json', JSON.stringify(resolved.slice(',')));
});

let providerArray = ips.all.map(el => {
    return new Promise(async (resolve, reject) => {
        resolve(new ethers.providers.JsonRpcProvider("http://" + el + ":8545"))
    })
});

Promise.all(providerArray).then(res => {
    fs.writeFileSync('./provider.json', JSON.stringify(res))
})
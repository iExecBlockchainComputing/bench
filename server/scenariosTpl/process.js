const fs = require('fs');
const ethers = require("ethers");
const { resolve } = require('path');


var args = process.argv.slice(2);
var fileName = args[0];
var delay = parseInt(args[1]);
var eventNumber = args[2];
var ip = args[3];

var rawTxArray = JSON.parse(fs.readFileSync('./' + eventNumber + '/' + fileName));
// var ips = JSON.parse(fs.readFileSync('./ips.json'));

const provider = new ethers.providers.JsonRpcProvider("http://" + ip + ":8545")
rawTxArray.reduce((accPromise, raw) => new Promise(resolve =>
        accPromise.then(acc => setTimeout(async () => {
                let tx = await provider.sendTransaction(raw);
                acc.push({ start: Date.now() / 1000, tx });
                resolve(acc);
        }, delay ))
), Promise.resolve([]))
.then(txs => fs.writeFileSync('./' + eventNumber + '/executed_' + fileName, JSON.stringify(txs)));

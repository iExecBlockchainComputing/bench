const fs = require('fs');
const ethers = require("ethers");
const { resolve } = require('path');

var args = process.argv.slice(2);
var timing = args[0];
var delay = parseInt(args[1]);
const START = Date.now()

var rawTxArray = JSON.parse(fs.readFileSync('./raw' + timing + '.json'));
//const providers = JSON.parse(fs.readFileSync('./provider.json'));
const providers = new ethers.providers.JsonRpcProvider("http://localhost:8545")

rawTxArray.reduce((accPromise, raw , index) => new Promise(resolve =>
	accPromise.then(acc => setTimeout(async () => {
		let tx = await providers.sendTransaction(raw);
		acc.push({ start: Date.now() / 1000, tx });
		resolve(acc);
	}, START + delay - Date.now()))
), Promise.resolve([]))
.then(txs => fs.writeFileSync('./executed' + timing + '.json', JSON.stringify(txs)));

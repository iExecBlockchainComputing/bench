'use strict';

const { ethers } = require('ethers');
const fs         = require('fs');
const ips = JSON.parse(fs.readFileSync('./ips.json'));

const provider = new ethers.providers.JsonRpcProvider("http://" + ips.moc + ":8545")

var args = process.argv.slice(2);
// var fileName = args[0];
var eventNumber = args[0];

var filesName = fs.readdirSync(eventNumber);

fs.mkdirSync("./results");

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

filesName.forEach(fileName => {
	Promise.all(
		JSON
		.parse(fs.readFileSync(process.env.INFILE || './' + eventNumber + '/' + fileName))
		.map(async ({ start, tx }, i) => {
			sleep(10 + i);
			return ({
				start,
				receipt: await provider.getTransaction(tx.hash),
			})
		})
	)
	.then(entries => {
		Promise.all(
			entries
			.map(({receipt}) => receipt.blockNumber)
			.filter((entry, i, array) => array.indexOf(entry) == i)
			.map(blockNumber => provider.getBlock(blockNumber))
		)
		.then(blocks => {
			const timestamps = blocks.reduce((acc, block) => Object.assign({ [block.number]: block.timestamp }, acc), {})
			fs.writeFileSync('./results/' + fileName, JSON.stringify(
				entries.map(({ start, receipt }) => ({
					start: start,
					stop:  timestamps[receipt.blockNumber],
					executionTime: timestamps[receipt.blockNumber] - start,
					blockNumber: receipt.blockNumber
				}))
			))
		})
	})
});

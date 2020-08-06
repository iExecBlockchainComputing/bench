'use strict';

const { ethers } = require('ethers');
const fs         = require('fs');
const ips = JSON.parse(fs.readFileSync('./ips.json'));

const provider = new ethers.providers.JsonRpcProvider("http://" + ips.moc + ":8545")

var args = process.argv.slice(2);
var time = args[0];

Promise.all(
	JSON
	.parse(fs.readFileSync(process.env.INFILE || 'executed' + time + '.json'))
	.map(async ({ start, tx }) => {
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
		console.log(JSON.stringify(
			entries.map(({ start, receipt }) => ({
				start: start,
				stop:  timestamps[receipt.blockNumber],
				executionTime: timestamps[receipt.blockNumber] - start,
				blockNumber: receipt.blockNumber
			}))
		))
	})
})

import React from 'react';
import { ethers } from 'ethers';
import { useState, useEffect } from 'react';
import { useTracked, checkEthProvider } from '../../components/State';
import stringify from 'fast-json-stable-stringify'

import { makeStyles } from '@material-ui/core/styles';
import { useSnackbar } from 'notistack';
import { Button } from '@material-ui/core';
import Paper from '@material-ui/core/Paper';


const useStyles = makeStyles(theme => ({
	bottom: {
		width: '100%',
	},
  left: {
		position: 'absolute',
		left: "2%",
		width: '46%',
	},
	right: {
		position: 'absolute',
		right: "2%",
		width: '46%',
	},
	heading: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '90%',
    flexShrink: 0,
	},
	input: {
    marginLeft: theme.spacing(1),
    flex: 1,
  },
  textField: {
    margin: theme.spacing(1),
    flex: 1,
  },
  container: {
    padding: theme.spacing(2),
  },
	iconButton: {
    padding: 10,
	},
	hiddenInput: {
    display: 'none',
	},
	fab: {
    margin: theme.spacing(2),
  },
  absolute: {
    position: 'absolute',
    bottom: theme.spacing(2),
    right: theme.spacing(3),
  },
}));

export default function ThroughtputWrite() {
	const classes = useStyles();
	const { enqueueSnackbar } = useSnackbar();

	const [globalState, setGlobalState ] = useTracked();
	const [nbTransaction, setNbTransaction] = useState(2);
	const [time, setTime] = useState(0);
	const [gap, setGap] = useState(0);
	const [sendingValue, setSendingValue] = useState(0);
	const [gasPriceValue, setGasPriceValue] = useState("20000000000")
	const [transactions, setTransactions] = useState([]);
	const [signedTransactions, setSignedTransactions] = useState([])

	async function initializeBench() {
		let tmpTransactions = [];
		let tmpSignedTransactions = [];
		let index = 0;
		if(nbTransaction > 0) {
			// getting the nonce of each wallets
			globalState.wallets.forEach((wallet, it) => {
				new ethers.Wallet(wallet.privateKey, globalState.testedChainProvider).getTransactionCount()
				.then((_nonce) => {
					// creating the transactions for each wallets
					while(index < nbTransaction) {
						if(index === 0) {
							tmpTransactions[it] = [];
							tmpSignedTransactions[it] = [];
						}
						tmpTransactions[it].push({
							nonce: _nonce+index,
							to: globalState.mainWallet.signingKey.address,
							value: ethers.utils.parseEther(stringify(sendingValue)),
							gasLimit: 21000,
							gasPrice: ethers.utils.bigNumberify(gasPriceValue),
							chainId: globalState.ethProvider.chainId,
						})
						tmpSignedTransactions[it].push(wallet.sign(tmpTransactions[it][index]))
						index = index+1;
					}
					index = 0;
				})
			})
			setSignedTransactions(tmpSignedTransactions);
			setTransactions(tmpTransactions);
		} else {
			enqueueSnackbar("nombre de transaction trop faible", {variant: "error"});
		}
		enqueueSnackbar("Transactions are ready !", {variant: "success"});
	}

	function startBench() {
		let index = 0;
		globalState.wallets.forEach((wallet, it) => {
			index = 0;
			while(index < nbTransaction) {
				signedTransactions[it][index].then((signedTx) => {

					globalState.ethProvider.sendTransaction(signedTx)
					.then((tx) => {
						globalState.ethProvider.waitForTransaction(tx.hash)
						.then((tx) => {
							// setWaitTransaction(false);
							enqueueSnackbar("Transaction to " + tx.to + " mined", {variant: "success"})
							// setGlobalState({reload: true});
						})
					})
				});
				index = index+1;
			}
		})
		// enqueueSnackbar("Bench done !", {variant: "success"});
	}

	function testBench() {
		
	}

	return (
		<div>
			{ !checkEthProvider(globalState) ? <h2>Please choose an eth Provider</h2> :
				<div>
					<h1>Throughtput Write</h1>
					<div className={classes.left}>
						<Paper variant="outlined" className={classes.container}>
							<h4>Bench:</h4>
							
						</Paper>
					</div>
					<div className={classes.right}>
						<Paper variant="outlined" className={classes.container}>
							<h4>Logs:</h4>
						</Paper>
					</div>
      
				</div>
			}
		</div>
	);
}
import React from 'react';
import { ethers } from 'ethers';
import { useState, useEffect } from 'react';
import { useTracked } from '../State';
import stringify from 'fast-json-stable-stringify'

import { makeStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { useSnackbar } from 'notistack';
import Button from '@material-ui/core/Button';
import ListItem from '@material-ui/core/ListItem';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import InputBase from '@material-ui/core/InputBase';
import Input from '@material-ui/core/Input';
import Icon from '@material-ui/core/Icon';
import IconButton from '@material-ui/core/IconButton';
import Paper from '@material-ui/core/Paper';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CircularProgress from '@material-ui/core/CircularProgress';

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

export default function WalletManager() {
	const classes = useStyles();
	const { enqueueSnackbar } = useSnackbar();

	const [globalState, setGlobalState ] = useTracked();
  const [expanded, setExpanded] = useState(false);
	const [walletsInput, setWalletsInput] = useState(1);
	const [mainWalletBalance, setMainWalletBalance] = useState("");
	const [privKey, setPrivKey] = useState("");
	const [fill, setFill] = useState(0);
	const [waitTransaction, setWaitTransaction] = useState(false);
	
	useEffect(() => {
		setGlobalState({reload: true})
	}, []);

	useEffect(() => {
		if(globalState.ethProvider !== "" && globalState.mainWallet !== "") {
			if(globalState.reload) {
				globalState.ethProvider.getBalance(
					globalState.mainWallet.signingKey.address)
					.then(balance => {
						setMainWalletBalance(ethers.utils.formatEther(balance));
					})
				setGlobalState({reload: false});
			}
		} else {
			setGlobalState({reload: false});
		}
	}, [globalState.reload]);

	const handleChangePanel = panel => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
	};
	
	function walletExist(walletId) {
		if(globalState.wallets[walletId] !== undefined ) {
			return true;
		}
		return false;
	}

	function addWallet(wallet) {
		setGlobalState({wallets: globalState.wallets.concat(wallet)})
	}

	function createAndAddWallet() {
		addWallet(ethers.Wallet.createRandom());
		enqueueSnackbar('Random wallet created', { variant: 'success'})
	}

	function createAndAddMultipleWallets(number) {
		let tmp = new Array(parseInt(number)).fill(null);
		addWallet(tmp.map( (el, index) => {
			return ethers.Wallet.createRandom();
		}))
		enqueueSnackbar(number + ' Wallets created', { variant: 'success'})
	}

	// function getPublicKey(walletId) {
	// 	if(walletExist(walletId)) {
	// 		return globalState.wallets[walletId].publicKey;
	// 	}
	// 	return undefined;
	// }

	// function getPrivateKey(walletId) {
	// 	if(walletExist(walletId)) {
	// 		return globalState.wallets[walletId].privateKey;
	// 	}
	// 	return undefined;
	// }

	// function getAddressByWallet(wallet) {
	// 	return wallet.address;
	// }
	
	// function getAddressById(walletId) {
	// 	if(walletExist(walletId)) {
	// 		return globalState.wallets[walletId].address;
	// 	}
	// 	return undefined;
	// }

	function checkEthProvider() {
		if(globalState.ethProvider === "") {
			return false;
		}
		return true;
	}

	function checkMainWallet() {
		if(globalState.mainWallet === "") {
			return false;
		}
		return true;
	}

	function exportWallets() {
		if(globalState.wallets.length > 50) {
			let div = globalState.wallets.length/50;
			let rest = globalState.wallets.length%50;
			let it = 0;
			while(rest > 0) {
				let arr = [];
				for(let i = 0; i < 50 ; i = i + 1) {
					arr.push(stringify(globalState.wallets[i].privateKey));
				}
				fetch( globalState.expressServer + "/wallets/export?array="+stringify(arr))
					.then(res => res.text())
					.then(res => enqueueSnackbar(JSON.parse(res).msg, {variant: JSON.parse(res).type})
					.then(() => enqueueSnackbar(it+"/"+rest, {variant: "info"})));
				rest = rest - 1;
			}

		} else {
			let arr = [];
			globalState.wallets.forEach((el) => {
				arr.push(stringify(el.privateKey));
			});
			fetch( globalState.expressServer + "/wallets/export?array="+stringify(arr))
				.then(res => res.text())
				.then(res => enqueueSnackbar(JSON.parse(res).msg, {variant: JSON.parse(res).type}));	
		}
	}
	
	function exportMainWallets() {
		let wallet = stringify(globalState.mainWallet);
		fetch( globalState.expressServer + "/wallets/exportMain?main="+wallet)
			.then(res => res.text())
			.then(res => {
				enqueueSnackbar(JSON.parse(res).msg, {variant: JSON.parse(res).type})
			});
	}

	function deleteAllWallets() {
		console.log(Math.trunc(globalState.wallets.length/50));
		// fetch( globalState.expressServer + "/wallets/deleteAll")
		// .then(res => res.text())
		// .then(res => enqueueSnackbar(JSON.parse(res).msg, {variant: JSON.parse(res).type}));
		// setGlobalState({wallets: []});
	}

	function fillAllWallets() {
		// cas : pas de wallets, value a 0
		if(globalState.wallets.length !== 0 && mainWalletBalance >= fill) {
			setWaitTransaction(true)
			let _value = fill / globalState.wallets.length;
			let transactionArray = [];
			let tmpWallet = new ethers.Wallet(globalState.mainWallet.signingKey.privateKey, globalState.ethProvider)
			if(checkEthProvider()) {
				tmpWallet.getTransactionCount().then((_nonce => {
					globalState.wallets.forEach((el, index) => {
					
						transactionArray.push({
							nonce: _nonce+index,
							to: el.address,
							value: ethers.utils.parseEther(stringify(_value)),
							gasLimit: 21000,
							gasPrice: ethers.utils.bigNumberify("20000000000"),
							chainId: globalState.ethProvider.chainId,
						})
					});
					transactionArray.forEach((el, index) => {
						let signedPromise = tmpWallet.sign(el);
						signedPromise.then((signedTransaction) => {
							globalState.ethProvider.sendTransaction(signedTransaction)
							.then((tx) => {
								globalState.ethProvider.waitForTransaction(tx.hash)
								.then((res) => {
									setWaitTransaction(false);
									enqueueSnackbar("Transaction to " + tx.to + " mined", {variant: "success"})
									setGlobalState({reload: true});
								})
							})
						})
					});
				}))
			}
		} else {
			// interdit
		}

		return undefined;
	}

	function changeMainWallet() {
		if(privKey === "") {
			enqueueSnackbar("Empty Private Key", {variant: "error"})
		} else {
			setGlobalState({mainWallet: new ethers.Wallet(privKey), reload: true});
			setPrivKey("");
			exportMainWallets();
		}
	}
	
  return (
		<div>
			{ !checkEthProvider() ? <h2>Please choose an eth Provider</h2> :
			<div>
				<div className={classes.left}>
					<h1>Wallet Manager</h1>
					<br/>
					<ButtonGroup
						orientation="vertical"
						color="primary"
						size="large"
						aria-label="vertical outlined primary button group"
					>
						<Button onClick={() => createAndAddWallet()}>Create random wallet</Button>
						<Button onClick={() => exportWallets()}>Export wallets</Button>
						<Button onClick={() => deleteAllWallets()}>Delete wallets</Button>
						<Paper>
							<InputBase
								className={classes.input}
								placeholder="How much to split?"
								inputProps={{ 'aria-label': 'How much to split'}}
								value={fill}
								onChange={(e) => setFill(e.currentTarget.value)}
							/>
							{!waitTransaction ? <Button onClick={() => {fillAllWallets(); exportWallets();}} aria-label="split">Split and save</Button> : <Button disabled aria-label="split"><CircularProgress size={25}/></Button>}
						</Paper>
						<Paper>
							<InputBase
								className={classes.input}
								placeholder="Create X wallets"
								inputProps={{ 'aria-label': 'create X wallets'}}
								value={walletsInput}
								onChange={(e) => setWalletsInput(e.currentTarget.value)}
							/>
							<IconButton onClick={() => createAndAddMultipleWallets(walletsInput)} className={classes.iconButton} aria-label="create">
								<Icon className="fa fa-plus-circle" color="primary" />
							</IconButton>
						</Paper>
					</ButtonGroup>
				</div>
				<div className={classes.right}>
					{ !checkMainWallet() ? 
						<div>
							<h1>Please add main wallet</h1>
							<Paper>
								<Input
									className={classes.input}
									placeholder="Enter PrivKey"
									inputProps={{ 'aria-label': 'Enter PrivKey'}}
									value={privKey}
									onChange={(e) => setPrivKey(e.currentTarget.value)}
								/>
								<Button size="small" onClick={() => changeMainWallet()} aria-label="PrivKey">Change wallet</Button>
						</Paper>
						</div>
							:
						<div>
							<h1>Main Wallet</h1>
							<br/>
							<Card className={classes.root}>
								<CardContent>
									<Typography className={classes.title} color="textPrimary" gutterBottom noWrap>
										{globalState.mainWallet.signingKey.address}
									</Typography>
									<Typography className={classes.pos} color="textSecondary">
									Balance: {mainWalletBalance === "" ? <CircularProgress size={20}/> : mainWalletBalance}
									</Typography>
									<Typography variant="body2" component="p">
										
									</Typography>
								</CardContent>
								<CardActions>
									<Input
										className={classes.input}
										placeholder="Enter PrivKey"
										inputProps={{ 'aria-label': 'Enter PrivKey'}}
										value={privKey}
										onChange={(e) => setPrivKey(e.currentTarget.value)}
									/>
									<Button size="small" onClick={() => changeMainWallet()} aria-label="PrivKey">Change wallet</Button>
								</CardActions>
							</Card>
						</div>
					}
					<br/>
					<h1>Wallets</h1>
					{globalState.wallets.map((wallet, index) => (
					
					<ExpansionPanel expanded={expanded === index } onChange={handleChangePanel(index)}>
						<ExpansionPanelSummary
							expandIcon={<ExpandMoreIcon />}
							aria-controls="panel1bh-content"
							id="panel1bh-header"
						>
							<Typography noWrap className={classes.heading}>{wallet.address}</Typography>
						</ExpansionPanelSummary>
						<ExpansionPanelDetails>
							<ListItem><Typography noWrap>Private Key: {wallet.privateKey}</Typography></ListItem>
						</ExpansionPanelDetails>
					</ExpansionPanel>
					))}
				</div>
			</div>
			}
		</div>
	);
}
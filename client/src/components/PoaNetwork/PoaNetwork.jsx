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
import TextField from '@material-ui/core/TextField';
import { populateTransaction } from 'ethers/utils';
import Divider from '@material-ui/core/Divider';
import { forEach } from 'benchmark';

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

export default function PoaNetwork() {
  const classes = useStyles();
  const express = "http://localhost:9000";

  const [waitFetchBlock, setWaitFetchBlock] = useState(false);
	const { enqueueSnackbar } = useSnackbar();
  const [logs, setLogs] = useState("");
	const [globalState, setGlobalState ] = useTracked();

  const [repo, setRepo] = useState("");
  const [repoFetch, setRepoFetch] = useState("nathPay");
  const [chainName, setChainName] = useState("test");
  const [mail, setMail] = useState("np@iex.ec");
  const [mocHost, setMocHost] = useState("taurus-2.lyon.grid5000.fr");
  const [bootnodeHost, setBootnodeHost] = useState("taurus-10.lyon.grid5000.fr");
  const [otherHost, setOtherHost] = useState("taurus-11.lyon.grid5000.fr");
  // const [sshKeyPath, setSshKeyPath] = useState("");
  
  const [encryptedWallet, setEncryptedWallet] = useState("");
  const [spec, setSpec] = useState({
    "name": "", // change chain name here
    "engine": {
      "authorityRound": {
        "params": {
          "stepDuration": 5,
          "blockReward": "0x0",
          "maximumUncleCountTransition": 0,
          "maximumUncleCount": 0,
          "validators": {
            "multi": {
              // "0": {
              //   "list": [
              //     // add all validators address
              //   ]
              // }
            }
          }
        }
      }
    },
    "params": {
      "gasLimitBoundDivisor": "0x400",
      "maximumExtraDataSize": "0x20",
      "minGasLimit": "0x1388",
      "networkID": "0x11",
      "eip140Transition": "0x0",
      "eip211Transition": "0x0",
      "eip214Transition": "0x0",
      "eip658Transition": "0x0",
      "eip145Transition": "0x0",
      "eip1014Transition": "0x0",
      "eip1052Transition": "0x0",
      "eip1283Transition": "0x0",
      "eip1283DisableTransition": "0x0",
    },
    "genesis": {
      "seal": {
        "authorityRound": {
          "step": "0x0",
          "signature": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        }
      },
      "difficulty": "0x20000",
      "gasLimit": "0x663BE0"
    },
    "accounts": {
      //add accounts that have coins
      // "address": {"balance": "1000000000"}
    }
  })
  
  
  var IDCounter = 0;
  var web3Provider = new ethers.providers.JsonRpcProvider("https://rpcmainnet1w7wagudqhtw5khzsdtv.iex.ec");


  function generateConfig() {
    let otherHostModified = otherHost.split(",");
    fetch(express + '/wallets/getEncryptedWallet?privKey=' + globalState.mainWallet.signingKey.privateKey)
    .then(res => res.text())
    .then(res => {
      setEncryptedWallet(res);
    }).then(() => {
      let requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: stringify({
          'chainName': chainName, 
          'poaDeployementRepo': 'https://github.com/nathPay/poa-deployment-bench.git',
          'mocAddress': globalState.mainWallet.signingKey.address,
          'mail': mail,
          'repoFetch': repoFetch,
          'mocHost': mocHost,
          'bootnodeHost': bootnodeHost,
          'otherHost': otherHostModified
        })
      };
      fetch(express + '/bench/poaMocGroup', requestOptions)
      .then(() => {
        enqueueSnackbar("successfully initiated", {variant: "success"})
      });
    });
    // genSpec();
    let requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: stringify({
        'name': chainName,
        'validators': otherHostModified
      })
    };
    fetch(express + '/bench/genSpec', requestOptions)
    .then(res => res.json())
    .then(res => {
      enqueueSnackbar(res.msg, {variant: res.type});
    })
    
    // let sidechainProvider = new ethers.providers.JsonRpcProvider("https://" + otherHostModified[0]);

    // let transaction = {
    //   nonce: 0,
    //   to: ,
    //   value: ethers.utils.parseEther(stringify(0)),
    //   gasLimit: 21000,
    //   gasPrice: ethers.utils.bigNumberify("20000000000"),
    //   chainId: sidechainProvider.chainId,
    // }
    // let tmpWallet = new ethers.Wallet("0x8381D84F3639608F826F42F9CCD4CF70965F52D62AF5BB233EEF695986FB4A8B", sidechainProvider);
    // let signedPromise = tmpWallet.sign(transaction);
    // signedPromise.then((signedTransaction) => {
    //   sidechainProvider.sendTransaction(signedTransaction)
    //   .then((tx) => {
    //     console.log(tx);
    //     // sidechainProvider.waitForTransaction(tx.hash)
    //   })
    // })
  }

  function test() {
    let otherHostModified = otherHost.split(",");
    globalState.testedChainProvider = [];
    globalState.testedChainProvider.push(new ethers.providers.JsonRpcProvider("http://" + mocHost + ":8545"));
    otherHostModified.forEach((el) => {
      globalState.testedChainProvider.push(new ethers.providers.JsonRpcProvider("http://" + el + ":8545"));
    });
    console.log(globalState.testedChainProvider[0])
    console.log(globalState.testedChainProvider[1])
  }

  function validatorFiles() {

  }

  function genSpec() {
    spec.name = chainName;
    if(globalState.wallets.length === 0) {
      enqueueSnackbar("please add wallets", {variant: "error"})
    } else {
      let tmpList = [];
      let tmpAccounts = {};
      tmpAccounts[globalState.mainWallet.signingKey.address] = {"balance": "100000000000000000000000000000"};
      tmpList.push(globalState.mainWallet.signingKey.address)
      globalState.wallets.forEach(el => {
        tmpAccounts[el.signingKey.address] = {"balance": "100000000000000000000000000000"};
        tmpList.push(el.signingKey.address);
      });
      spec.engine.authorityRound.params.validators.multi
        = {"0": {"list": tmpList}};
      spec.accounts = tmpAccounts;
    }
    // if(globalState.mainWallet === {}) {
    //   enqueueSnackbar("please add main wallet", {variant: "success"})
    // } else {
    //   spec.params.registrar = globalState.mainWallet.signingKey.address;
    // }

  }

  function displayConfig() {
    setLogs(stringify(spec))
  }

  return (
    <div>
      <h1>Create PoA Network chain</h1>
      <div className={classes.left}>
        <Paper variant="outlined" className={classes.container}>
          <h4>Spec.json:</h4>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Chain name"
            inputProps={{ 'aria-label': 'chain name'}}
            value={chainName}
            onChange={(e) => setChainName(e.currentTarget.value)}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Your git repo"
            inputProps={{ 'aria-label': 'your git repo'}}
            value={repoFetch}
            onChange={(e) => setRepoFetch(e.currentTarget.value)}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Email address"
            inputProps={{ 'aria-label': 'email address'}}
            value={mail}
            onChange={(e) => setMail(e.currentTarget.value)}
          />
          <br></br>
          <br></br>
          <Divider></Divider>
          <br></br>
          <h4>Hosts:</h4>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Moc ip"
            inputProps={{ 'aria-label': 'moc host'}}
            value={mocHost}
            variant="outlined"
            onChange={(e) => setMocHost(e.currentTarget.value)}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Bootnode ip"
            inputProps={{ 'aria-label': 'bootnode host'}}
            value={bootnodeHost}
            variant="outlined"
            onChange={(e) => setBootnodeHost(e.currentTarget.value)}
          />
          <TextField
            className={classes.textField}
            id="outlined-multiline-static"
            multiline
            rows={3}
            label="Validators nodes ip"
            inputProps={{ 'aria-label': 'other host'}}
            value={otherHost}
            variant="outlined"
            onChange={(e) => setOtherHost(e.currentTarget.value)}
          />
          {/* <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="SSH key path"
            inputProps={{ 'aria-label': 'SSH key path'}}
            value={sshKeyPath}
            variant="outlined"
            onChange={(e) => setSshKeyPath(e.currentTarget.value)}
          /> */}
          <br></br>
          <br></br>
          <ButtonGroup
            orientation="horizontal"
            color="primary"
            size="large"
            aria-label="horizontal outlined primary button group"
          >
            <Button onClick={() => generateConfig()}>Generate config</Button>
            {/* <Button onClick={() => test()}>Start chain</Button> */}
            <Button onClick={() => displayConfig()}>Display configuration</Button>
          </ButtonGroup>
          <br></br>
          {/* <br></br> */}
          {/* <Divider type="horizontal"></Divider>
          <br></br>
          <h4>???:</h4> */}
          {/* <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Save name"
            inputProps={{ 'aria-label': 'chain id dest'}}
            value={nameSave}
            onChange={(e) => setNameSave(e.currentTarget.value)}
          />
          <ButtonGroup
            orientation="horizontal"
            color="primary"
            size="large"
            aria-label="horizontal outlined primary button group"
          >
            <Button onClick={() => showSavedName()}>Display saved names</Button>
          </ButtonGroup> */}
        </Paper>
        
      </div>
      <div className={classes.right}>
        <Paper variant="outlined" className={classes.container}>
          <h4>Logs:</h4>
          {logs}
          {/* {
            logs.map((el, index) => (
              <div className={index + "log"}>
                {el}
                <br/>
              </div>
            ))
          } */}
        </Paper>
      </div>
      
    </div>
  )
}

// 35.180.32.186 moc
// 35.181.48.191 other
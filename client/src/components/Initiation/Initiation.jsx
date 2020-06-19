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

export default function Initiation() {
	const classes = useStyles();

  const [waitFetchBlock, setWaitFetchBlock] = useState(false);
	const { enqueueSnackbar } = useSnackbar();
  const [logs, setLogs] = useState([]);
	const [globalState, setGlobalState ] = useTracked();

  const [ethNodeSrcURL, setEthNodeSrcURL] = useState('https://rpcmainnet1w7wagudqhtw5khzsdtv.iex.ec');
  const [ethNodeDestURL, setEthNodeDestURL] = useState('');
  const [startingBlock, setStartingBlock] = useState(9689846);
  const [endBlock, setEndBlock] = useState(9689847);
  const [chainIdDest, setChainIdDest] = useState(0);
  const [nameSave, setNameSave] = useState('test');

  const [nbWallets, setNbWallets] = useState(0);
  const [blockArray, setBlockArray] = useState([]);
  const [walletArray, setWalletArray] = useState([]);
  const [contractArray, setContractArray] = useState([]);
  const [transactionArray, setTransactionArray] = useState([]);

  const [srcWalletToID, setSrcWalletToID] = useState({});
  const [IDToNewWallet, setIDToNewWallet] = useState({});
  const [IDToContractCode, setIDToContractCode] = useState({});
  const [IDToEth, setIDToEth] = useState({});
  
  const [prom, setProm] = useState([]);
  
  var IDCounter = 0;
  var web3Provider = new ethers.providers.JsonRpcProvider("https://rpcmainnet1w7wagudqhtw5khzsdtv.iex.ec");
  
  function _setStartingBlock(_block) {
    setStartingBlock(parseInt(_block));
  }

  function _setEndBlock(_block) {
    setEndBlock(parseInt(_block));
  }

  function getTransactionOfBlock(block) {

  }

  function isContract(address) {

  }

  function fetchBlocks() {
    if(startingBlock > endBlock) {
      // return error;
    }
    
  }
 
  function startInit() {
    if(startingBlock > endBlock) {
      enqueueSnackbar("Starting block > Ending block", {variant: "error"})
    } else {
      setWaitFetchBlock(true);
      let fetches = [];

      for(let i = startingBlock; i <= endBlock; i = i+1) {
        let tmp = i;
        let hexBlock = "0x" + tmp.toString(16);
        let requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: stringify({"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":[hexBlock, true],"id":1})
        };

        fetches.push(
          fetch(ethNodeSrcURL, requestOptions)
          .then(res => res.json())
          .then(res => {
            blockArray.push(res.result);
            enqueueSnackbar(res.result.number, {variant: "success"})
          })
        )
      }

      Promise.all(fetches)
      .then(() => {
        blockArray.forEach(async (el) => {
          await setProm([]);
            parseBlock(el);
          await Promise.all(prom);
        });
      })
      .then(() => {
        Promise.all(prom).then(() => {
          setWaitFetchBlock(false);
        })
      });
    }
  }

  function parseBlock(block) {
    block.transactions.forEach(el => {
      let IDFrom = checkRegistered(el.from, el.gas, el.gasPrice, el.value);
      let IDTo = checkRegistered(el.to, el.gas, el.gasPrice, el.value);
      let tmp = {
        nonce: "",
        from: IDFrom,
        to: IDTo,
        value: el.value,
        gasLimit: el.gas,
        gasPrice: el.gasPrice,
        chainId: chainIdDest,
      }
      transactionArray.push(tmp);
    });
  }

  // check if the address is already registered and add new ID if not
  // Return the ID of the wallet
  function checkRegistered(address, gas, gasPrice, eth) {
    if(typeof(srcWalletToID[address]) != "undefined") {
      let tmp = parseInt(IDToEth[srcWalletToID[address]]) + parseInt(gas) * parseInt(gasPrice) + parseInt(eth);
      IDToEth[srcWalletToID[address]] = "0x"+tmp.toString(16);
      return srcWalletToID[address];
    } else {
      srcWalletToID[address] = genNewID();
      let tmp = parseInt(gas) * parseInt(gasPrice) + parseInt(eth);
      IDToEth[srcWalletToID[address]] = "0x"+tmp.toString(16);
      if(address !== null) {
        prom.push(
          web3Provider.getCode(address)
            .then(res => {
              if(res !== "0x") {
                IDToContractCode[srcWalletToID[address]] = res;
              }
          })
        )
      }
      return srcWalletToID[address];
    }
  }

  function genNewID() {
    IDCounter = IDCounter + 1;
    return IDCounter;
  }

  // get the ID of a wallet in oldWalletToID
  function getIDOf(address) {

  }

  // get the Wallet address of an ID in IDToNewWallet
  function getWalletOf(ID) {
    
  }

  function deployToNewChain() {
    setLogs(stringify(IDToContractCode));
  }

  function saveConfig() {
    if(nameSave === "") {
      enqueueSnackbar("Please specify a name", {variant: "error"})
    } else if(transactionArray.length === 0) {
      enqueueSnackbar("Please fetch blocks before", {variant: "error"})
    } else {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          "name": nameSave,
          "blocks": transactionArray, 
          "srcWalletToID": srcWalletToID,
          "IDToContractCode": IDToContractCode,
          "IDToEth": IDToEth
        })
      };
      fetch(globalState.expressServer + '/block/saveConfig', requestOptions)
        .then(res => res.json())
        .then(res => enqueueSnackbar(res.msg, {variant: res.type})
      );
    }
  }

  function importConfig() {
    if(nameSave === "") {
      enqueueSnackbar("Please specify a name", {variant: "error"})
    } else {
      fetch(globalState.expressServer + '/block/getConfig?name=' + nameSave)
        .then(res => res.json())
        .then(res => { 
          console.log(res.data.blocks)
          setTransactionArray(res.data.blocks);
          setSrcWalletToID(res.data.srcWalletToID);
          setIDToContractCode(res.data.IDToContractCode);
          setIDToEth(res.data.IDToEth);
          enqueueSnackbar(res.msg, {variant: res.type});
        }
      );
    }
  }

  function showSavedName() {
    fetch(globalState.expressServer + '/block/getSavedNames')
      .then(res => res.json())
      .then(res => enqueueSnackbar(res.msg, {variant: res.type})
    );
  }

  return (
    <div>
      <h1>Bench Initiation</h1>
      <div className={classes.left}>
        <Paper variant="outlined" className={classes.container}>
          <h4>Parameters:</h4>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Src node URL"
            inputProps={{ 'aria-label': 'enter src node url'}}
            value={ethNodeSrcURL}
            onChange={(e) => setEthNodeSrcURL(e.currentTarget.value)}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Dest node URL"
            inputProps={{ 'aria-label': 'enter dest node url'}}
            value={ethNodeDestURL}
            onChange={(e) => setEthNodeDestURL(e.currentTarget.value)}
          />
          <br></br>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Starting block"
            inputProps={{ 'aria-label': 'starting block'}}
            value={startingBlock}
            onChange={(e) => _setStartingBlock(e.currentTarget.value)}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Ending block"
            inputProps={{ 'aria-label': 'ending block'}}
            value={endBlock}
            onChange={(e) => _setEndBlock(e.currentTarget.value)}
          />
          <br></br>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Chain ID dest"
            inputProps={{ 'aria-label': 'chain id dest'}}
            value={chainIdDest}
            onChange={(e) => setChainIdDest(e.currentTarget.value)}
          />
          <br></br>
          <ButtonGroup
            orientation="horizontal"
            color="primary"
            size="large"
            aria-label="horizontal outlined primary button group"
          >
						{!waitFetchBlock ? <Button onClick={() => startInit()} aria-label="startInit">Fetch Blocks</Button> : <Button disabled aria-label="startInit"><CircularProgress size={50}/></Button>}
            <Button onClick={() => deployToNewChain()}>Deploy to new chain</Button>
            <Button onClick={() => console.log(blockArray)}>show block array</Button>
          </ButtonGroup>
          <br></br>
          <br></br>
          <Divider type="horizontal"></Divider>
          <br></br>
          <h4>Saves:</h4>
          <TextField
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
            <Button onClick={() => saveConfig(nameSave)}>Save Configuration</Button>
            <Button onClick={() => importConfig(nameSave)}>Import configuration</Button>
            <Button onClick={() => showSavedName()}>Display saved names</Button>
          </ButtonGroup>
        </Paper>
        
      </div>
      <div className={classes.right}>
        <Paper variant="outlined" className={classes.container}>
          
          <h4>Custom provider</h4>

          <br></br>
          <br></br>
          <Divider type="horizontal"></Divider>
          <br></br>
          <h4>Logs:</h4>
          {
            logs.map((el, index) => (
              <div className={index + "log"}>
                {el}
                <br/>
              </div>
            ))
          }

        </Paper>
      </div>
      
    </div>
  )
}
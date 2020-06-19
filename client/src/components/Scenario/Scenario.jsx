import React from 'react';
import { ethers } from 'ethers';
import { useState, useEffect } from 'react';
import { useTracked } from '../State';
import stringify from 'fast-json-stable-stringify'

import TxPerSec from '../../bench/TxPerSec'
import KillNodes from '../../bench/KillNodes'


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
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import InputLabel from '@material-ui/core/InputLabel';

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

export default function Scenario() {
  const classes = useStyles();
  const express = "http://localhost:9000";

  const [waitFetchBlock, setWaitFetchBlock] = useState(false);
	const { enqueueSnackbar } = useSnackbar();
  const [logs, setLogs] = useState("");
	const [globalState, setGlobalState ] = useTracked();
	const [scenarioType, setScenarioType ] = useState(1);
  const [form, setForm ] = useState([<TxPerSec/>, <KillNodes/>]);

  // const [repo, setRepo] = useState("");
  // const [repoFetch, setRepoFetch] = useState("nathPay");
  // const [chainName, setChainName] = useState("test");
  // const [mail, setMail] = useState("np@iex.ec");
  // const [mocHost, setMocHost] = useState("taurus-2.lyon.grid5000.fr");
  // const [bootnodeHost, setBootnodeHost] = useState("taurus-10.lyon.grid5000.fr");
  // const [otherHost, setOtherHost] = useState("taurus-11.lyon.grid5000.fr");
  // const [sshKeyPath, setSshKeyPath] = useState("");
  
  // var web3Provider = new ethers.providers.JsonRpcProvider("https://rpcmainnet1w7wagudqhtw5khzsdtv.iex.ec");

  const handleChangeType = (event) => {
    setScenarioType(event.target.value);
  };

  function test() {
  }

  function validatorFiles() {

  }

  function displayConfig() {
  }

  function genScenario() {

  }

  return (
    <div>
      <h1>Create Bench Scenario</h1>
      <div className={classes.left}>
        <Paper variant="outlined" className={classes.container}>
          <h4>Create Scenario:</h4>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Type of scenario"
            inputProps={{ 'aria-label': ''}}
            value={scenarioType}
            onChange={handleChangeType}
            select
          >
            <MenuItem value={0}>Transaction per seconds</MenuItem>
            <MenuItem value={1}>Killing nodes</MenuItem>
            {/* <MenuItem value={2}>Malicious nodes</MenuItem> */}
          </TextField>
          {/* <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label=""
            inputProps={{ 'aria-label': ''}}
            value={}
            onChange={}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label=""
            inputProps={{ 'aria-label': ''}}
            value={}
            onChange={}
          /> */}
          <br></br>
          <br></br>
          <Divider></Divider>
          <br></br>
          {
            form[scenarioType]
          }
          {/* <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Moc ip"
            inputProps={{ 'aria-label': 'moc host'}}
            value={}
            variant="outlined"
            onChange={}
          />
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Bootnode ip"
            inputProps={{ 'aria-label': 'bootnode host'}}
            value={}
            variant="outlined"
            onChange={}
          />
          <TextField
            className={classes.textField}
            id="outlined-multiline-static"
            multiline
            rows={3}
            label=""
            inputProps={{ 'aria-label': ''}}
            value={}
            variant="outlined"
            onChange={}
          /> */}
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
            <Button onClick={() => genScenario()}>Generate Scenario</Button>
            <Button onClick={() => displayConfig()}>Display configuration</Button>
          </ButtonGroup>
          <br></br>
        </Paper>
        
      </div>
      <div className={classes.right}>
        <Paper variant="outlined" className={classes.container}>
          <h4>Logs:</h4>
          {logs}

        </Paper>
      </div>
      
    </div>
  )
}

// 35.180.32.186 moc
// 35.181.48.191 other
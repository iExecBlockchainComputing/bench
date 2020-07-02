import React from 'react';
import { useState, useEffect } from 'react';
import { useTracked } from '../State';
import stringify from 'fast-json-stable-stringify'

import TxPerSec from '../../bench/TxPerSec'
// import KillNodes from '../../bench/KillNodes'


import { makeStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import { useSnackbar } from 'notistack';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Paper from '@material-ui/core/Paper';
import TextField from '@material-ui/core/TextField';
import Divider from '@material-ui/core/Divider';
import MenuItem from '@material-ui/core/MenuItem';
import KillNodes from '../../bench/KillNodes';

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

  const TYPE_OF_SCENARIOS = ["Tx Per sec", "Kill Nodes", "Malicious Nodes"];
  // const CONTENT_BY_TYPE = [<TxPerSec id={index}/>, <KillNodes/>]

  const [expanded, setExpanded] = useState(false);
  const [waitFetchBlock, setWaitFetchBlock] = useState(false);
	const { enqueueSnackbar } = useSnackbar();
	const [globalState, setGlobalState ] = useTracked();
  const [scenarioType, setScenarioType ] = useState(0);
  const [time, setTime] = useState(1000);
  const [scenarioName, setScenarioName] = useState("test");

  const handleChangePanel = panel => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
  };

  function addEvent() {
    globalState.events.push({"type": scenarioType, "time": time})
    setScenarioType(0);
    setTime(time+1);
  }

  function test() {
  }

  function validatorFiles() {

  }

  function displayConfig() {
    console.log(globalState.events);
  }

  function genScenario() {
    let requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: stringify({
        'events': globalState.events,
        scenarioName
      })
    };
    fetch(express + '/scenario/genScenario', requestOptions)
    .then(() => {
      enqueueSnackbar("successfully created", {variant: "success"})
    });
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
            onChange={(e) => setScenarioType(e.target.value)}
            select
          >
            <MenuItem value={0}>Transaction per seconds</MenuItem>
            <MenuItem value={1}>Killing nodes</MenuItem>
            {/* <MenuItem value={2}>Malicious nodes</MenuItem> */}
          </TextField>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="At (ms)"
            inputProps={{ 'aria-label': 'at (ms)'}}
            value={time}
            onChange={(e) => setTime(e.target.value)}
          />
          <br></br>
          <br></br>
          <Button size="large" variant="contained" color="primary" onClick={() => addEvent()}>Add Event</Button>
          <br></br>
          <br></br>
          <Divider></Divider>
          <br></br>
          <TextField
            className={classes.textField}
            id="outlined-basic"
            variant="outlined"
            label="Scenario Name"
            inputProps={{ 'aria-label': 'Scenario Name'}}
            value={scenarioName}
            onChange={(e) => setScenarioName(e.target.value)}
          />
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
          <h4>Scenario:</h4>
          {globalState.events.map((el, index) => (
					<ExpansionPanel expanded={expanded === index } onChange={handleChangePanel(index)}>
						<ExpansionPanelSummary
							expandIcon={<ExpandMoreIcon />}
							aria-controls="panel1bh-content"
							id="panel1bh-header"
						>
							<Typography noWrap className={classes.heading}>{"Event Type: " + TYPE_OF_SCENARIOS[el.type] + " | At: " + el.time + "sec"}</Typography>
						</ExpansionPanelSummary>
						<ExpansionPanelDetails>
              { el.type === 0 ? <TxPerSec id={index}/> : <KillNodes id={index}/>}
						</ExpansionPanelDetails>
					</ExpansionPanel>
					))}

        </Paper>
      </div>
      
    </div>
  )
}
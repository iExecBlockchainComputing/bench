import React from 'react';
import TextField from '@material-ui/core/TextField';
import { useState, useEffect } from 'react';

import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  textField: {
    margin: theme.spacing(1),
    flex: 1,
  },
}));

export default function TxPerSec() {
  const classes = useStyles();

	const [nbTransaction, setNbTransaction ] = useState(2000);
	const [timeBetween2Tx, setTimeBetween2Tx ] = useState(1);
	// const [scenarioType, setScenarioType ] = useState(0);

	return (
    <div>
  		<h4>Scenario: Transaction per seconds</h4>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Number of transaction"
        inputProps={{ 'aria-label': ''}}
        value={nbTransaction}
        onChange={(e) => setNbTransaction(e.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Time between 2 transactions"
        inputProps={{ 'aria-label': ''}}
        value={timeBetween2Tx}
        onChange={(e) => setTimeBetween2Tx(e.value)}
      />
      <br></br>
      {/* <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label=""
        inputProps={{ 'aria-label': ''}}
        // value={}
        // onChange={}
      />
      <br></br> */}

    </div>
	);
}
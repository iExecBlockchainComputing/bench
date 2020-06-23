import React from 'react';
import TextField from '@material-ui/core/TextField';
import { useState, useEffect } from 'react';
import { useTracked } from '../../components/State';

import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  textField: {
    margin: theme.spacing(1),
    flex: 1,
  },
}));

export default function TxPerSec(props) {
  const classes = useStyles();

	const [ nbTx, setNbTx ] = useState("2000");
	const [ timeBetween2Tx, setTimeBetween2Tx ] = useState("1");
	const [ priority, setPriority ] = useState("1");
	const [ globalState, setGlobalState ] = useTracked();

  useEffect(() => {
		globalState.events[props.id] = {...globalState.events[props.id], "priority": priority, "timeBetween2Tx": timeBetween2Tx, "nbTx": nbTx};
  }, []);

  function _setNbTx(value) {
    setNbTx(value);
    globalState.events[props.id].nbTx = value;
  }

  function _setTimeBetween2Tx(value) {
    setTimeBetween2Tx(value);
    globalState.events[props.id].timeBetween2Tx = value;
  }
  
  function _setPriority(value) {
    setPriority(value);
    globalState.events[props.id].priority = value;
  }

	return (
    <div>
  		<h4>Scenario: Transaction per seconds</h4>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Number of transaction"
        inputProps={{ 'aria-label': ''}}
        value={nbTx}
        onChange={(e) => _setNbTx(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Time between 2 transactions (s)"
        inputProps={{ 'aria-label': ''}}
        value={timeBetween2Tx}
        onChange={(e) => _setTimeBetween2Tx(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Priority"
        inputProps={{ 'aria-label': ''}}
        value={priority}
        onChange={(e) => _setPriority(e.target.value)}
      />
    </div>
	);
}
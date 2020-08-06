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

	const [ nbTx, setNbTx ] = useState("67");
	const [ during, setDuring ] = useState("30");
	const [ priority, setPriority ] = useState("1");
	const [ globalState, setGlobalState ] = useTracked();

  useEffect(() => {
    globalState.events[props.id] = {...globalState.events[props.id], 
      "priority": priority, 
      "during": during, 
      "nbTx": nbTx
    };
  }, []);

  function _setNbTx(value) {
    setNbTx(value);
    globalState.events[props.id].nbTx = value;
  }

  function _setDuring(value) {
    setDuring(value);
    globalState.events[props.id].during = value;
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
        label="Transaction per Sec"
        inputProps={{ 'aria-label': ''}}
        value={nbTx}
        onChange={(e) => _setNbTx(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="During time (s)"
        inputProps={{ 'aria-label': ''}}
        value={during}
        onChange={(e) => _setDuring(e.target.value)}
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
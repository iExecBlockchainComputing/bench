import React from 'react';
import TextField from '@material-ui/core/TextField';
import { useState, useEffect } from 'react';
import { useTracked } from '../../components/State';

import { makeStyles } from '@material-ui/core/styles';
import Checkbox from '@material-ui/core/Checkbox';
import CheckBoxOutlineBlankIcon from '@material-ui/icons/CheckBoxOutlineBlank';
import CheckBoxIcon from '@material-ui/icons/CheckBox';
import FormControlLabel from '@material-ui/core/FormControlLabel';

const useStyles = makeStyles(theme => ({
  textField: {
    margin: theme.spacing(1),
    flex: 1,
  },
}));

export default function KillNodes(props) {
  const classes = useStyles();

	const [ reUpAt, setReUpAt ] = useState(100);
  const [ priority, setPriority ] = useState(1);
  const [ nbNodes, setNbNodes ] = useState(1);
  const [ bootnode, setBootnode ] = useState(false);
  // const [ moc, setMoc ] = useState(false);
  const [ validators, setValidators ] = useState(true);
  const [ globalState, setGlobalState ] = useTracked();

  useEffect(() => {
    globalState.events[props.id] = {
      ...globalState.events[props.id],
      priority,
      reUpAt,
      nbNodes,
      bootnode,
      validators
    };
  }, []);

  function _setBootnode(event) {
    setBootnode(event.target.checked);
    globalState.events[props.id] = {
      ...globalState.events[props.id], 
      "bootnode": event.target.checked
    };
  }

  // function _setMoc(event) {
  //   setMoc(event.target.checked);
  //   globalState.events[props.id] = {
  //     ...globalState.events[props.id], 
  //     "moc": event.target.checked
  //   };
  // }

  function _setValidators(event) {
    setValidators(event.target.checked);
    globalState.events[props.id] = {
      ...globalState.events[props.id], 
      "validators": event.target.checked
    };
  }

  function _setReUpAt(value) {
    setReUpAt(value);
    globalState.events[props.id].timeBeforeReUp = value;
  }

  function _setNbNodes(value) {
    setNbNodes(value);
    globalState.events[props.id].nbNodes = value;
  }
  
  function _setPriority(value) {
    setPriority(value);
    globalState.events[props.id].priority = value;
  }

	return (
    <div>
  		<h4>Scenario: Kill Nodes</h4>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="reUp nodes at"
        inputProps={{ 'aria-label': ''}}
        value={reUpAt}
        onChange={(e) => _setReUpAt(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Number of Down validators"
        inputProps={{ 'aria-label': ''}}
        value={nbNodes}
        onChange={(e) => _setNbNodes(e.target.value)}
      ></TextField>
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
      <br></br>
      <h5>Type of nodes</h5>
      <FormControlLabel
        control={
          <Checkbox
            checked={bootnode}
            onChange={_setBootnode}
            name="bootnode"
            color="primary"
          />
        }
        label="Bootnode"
      />
      <FormControlLabel
        control={
          <Checkbox
            checked={validators}
            onChange={_setValidators}
            name="validators"
            color="primary"
          />
        }
        label="Validators"
      />
    </div>
	);
}
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

export default function NetworkDegradation(props) {
  const classes = useStyles();

  const [ restoreAt, setRestoreAt ] = useState(100);
  const [ priority, setPriority ] = useState(1);
  const [ nbNodes, setNbNodes ] = useState(1);
  const [ bootnode, setBootnode ] = useState(false);
  const [ validators, setValidators ] = useState(true);
  const [ latency, setLatency ] = useState(100);
  const [ download, setDownload ] = useState(1024);
  const [ upload, setUpload ] = useState(1024);
  const [ globalState, setGlobalState ] = useTracked();

  useEffect(() => {
    globalState.events[props.id] = {
      ...globalState.events[props.id],
      priority,
      restoreAt,
      nbNodes,
      bootnode,
      validators,
      latency,
      download,
      upload
    };
  }, []);

  function _setBootnode(event) {
    setBootnode(event.target.checked);
    globalState.events[props.id] = {
      ...globalState.events[props.id], 
      "bootnode": event.target.checked
    };
  }

  function _setValidators(event) {
    setValidators(event.target.checked);
    globalState.events[props.id] = {
      ...globalState.events[props.id], 
      "validators": event.target.checked
    };
  }

  function _setRestoreAt(value) {
    setRestoreAt(value);
    globalState.events[props.id].restoreAt = value;
  }

  function _setNbNodes(value) {
    setNbNodes(value);
    globalState.events[props.id].nbNodes = value;
  }
  
  function _setPriority(value) {
    setPriority(value);
    globalState.events[props.id].priority = value;
  }

  function _setLatency(value) {
    setLatency(value);
    globalState.events[props.id].latency = value;
  }
  
  function _setDownload(value) {
    setDownload(value);
    globalState.events[props.id].download = value;
  }

  function _setUpload(value) {
    setUpload(value);
    globalState.events[props.id].upload = value;
  }

	return (
    <div>
  		<h4>Scenario: Network Degradation</h4>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Restore network at "
        inputProps={{ 'aria-label': ''}}
        value={restoreAt}
        onChange={(e) => _setRestoreAt(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Number of affected validators"
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
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Latency (ms)"
        inputProps={{ 'aria-label': ''}}
        value={latency}
        onChange={(e) => _setLatency(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Download (kbs)"
        inputProps={{ 'aria-label': ''}}
        value={download}
        onChange={(e) => _setDownload(e.target.value)}
      />
      <br></br>
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label="Upload (kbs)"
        inputProps={{ 'aria-label': ''}}
        value={upload}
        onChange={(e) => _setUpload(e.target.value)}
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
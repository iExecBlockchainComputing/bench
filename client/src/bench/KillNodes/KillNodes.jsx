import React from 'react';
import TextField from '@material-ui/core/TextField';
import { useState, useEffect } from 'react';

import { makeStyles } from '@material-ui/core/styles';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import ListItem from '@material-ui/core/ListItem';
import Icon from '@material-ui/core/Icon';
import RemoveCircleIcon from '@material-ui/icons/RemoveCircle';
import AddCircleIcon from '@material-ui/icons/AddCircle';

const useStyles = makeStyles(theme => ({
  textField: {
    margin: theme.spacing(1),
    flex: 1,
  },
}));

export default function KillNodes() {
  const classes = useStyles();
  const [expanded, setExpanded] = useState(false);

	const [nbTransaction, setNbTransaction ] = useState(2000);
	const [timeBetween2Tx, setTimeBetween2Tx ] = useState(1);
	const [nbDown, setNbDown ] = useState(4);
	const [timeBetween2Down, setTimeBetween2Down ] = useState([""]);
	const [downDate, setDownDate ] = useState([""]);
	const [nbDownNodes, setNbDownNodes ] = useState([""]);
	const [timeToUp, setTimeToUp ] = useState([""]);
  const [panelSize, setPanelSize] = useState([""]);

  const handleChange = panel => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
	};

  function _setNbDown(el) {
    setNbDown(el)
    let tmp = [];
    for(let i = 0; i < nbDown; i++) {
      tmp.push("");
    }

  }

	return (
    <div>
  		<h4>Scenario: Kill Nodes</h4>
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
      <TextField
        className={classes.textField}
        id="outlined-basic"
        variant="outlined"
        label=""
        inputProps={{ 'aria-label': ''}}
        value={nbDown}
        onChange={(e) => _setNbDown(e.value)}
      ><RemoveCircleIcon color="primary"/></TextField>
      <br></br>
      {panelSize.map((el, index) => (
					<ExpansionPanel expanded={expanded === index } onChange={handleChange(index)}>
						<ExpansionPanelSummary
							expandIcon={<ExpandMoreIcon />}
							aria-controls="panel1bh-content"
							id="panel1bh-header"
						>
							{/* <Typography noWrap className={classes.heading}>{wallet.address}</Typography> */}
						</ExpansionPanelSummary>
						<ExpansionPanelDetails>
							{/* <ListItem><Typography noWrap>Private Key: {wallet.privateKey}</Typography></ListItem> */}
						</ExpansionPanelDetails>
					</ExpansionPanel>
					))}
    </div>
	);
}
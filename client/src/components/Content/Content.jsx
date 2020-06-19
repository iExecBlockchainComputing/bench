import React from 'react';
import { useTracked } from '../State';

import WalletManager from '../WalletManager';
import PoaNetwork from '../PoaNetwork'
import Scenario from '../Scenario'
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  main: {
    textAlign: 'center',
  }
}));

export default function Content(props) {
  const classes = useStyles();

  const [globalState] = useTracked();

  function displayPage(activePage) {
    switch (activePage) {
      case "walletManager":
        return <WalletManager/>;
      case "poaNetwork":
        return <PoaNetwork/>;
      case "scenario":
        return <Scenario/>;
      default:
        return <WalletManager/>;
    }
  }

		return (
      <div className={classes.main}>
        {displayPage(globalState.page)}
      </div>
    );
}
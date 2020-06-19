import React from 'react';
import Bar from '../Bar';

import { Provider } from '../State';

import { makeStyles } from '@material-ui/core/styles';
import { SnackbarProvider } from 'notistack';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
  },
}));

export default function App() {
  const classes = useStyles();

  return (
      <div className={classes.root}>
        <SnackbarProvider autoHideDuration={3000}>
          <Provider>
            <Bar/>
          </Provider>
        </SnackbarProvider>
      </div>
    );
}
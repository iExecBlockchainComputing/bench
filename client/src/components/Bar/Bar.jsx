import React from 'react';
import { ethers } from 'ethers';
import { useTracked, getEthNetwork } from '../State';
import clsx from 'clsx';
import Content from '../Content'

import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import AccountBalanceWalletIcon from '@material-ui/icons/AccountBalanceWallet';
import { Menu, MenuItem, Button } from '@material-ui/core';
import { useSnackbar } from 'notistack';


const drawerWidth = 240;

const useStyles = makeStyles(theme => ({
  menuButton: {
    marginRight: theme.spacing(2),
  },
  drawer: {
    width: drawerWidth,
  },
  title: {
    flexGrow: 1,
  },
  content: {
    padding: theme.spacing(3),
  },
  toolbar: theme.mixins.toolbar,
}));


export default function Bar() {
  const classes = useStyles();
	const { enqueueSnackbar } = useSnackbar();

  const [ globalState, setGlobalState ] = useTracked();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [open, setOpen] = React.useState(false);

  function handleChangePage(index) {
    setGlobalState({page: index});
  };

  const changeProvider = (value) => {
    setGlobalState({ethProvider: value, reload: true});
    setAnchorEl(null);
  };

  const handleClick = event => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const toggleDrawer = (el) => () => {
    setOpen(el);
  };

	function addWallet(wallet) {
		setGlobalState({wallets: globalState.wallets.concat(wallet)})
  }
  
  function reloadConf() {
    fetch( globalState.expressServer + "/wallets/importAllWallets")
    // .then(res => res.text())
    .then(res => res.json())
    .then(res => {
      setGlobalState({wallets: []});
      addWallet(res.map( (el) => {
        return new ethers.Wallet(el.privateKey);
      }))
    })
    .then(() => {
		  enqueueSnackbar('Configuration successfully loaded', { variant: 'success'})
    })

  }

  const leftDrawer = () => (
    <div 
      className={classes.list}
      role="presentation"
      onClick={toggleDrawer(false)}
      onKeyDown={toggleDrawer(false)}
    >
    <Divider/>
    <List>
      <ListItem button key="Wallet Manager" onClick={() => handleChangePage("walletManager")}>
      <ListItemIcon><AccountBalanceWalletIcon/></ListItemIcon>
        <ListItemText primary="Wallet Manager"/>
      </ListItem>
      <Divider/>
      <ListItem button key="PoA Network" onClick={() => handleChangePage("poaNetwork")}>
        <ListItemText primary="PoA Network"/>
      </ListItem>
      <Divider/>
      <ListItem button key="Scenario Creator" onClick={() => handleChangePage("scenario")}>
        <ListItemText primary="Scenario Creator"/>
      </ListItem>
    </List>
  </div>
  );

  return (
    <div>
      <CssBaseline />
      <AppBar position="fixed">
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={toggleDrawer(true)}
            edge="start"
            className={clsx(classes.menuButton, open && classes.hide)}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap className={classes.title}>
            Chain Benchmark
          </Typography>
          <Button color="inherit" onClick={() => reloadConf()}>
            reload configuration
          </Button>
          <Button color="inherit" aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick}>
            {globalState.ethProvider === "" ?
              "No eth Provider" : getEthNetwork(globalState)
            }
          </Button>
          <Menu
            id="simple-menu"
            anchorEl={anchorEl}
            keepMounted
            open={Boolean(anchorEl)}
            onClose={handleClose}
          >
            <MenuItem onClick={() => changeProvider("")} >Disconnect</MenuItem>
            <MenuItem onClick={() => changeProvider(ethers.getDefaultProvider('kovan'))}>Kovan</MenuItem>
            <MenuItem onClick={() => changeProvider(ethers.getDefaultProvider('mainnet'))}>Mainnet</MenuItem>
          </Menu>
        </Toolbar>
      </AppBar>
      <Drawer open={open} onClose={toggleDrawer(false)}>
          {leftDrawer()}
      </Drawer>

      <main className={classes.content}>
        <div className={classes.toolbar} />
        <Content/>
      </main>
    </div>

  );
}
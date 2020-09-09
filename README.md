# Generic benchmark framwork for blockchain
3 tabs compose the application:

## Wallet Manager
Permit wallet management: create, save, reload.
MainWallet is the MOC Wallet for PoA deployement. (can be something else for other blockchain deployment in hte future)
Others are used for validators.

Saving wallet configuration is possible by pressing the "Export Wallets" button

Saved wallets are in `server/wallets/` and it is possible to reload the configuration by pressing "Reload Configuration" at the top right corner.

## PoA Network
This is for PoA deployment automatic configuration generation.

The deployment scripts are usable on any infrastructure that can run ansible.

It is important to load wallets before generating the configuration.

/!\ Refresh the interface reset the cache automatically. You will have to "reload configuration" again.

Text input "validators nodes ip" have to be formatted following this pattern: ip,ip

## Scenario Creator
Create and generate complex scenarios.

In the right section all the events are displayed. A click on an event button display more configuration about it.

A Python program is generated in server side in `server/scenario/`. This script is the event injector.

## How it's work ?

### Start server
`npm i` in `server` folder then `npm start`

### Start client
`npm i` in `client` folder then `npm start`

### Starting PoA deployment

1. Generate or reload wallets (minimum 1 by node)
2. Generate PoA Network configuration
3. Copy `server/repos/poa-deployement-bench/` in a computer that run ansible and can access to other nodes.
4. Run `export ANSIBLE_HOST_KEY_CHECKING=False`
5. Run `ansible-playbook -i hosts site.yml`

### Starting benchmark

1. Generate scenario (using the interface)
2. Copy the higher folder number from `server/scenarios/` in the same computer which has deployed the chain.
3. Copy the scenario folder to all nodes and move the content of folder `0` in the same level as `scenario.py`
4. Run `python3 ./scenario.py`

/!\ The script can end before the full transaction injection. Please check parity logs in a node to check if some transactions are still mined.

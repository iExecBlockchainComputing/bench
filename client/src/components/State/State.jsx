import { useReducer } from 'react';

import { createContainer } from 'react-tracked';
import { ethers } from 'ethers';


const initialState = {
  wallets: [],
  page: "poaNetwork",
  ethProvider: ethers.getDefaultProvider('kovan'),
  testedChainProvider: [],
  mainWallet: {"signingKey":{"address":"0x1f23f42c865d7D580C5850fCf13518307C2fa567","keyPair":{"compressedPublicKey":"0x03f8f4653d0a81a4b3498396a803a3fadbad4b0e309e830615ad92c47c80f72d91","privateKey":"0xaadbffbda78a7b1e7e98acb801cfe9fac326f0ce0c9c90a48fc9535fb83d7b76","publicKey":"0x04f8f4653d0a81a4b3498396a803a3fadbad4b0e309e830615ad92c47c80f72d915422b5939c943a834859a8a2f636a07908b6ef082e73bee55e4ed2a7df7ac9bb","publicKeyBytes":[3,248,244,101,61,10,129,164,179,73,131,150,168,3,163,250,219,173,75,14,48,158,131,6,21,173,146,196,124,128,247,45,145]},"mnemonic":"canoe elegant cargo estate wisdom trial garlic swing congress skull put vocal","path":"m/44'/60'/0'/0/0","privateKey":"0xaadbffbda78a7b1e7e98acb801cfe9fac326f0ce0c9c90a48fc9535fb83d7b76","publicKey":"0x04f8f4653d0a81a4b3498396a803a3fadbad4b0e309e830615ad92c47c80f72d915422b5939c943a834859a8a2f636a07908b6ef082e73bee55e4ed2a7df7ac9bb"}},
  reload: true,
  expressServer: "http://localhost:9000",
};

// {"signingKey":{"address":"0x1f23f42c865d7D580C5850fCf13518307C2fa567","keyPair":{"compressedPublicKey":"0x03f8f4653d0a81a4b3498396a803a3fadbad4b0e309e830615ad92c47c80f72d91","privateKey":"0xaadbffbda78a7b1e7e98acb801cfe9fac326f0ce0c9c90a48fc9535fb83d7b76","publicKey":"0x04f8f4653d0a81a4b3498396a803a3fadbad4b0e309e830615ad92c47c80f72d915422b5939c943a834859a8a2f636a07908b6ef082e73bee55e4ed2a7df7ac9bb","publicKeyBytes":[3,248,244,101,61,10,129,164,179,73,131,150,168,3,163,250,219,173,75,14,48,158,131,6,21,173,146,196,124,128,247,45,145]},"mnemonic":"canoe elegant cargo estate wisdom trial garlic swing congress skull put vocal","path":"m/44'/60'/0'/0/0","privateKey":"0xaadbffbda78a7b1e7e98acb801cfe9fac326f0ce0c9c90a48fc9535fb83d7b76","publicKey":"0x04f8f4653d0a81a4b3498396a803a3fadbad4b0e309e830615ad92c47c80f72d915422b5939c943a834859a8a2f636a07908b6ef082e73bee55e4ed2a7df7ac9bb"}}
const useValue = () => useReducer(
  (state, newValue) => ({ ...state, ...newValue }),
  initialState
);

export function checkEthProvider(state) {
  if(state.ethProvider === "") {
    return false;
  }
  return true;
}

export function getEthNetwork(state) {
  return state.ethProvider._network.name;
}

export const { Provider, useTracked } = createContainer(useValue);
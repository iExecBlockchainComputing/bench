import ethers from 'ethers';

function cycleTransaction(provider, signedTransactions, wallets, gap, time, nbTransactions) {
  wallets.forEach((wallet, it) => {
    index = 0;
    while(index < nbTransaction) {
      signedTransactions[it][index].then((signedTx) => {

        provider.sendTransaction(signedTx)
        .then((tx) => {
          provider.waitForTransaction(tx.hash)
          .then((tx) => {
            // setWaitTransaction(false);
            enqueueSnackbar("Transaction to " + tx.to + " mined", {variant: "success"})
            // setGlobalState({reload: true});
          })
        })
      });
      index = index+1;
    }
  })
}
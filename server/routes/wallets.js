var express = require('express');
var router = express.Router();
var fs = require('fs');
var fsPromise = require('fs').promises;
var path = require('path');
var async = require('async');
var shell = require('shelljs');

var walletDirectory = "./wallets";

router.get('/exportMain', function(req, res, next) {
  let tmp = JSON.parse(req.query.main);
  if(!fs.existsSync(walletDirectory +'/mainWallet/'+ tmp.signingKey.address+ ".json")) {
    fs.writeFile(walletDirectory+'/mainWallet/'+ tmp.signingKey.address + ".json", JSON.stringify(tmp), (err) => {
      if(err) {
        res.send(JSON.stringify({type: "error", msg: err}));
      } else {
        res.send(JSON.stringify({type: "success", msg:"Main Wallet exported"}));
      }
    })
  } else {
    res.send(JSON.stringify({type: "info", msg:"Wallet already exported"}));
  }
});

router.get('/export', function(req, res, next) {
  let tmp = JSON.parse(req.query.array);
  tmp.map((el, index) => (
    fs.writeFile(walletDirectory+'/wallet' + index + ".json", '{ "privateKey": ' + el + '}', (err) => {
      if(err) {
        res.send(JSON.stringify({type: "error", msg: err}));
      }
    })
  ));
  res.send(JSON.stringify({type: "success", msg:"Wallets exported"}));
});

router.get('/deleteAll', function(req, res, next) {
  fs.readdir(walletDirectory, (err, files) =>{
    if(err) throw err;
    for(const file of files) {
      if(file !== "mainWallet") {
        fs.unlink(path.join(walletDirectory, file), (err) => {
          if(err) {
            res.send(JSON.stringify({type: "error", msg: err}));
          }
        });
      }
    }
  });
  res.send(JSON.stringify({type: "success", msg:"Wallets deleted"}));
});

router.get('/importAllWallets', function(req, res, next) {
  let arr = [];
  let count = 0;
  fsPromise.readdir(walletDirectory, (err) => {
    if(err) throw err;
  }).then( (files) => {
    files.forEach( (file) => {
      if(file !== "mainWallet") {
        fsPromise.readFile(path.join(walletDirectory, file), 'utf8', (err) => {
          if(err) throw err;
          // res.write(data.toString())
        }).then( (data) => {
          arr.push(JSON.parse(data));
          count = count+1;
        }).then(() => {
          if(count >= files.length - 1) {
            res.send(arr);
          }
        })
      }
    })
  })

  // fsPromise.readdir(walletDirectory, (err, files) => {
  //   if(err) throw err;
  //   for(const file of files) {
  //     if(file !== "mainWallet") {
  //       fs.readFile(path.join(walletDirectory, file), 'utf8', (err, data) => {
  //         if(err) throw err;
  //         // res.write(data.toString());
  //         arr.concat(data.toString());
  //         console.log(arr)
  //       });
  //     }
  //   }
  //   return arr;
  // }).then( (el) => {
  //   res.send(el);
  // });
});

router.get('/getEncryptedWallet', function(req, res) {
  shell.exec("iexec wallet import " + req.query.privKey + " --password whatever --raw | jq .wallet > ./encryptedWallet/wallet.json");
  // fsPromise.readFile('./encryptedWallet/wallet.json', 'utf8', (err) => {
  //   if(err) throw err;
  // }).then( data => {
  //   res.send(data);
  // })
  res.send(JSON.stringify({type: "success", msg: "Wallet is now encrypted"}));
});

module.exports = router;
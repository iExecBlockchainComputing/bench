var express = require('express');
var router = express.Router();
var fs = require('fs');
var fsPromise = require('fs').promises;
var path = require('path');
var async = require('async');

var blockSaveDirectory = "./block";

module.exports = router;

router.get('/getConfig', function(req, res, next) {
  fs.readdir(blockSaveDirectory + "/" + req.query.name, (err, files) => {
    if(err) {
      res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
    } else {
      let tmpData = {
        blocks: "", 
        srcWalletToID: "",
        IDToContractCode: "",
        IDToEth: ""
      };
      let prom = [];
      files.forEach(file => {
        prom.push(fsPromise.readFile(path.join(blockSaveDirectory, req.query.name, file), "utf8", (err) => {
          if(err) {
            res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
          }
        }).then(data => {
          file === "blocks.json" ? tmpData.blocks = data 
          : file === "srcWalletToID.json" ? tmpData.srcWalletToID = data
          : file === "IDToContractCode.json" ? tmpData.IDToContractCode = data
          : tmpData.IDToEth = data;
        }));
      });
      Promise.all(prom).then(() => {
        res.send(JSON.stringify({type: "success", msg: "Successfully imported", data: tmpData}));
      })
    }
  });
});

router.post('/saveConfig', function(req, res, next) {
  let prom = [];
  fsPromise.mkdir(path.join(blockSaveDirectory, req.body.name), (err) => {
    if (err) {
      res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
    }
  })
  .then(() => {
    prom.push(fsPromise.writeFile(blockSaveDirectory + '/' + req.body.name + '/blocks.json', JSON.stringify(req.body.blocks), (err) => {
      if (err) {
        res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
      }
    }));
    prom.push(fsPromise.writeFile(blockSaveDirectory + '/' + req.body.name + '/srcWalletToID.json', JSON.stringify(req.body.srcWalletToID), (err) => {
      if (err) {
        res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
      }
    }));
    prom.push(fsPromise.writeFile(blockSaveDirectory + '/' + req.body.name + '/IDToContractCode.json', JSON.stringify(req.body.IDToContractCode), (err) => {
      if (err) {
        res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
      }
    }));
    prom.push(fsPromise.writeFile(blockSaveDirectory + '/' + req.body.name + '/IDToEth.json', JSON.stringify(req.body.IDToEth), (err) => {
      if (err) {
        res.send(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
      }
    }));
  });
  Promise.all(prom).then(() => {
    res.send(JSON.stringify({type: "success", msg: "Successfully saved"}));
  });
});

router.get('/getSavedNames', function(req, res, next) {
  let filesNames = [];
  fsPromise.readdir(blockSaveDirectory, (err, dirs) => {
    console.log(dirs);
    if(err) {
      res.end(JSON.stringify({type: "error", msg: JSON.stringify(err)}));
    }
  }).then(dirs => {
    for(const dir of dirs) {
      filesNames.push(dir);
    }
  }).then(() => {
    res.send(JSON.stringify({type: "success", msg: JSON.stringify(filesNames)}));
  })
});
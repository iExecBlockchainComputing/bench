const fs = require('fs');
const { resolve } = require('path');
const { reject } = require('async');
var fsPromise = require('fs').promises;

var res = "";
const reg = /.json$/;

fsPromise.readdir("./", (err) => {
    if(err) throw err;
  }
)
.then(files => {
  files.forEach(file => {
    if(reg.test(file)) {
      res = res + fs.readFileSync(file).slice(1, -1) + ",";
    }
  });
})
.then(() => {
  res = res.slice(0, -1);
  fs.writeFileSync("./results.json", "[" + res.toString() + "]");
})
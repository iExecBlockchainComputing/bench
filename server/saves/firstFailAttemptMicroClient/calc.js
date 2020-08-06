const fs         = require('fs');

var txs = JSON.parse(fs.readFileSync('./results.json'));

let tmp1 = 0;
let tmp2 = 0;
let res = 0;

for (let i = 0; i < txs.length - 1; i++) {
    res = txs[i + 1].start - txs[i].start + res;
    
}
console.log(res/200);
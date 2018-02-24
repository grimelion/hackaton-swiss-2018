const neo = require('neo-api');
const local = neo.node('http://localhost:30333');

local.getConnectionCount().then(res => console.log(res)).catch(err => console.log('Dropped with: ', err));

local.getBlockCount().then((result) => {
    console.log('Current block height: ' + result);
});
local.getLastBlockHash().then((result) => {
    console.log('Hash of last block: ' + result);
});
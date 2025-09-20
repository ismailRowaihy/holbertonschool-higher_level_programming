#!/usr/bin/node
const { argv } = require('node:process');
const isNum = parseInt(argv[3], 10);

if (isNaN(isNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${isNum}`);
}

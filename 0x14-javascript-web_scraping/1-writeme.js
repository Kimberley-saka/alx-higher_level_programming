#!/usr/bin/node
const fs = require('fs');

const fileToWriteTo = process.argv[2];
const data = process.argv[3];

fs.writeFile(fileToWriteTo, data, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});

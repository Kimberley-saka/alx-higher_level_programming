#!/usr/bin/node
const fs = require('fs');

const fileToRead = process.argv[2];

fs.readFile(fileToRead, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(data);
});

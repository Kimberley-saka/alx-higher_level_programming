#!/usr/bin/node
const fs = require('fs');

const fileToRead = process.argv[1];

fs.readFile(fileToRead, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(data);
});

#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  fs.writeFile(file, body, 'utf8', function (err) {
    if (error) {
      console.log(error);
    }
  });
});

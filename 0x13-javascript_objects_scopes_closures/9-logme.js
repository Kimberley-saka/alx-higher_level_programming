#!/usr/bin/node
/*
prints the number of arguments already printed and
the new argument value
*/
let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};

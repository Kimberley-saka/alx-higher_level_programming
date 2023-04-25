#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const taskCompleted = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !taskCompleted[userId]) {
        taskCompleted[userId] = 0;
      }

      if (completed) ++taskCompleted[userId];
    }

    console.log(taskCompleted);
  }
});

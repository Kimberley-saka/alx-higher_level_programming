#!/bin/bash
#Displays HTTP Methods accepted by server
curl -sS -I -X OPTIONS $1 | grep "^Allow:"

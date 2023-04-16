#!/bin/bash
# Displays the status cod eof a response 
curl -s -o /dev/null -w "%{http_code}" "$1"

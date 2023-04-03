#!/bin/bash
# Displays the status cod eof a response 
curl -s -w "%{http_code}" "$1"

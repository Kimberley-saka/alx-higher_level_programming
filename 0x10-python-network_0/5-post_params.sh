#!/bin/bash
#Send a post request with data
curl -sS -X POST -d "email=test@gmail&subject=I will always be here for PLD" "$1"

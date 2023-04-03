#!/bin/bash
#Send a post request with data
curl -sS -X $1 POST -d "email=test@gmail&subject=I will always be here for PLD"

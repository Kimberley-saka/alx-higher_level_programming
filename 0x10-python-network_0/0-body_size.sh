#!/bin/bash
#Displays size of bosy of URL response
curl -sS $1 | wc -c

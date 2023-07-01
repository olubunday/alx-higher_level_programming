#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me
curl -s -X POST -d "user_id=98" "http://0.0.0.0:5000/catch_me" -o /dev/null -w "You got me!"

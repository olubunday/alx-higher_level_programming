#!/bin/bash
# make a specific request to solve a puzzle
curl -Ls -X PUT -d 'user_id=98' -H 'Origin: X-School' 0.0.0.0:5000/catch_me

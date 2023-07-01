#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me and displays the response
curl -X PUT -d "user_id=98" "http://0.0.0.0:5000/catch_me"

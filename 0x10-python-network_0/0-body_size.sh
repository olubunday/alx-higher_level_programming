#!/bin/bash
# Script to get the size of the response body in bytes
curl -Is "$@" | grep -Pio '(?<=Content-Length:)\s+\d+' | tr -d ' '

#!/bin/bash
# Script to get the size of the response body in bytes
echo "Response body size: $(curl -s "$1" | wc -c) bytes"

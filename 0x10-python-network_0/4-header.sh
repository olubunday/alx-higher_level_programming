#!/bin/bash
# make a request with an extra header
curl -s -H 'X-School-User-Id: 98' "$@"

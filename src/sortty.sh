#!/bin/bash

if [ -d /usr/local/bin/sortty-bin/ ]; then
  python3 /usr/local/bin/sortty-bin/sortty.py $1 $2 $3 $4 $5 $6
else
  python3 src/sortty.py $1 $2 $3 $4 $5 $6
fi

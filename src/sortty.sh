#!/bin/bash

version=1.0-beta

help_message () {
    echo
    echo "usage: sortty [ array_size ] [ array_range] [ fill ] [ wait_time (milliseconds) ] [ algorithm ]"
    echo "usage: sortty [ integer ] [ integer ] [ boolean integer (0 or 1) ] [ integer ] [ string ]"
    echo
    echo "Availible algorithms: bogosort, bubblesort"
    echo
    echo "example: sortty 15 10 0 100 bubblesort"
    echo
    echo "[ array_size ] is 15, [ array_range ] is 10, [ fill ] is 0 (AKA False), [ wait_time ] waits 0.01 seconds before drawing, [ algorithm ] uses the bubblesort algorithm"
    echo
}

# If first argument is empty, show help message
if [ -z "$1" ]; then
  echo
  echo "Arguments are missing"
  help_message

# -h or --help arguments
elif [ $1 == "-h" ] || [ $1 == "--help" ]; then
  echo
  echo "Arguments are needed with sortty"
  help_message

# -v or --version arguments
elif [ $1 == "-v" ] || [ $1 == "--version" ]; then
  echo "$version"

# Checks if arguments are correct value type [ integer, integer, integer, integer, string ]
elif [[ $1 =~ ^[0-9]+$ ]] && [[ $2 =~ ^[0-9]+$ ]] && [[ $3 =~ ^[0-9]+$ ]] && [[ $4 =~ ^[0-9]+$ ]] && ([ $5 == "bogosort" ] || [ $5 == "bubblesort" ]); then
  python3 main.py $1 $2 $3 $4 $5

# Any other possible arguments display help message
else
  echo
  echo "Argument(s) not recognized"
  help_message

fi

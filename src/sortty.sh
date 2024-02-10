#!/bin/bash

version=v1.0-beta

help_message () {
  echo
  echo "usage: sortty [ -h --help ] (to show advanced options) [ -v --version ] (to show version)"
  echo
  echo "or"
  echo
  echo "usage: sortty [ array_size ] [ array_range] [ fill ] [ wait_time (milliseconds) ] [ algorithm ] (to use the script)"
  echo
  echo "example command: sortty 15 10 0 100 bubblesort"
  echo
}

help_advanced () {
  echo
  echo "usage: sortty [ -h --help ] (to show advanced options)"
  echo
  echo "or"
  echo
  echo "usage: sortty [ -v --version ] (to show version)"
  echo
  echo "or"
  echo
  echo "sortty [ array_size ] [ array_range] [ fill ] [ wait_time (milliseconds) ] [ algorithm ] (to use the script)"
  echo
  echo "Enter the value types as follows:"
  echo "sortty [ integer ] [ integer ] [ boolean integer (0 or 1) ] [ integer ] [ string ]"
  echo
  echo "Example command:"
  echo "sortty 15 10 0 100 bubblesort"
  echo
  echo "In the example command above,"
  echo
  echo "[ array_size ] is 15, meaning it will give the program 15 items to sort."
  echo
  echo "[ array_range ] is 10, meaning the array that the program sorts ranges from values 0 to 10."
  echo
  echo "[ fill ] is 0 (AKA False), meaning that the program will not ignore the values above and use the highest possible array size and array range, limited by the size of the screen."
  echo
  echo "[ algorithm ] uses the bubblesort algorithm, but available algorithms are: bogosort, bubblesort"
  echo
  echo "Note: If [ fill ] is 1 (AKA True), the program will ignore [ array_size ] and [ array_range ], as it makes the program use the screen dimensions for [ array_size ] and [ array_range ] instead."
  echo
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
  help_advanced

# -v or --version arguments
elif [ $1 == "-v" ] || [ $1 == "--version" ]; then
  echo "$version"

# Checks if arguments are correct value type [ integer, integer, integer, integer, string ]
elif [[ $1 =~ ^[0-9]+$ ]] && [[ $2 =~ ^[0-9]+$ ]] && [[ $3 =~ ^[0-9]+$ ]] && [[ $4 =~ ^[0-9]+$ ]] && ([ $5 == "bogosort" ] || [ $5 == "bubblesort" ]); then
  python3 /usr/local/bin/sortty-bin/main.py $1 $2 $3 $4 $5

# Any other possible arguments display help message
else
  echo
  echo "Argument(s) not recognized"
  help_message

fi

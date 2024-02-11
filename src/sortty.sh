#!/bin/bash

version=v1.2-stable

help_advanced () {
  # Displays sorTTY in big ascii letters using figlet
  figlet sorTTY
  echo
  echo "usage: sortty [ -h --help ] (to show advanced options)"
  echo
  echo "or"
  echo
  echo "usage: sortty [ -v --version ] (to show version)"
  echo
  echo "or"
  echo
  echo "sortty [ array_size (integer) ] [ array_range (integer) ] [ fill (boolean integer (0 or 1)) ] [ reversed (boolean integer) ] [ show_info (boolean integer) ] [ wait_time (milliseconds) (integer) ] [ algorithm (string) ]"
  echo
  echo "Example command:"
  echo "sortty 15 10 0 0 1 100 bubblesort"
  echo
  echo "In the example command above,"
  echo
  echo "[ array_size ] is 15, meaning it will give the program 15 items to sort."
  echo
  echo "[ array_range ] is 10, meaning the array that the program sorts ranges from values 1 to 10."
  echo
  echo "[ fill ] is 0 (AKA False), but if it is 1 (AKA True), the program will ignore the values above and use the highest possible"
  echo "array size and array range, limited by the size of the screen, basically meaning it fills the screen with the array"
  echo
  echo "[ reversed ] is 0 (AKA False), so the program will not sort from greatest to least, but least to greatest."
  echo
  echo "[ show_info ] is 1 (AKA True), so the program will show the sorting information after sorting"
  echo
  echo "[ algorithm ] uses the bubblesort algorithm, but available algorithms are: bogosort, bubblesort, mergesort, insertionsort, quicksort, gnomesort, heapsort, cocktailsort, selectionsort, shellsort"
  echo
  echo "Note: If [ fill ] is 1 (AKA True), the program will ignore [ array_size ] and [ array_range ],"
  echo "as it makes the program use the screen dimensions for [ array_size ] and [ array_range ] instead."
  echo
}

# If first argument is empty, show help message
if [ -z "$1" ]; then
  echo
  echo "Arguments are missing"
  help_advanced

# -h or --help arguments
elif [ $1 == "-h" ] || [ $1 == "--help" ]; then
  echo
  echo "Arguments are needed with sortty"
  help_advanced

# -v or --version arguments
elif [ $1 == "-v" ] || [ $1 == "--version" ]; then
  echo "$version"

# Checks if arguments are correct value type [ integer, integer, integer, integer, string ]
elif [[ $1 =~ ^[0-9]+$ ]] && [[ $2 =~ ^[0-9]+$ ]] && ([ $3 == 0 ] || [ $3 == 1 ]) && ([ $4 == 0 ] || [ $4 == 1 ]) && ([ $5 == 0 ] || [ $5 == 1 ]) && [[ $6 =~ ^[0-9]+$ ]] && ([ $7 == "bogosort" ] || [ $7 == "bubblesort" ] || [ $7 == "mergesort" ] || [ $7 == "insertionsort" ] || [ $7 == "quicksort" ] || [ $7 == "gnomesort" ] || [ $7 == "heapsort" ] || [ $7 == "cocktailsort" ] || [ $7 == "selectionsort" ] || [ $7 == "shellsort" ]); then
  python3 /usr/local/bin/sortty-bin/main.py $1 $2 $3 $4 $5 $6 $7

# Any other possible arguments display help message
else
  echo
  echo "Argument(s) not recognized"
  help_advanced

fi

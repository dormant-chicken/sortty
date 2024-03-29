#!/bin/bash

version=v1.6-git

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
  echo "usage: sortty [ -hs --help-short ] (to show short version of help message)"
  echo
  echo "or"
  echo
  echo "sortty [ array_size (integer) ] [ array_range (integer) ] [ fill (boolean integer (0 or 1)) ] [ fancy (boolean integer) ] [ bar_size (integer) ] [ wait_time (milliseconds) (integer) ] [ algorithm (string) ]"
  echo
  echo "Example command:"
  echo "sortty 15 10 0 0 3 100 bubblesort"
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
  echo "[ fancy ] is 0 (AKA False), so the program will use a '#' instead of a fancy bar"
  echo
  echo "[ bar_size ] is 3, so the program will draw the bars with a width of 3 terminal cells"
  echo
  echo "[ algorithm ] uses the bubblesort algorithm, but available algorithms are: bogosort, bubblesort, mergesort, insertionsort, quicksort, gnomesort, heapsort, cocktailsort, selectionsort, shellsort, oddevensort, combsort, bingosort, radixsort"
  echo
  echo "Note: If [ fill ] is 1 (AKA True), the program will ignore [ array_size ] and [ array_range ],"
  echo "as it makes the program use the screen dimensions for [ array_size ] and [ array_range ] instead."
  echo
}

# If first argument is empty, show help message
if [ -z "$1" ]; then
  echo
  help_advanced
  echo "Error: arguments are missing"
  echo

# -h or --help arguments
elif [ $1 == "-h" ] || [ $1 == "--help" ]; then
  echo
  help_advanced
  echo "Error: arguments are needed with sortty"
  echo

# -hs or --help-short arguments
elif [ $1 == "-hs" ] || [ $1 == "--help-short" ]; then
  echo "sortty [array_size] [array_range] [fill] [fancy] [bar_size] [wait_time(ms)] [algorithm]"
  echo "sortty [integer] [integer] [boolean integer(0/1)] [boolean integer] [boolean integer] [integer] [string]"
  echo "Available algorithms: bogosort, bubblesort, mergesort, insertionsort, quicksort, gnomesort, heapsort, cocktailsort, selectionsort, shellsort, oddevensort, combsort, bingosort, radixsort"

# -v or --version arguments
elif [ $1 == "-v" ] || [ $1 == "--version" ]; then
  echo "$version"

# Checks if arguments are correct value type
elif [[ $1 =~ ^[0-9]+$ ]] && [[ $2 =~ ^[0-9]+$ ]] && ([ $3 == 0 ] || [ $3 == 1 ]) && ([ $4 == 0 ] || [ $4 == 1 ]) && [[ $5 =~ ^[0-9]+$ ]] && (( $5 <= 6 )) && (( $5 >= 1 )) && [[ $6 =~ ^[0-9]+$ ]] && ([ $7 == "bogosort" ] || [ $7 == "bubblesort" ] || [ $7 == "mergesort" ] || [ $7 == "insertionsort" ] || [ $7 == "quicksort" ] || [ $7 == "gnomesort" ] || [ $7 == "heapsort" ] || [ $7 == "cocktailsort" ] || [ $7 == "selectionsort" ] || [ $7 == "shellsort" ] || [ $7 == "oddevensort" ] || [ $7 == "combsort" ] || [ $7 == "bingosort" ] || [ $7 == "radixsort" ]); then
  # If not installed, and the user wants to just try it, run the python script directly without installing
  if [ -d /usr/local/bin/sortty-bin/ ]; then
    python3 /usr/local/bin/sortty-bin/main.py $1 $2 $3 $4 $5 $6 $7
  else
    python3 src/main.py $1 $2 $3 $4 $5 $6 $7
  fi

# Any other possible arguments display help message
else
  echo
  help_advanced
  echo "Error: invalid argument(s)"
  echo

fi

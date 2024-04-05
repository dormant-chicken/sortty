import os, sys

argc = len(sys.argv)

version = "v1.8-git"

fancy = "0"
bar_size = "2"
wait_time = "75"
algorithm = "quick"
array_size = "30"
array_range = "20"
fill = "1"

run = 1

def help_advanced():
    # Displays sorTTY in big ascii letters using figlet
    os.system("figlet sortty")
    
    print("""
Info usage:
sortty [ -h --help ] (to show advanced options) OR [ -v --version ] (to show version) OR [ -hs --help-short ] (to show short version of help message)
Usage:
sortty [--fancy or -f] [--bar_size or -b] [--wait_time or -w (ms)] [--algorithm or -a] [--size or -s] [--range or -r] [--fill or -fi]
sortty [0/1]           [integer]          [integer]                [string]           [integer]      [integer]        [0/1]

Example command:

sortty

Since only the name of the program is run, and there are no arguments, these are the defaults:
[--fancy of -f] is 0 (false), meaning the program will use a '#' character for the bars instead of a fancy bar
[--bar_size or -b] is 2, meaning the program will display the bars with a width of 2 terminal characters
[--wait_time or -w] is 75, meaning the program wlll wait 75ms before refreshing the screen
[--algorithm or -a] is quick, meaning the program will use the quicksort algorithm to sort the array
[--size or -s] of array is 30, meaning the array will have 30 elements
[--range or -r] of array is 20, meaning the maximum value of the array will be 20
[--fill or -fi] is 1, so the array fills the screen and ignores the array size and range

Available algorithms: bogo bubble merge insertion quick gnome heap cocktail selection shell oddeven comb bingo radix pigeonhole pancake

If you want custom options different from the default ones, do so like this:

sortty --algorithm insertion --fancy 1

The command above runs sortty with the insertion sort algorithm and sets fancy bars to 1 (true)

More options are available above in the usage part

Note: you can set the algorithm to 'forever' like this:

sortty --algorithm forever

Setting it to forever makes the program shuffles the array sorts the array with a random algorithm forever (excluding bogo sort)

    """)

def help_short():
    print("""
Info usage:
sortty [ -h --help ] (to show advanced options) OR [ -v --version ] (to show version) OR [ -hs --help-short ] (to show short version of help message)
Usage:
sortty [--fancy or -f] [--bar_size or -b] [--wait_time or -w (ms)] [--algorithm or -a] [--size or -s] [--range or -r] [--fill or -fi]
sortty [0 or 1]        [integer]          [integer]                [string]            [integer]      [integer]       [0 or 1] \n

Example command:

sortty

run 'sortty -h' or 'sortty --help' for more info

    """)

# starts at 1 so that it ignores the first argument (name of the program)
for i in range(1, argc):
    if (sys.argv[i] == "-f") or (sys.argv[i] == "--fancy"):
        if argc > (i + 1):
            if (sys.argv[i + 1] == "0") or (sys.argv[i + 1] == "1"):
                fancy = sys.argv[i + 1]
            else:
                run = -1
                print("fancy bar value not recognized")
            
                break
        else:
            run = -1
            print("fancy bar value not recognized")
            
            break

    if (sys.argv[i] == "-b") or (sys.argv[i] == "--bar_size"):
        if argc > (i + 1):
            if (sys.argv[i + 1].isnumeric()) and (int(sys.argv[i + 1]) > 0) and (int(sys.argv[i + 1]) <= 6):
                bar_size = sys.argv[i + 1]
            else:
                run = -1
                print("bar_size value not recognized")
            
                break
        else:
            run = -1
            print("bar_size value not recognized")
            
            break
    
    if (sys.argv[i] == "-w") or (sys.argv[i] == "--wait_time"):
        if argc > (i + 1):
            if (sys.argv[i + 1].isnumeric()) and (int(sys.argv[i + 1]) > 0):
                wait_time = sys.argv[i + 1]
            else:
                run = -1
                print("wait_time value not recognized")
            
                break
        else:
            run = -1
            print("wait_time value not recognized")
            
            break

    if (sys.argv[i] == "-a") or (sys.argv[i] == "--algorithm"):
        if argc > (i + 1):
            if ((str(sys.argv[i + 1]) == "bogo") or (str(sys.argv[i + 1]) == "bubble") or (str(sys.argv[i + 1]) == "merge") or (str(sys.argv[i + 1]) == "insertion") or (str(sys.argv[i + 1]) == "quick") or (str(sys.argv[i + 1]) == "gnome") or (str(sys.argv[i + 1]) == "heap") or (str(sys.argv[i + 1]) == "cocktail") or (str(sys.argv[i + 1]) == "selection") or (str(sys.argv[i + 1]) == "shell") or (str(sys.argv[i + 1]) == "oddeven") or (str(sys.argv[i + 1]) == "comb") or (str(sys.argv[i + 1]) == "bingo") or (str(sys.argv[i + 1]) == "radix") or (str(sys.argv[i + 1]) == "pigeonhole") or (str(sys.argv[i + 1]) == "pancake") or (str(sys.argv[i + 1]) == "forever")):
                algorithm = sys.argv[i + 1]
            else:
                run = -1
                print("specified algoritm not recognized")
            
                break
        else:
            run = -1
            print("specified algoritm not recognized")
            
            break
    
    if (sys.argv[i] == "-s") or (sys.argv[i] == "--size"):
        if argc > (i + 1):
            if (sys.argv[i + 1].isnumeric()) and (int(sys.argv[i + 1]) > 0):
                array_size = sys.argv[i + 1]
            else:
                run = -1
                print("array size value not recognized")
            
                break
        else:
            run = -1
            print("array size value not recognized")
            
            break

    if (sys.argv[i] == "-r") or (sys.argv[i] == "--range"):
        if argc > (i + 1):
            if (sys.argv[i + 1].isnumeric()) and (int(sys.argv[i + 1]) > 0):
                array_range = sys.argv[i + 1]
            else:
                run = -1
                print("array range value not recognized")
            
                break
        else:
            run = -1
            print("array range value not recognized")
            
            break

    if (sys.argv[i] == "-fi") or (sys.argv[i] == "--fill"):
        if argc > (i + 1):
            if (sys.argv[i + 1] == "0") or (sys.argv[i + 1] == "1"):
                fill = sys.argv[i + 1]
            else:
                run = -1
                print("fill value not recognized")
            
                break
        else:
            run = -1
            print("fill value not recognized")
            
            break
    
    elif (sys.argv[i] == "-h") or (sys.argv[i] == "--help"):
        run = 0

        help_advanced()

        break

    elif (sys.argv[i] == "-hs") or (sys.argv[i] == "--help_short"):
        run = 0

        help_short()

        break
    
    elif (sys.argv[i] == "-v") or (sys.argv[i] == "--version"):
        run = 0

        print("version: " + version)

        break

# runs installed program if present
if os.path.isdir("/usr/local/bin/sortty-bin/"):
    path = "/usr/local/bin/sortty-bin/main.py"
else:
    path = "src/main.py"

if run == 1:
    os.system("python3 " + path + " " + fancy + " " + bar_size + " " + wait_time + " " + algorithm + " " + array_size + " " + array_range + " " + fill)

# if run is 0, do nothing

elif run == -1:
    print("run 'sortty -h' or 'sortty --help' for help")
    print("Error: invalid argument(s)")

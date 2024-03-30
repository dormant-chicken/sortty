import os, sys

version = "v1.7-git"

argc = len(sys.argv)

def help_advanced():
    # Displays sorTTY in big ascii letters using figlet
    os.system("figlet sortty")
    print("Info:")
    print("sortty [ -h --help ] (to show advanced options) OR [ -v --version ] (to show version) OR [ -hs --help-short ] (to show short version of help message)")
    print("Usage:")
    print("sortty [fancy] [bar_size] [wait_time(ms)] [algorithm] [array_size(optional)] [array_range(optional)]")
    print("")
    print("Example command:")
    print("sortty 0 3 100 bubblesort")
    print("")
    print("In the example command above,")
    print("")
    print("[fancy] is 0 (AKA False), so the program will use a '#' character and a '@' character for highlight instead of a fancy bar with colors for highlight")
    print("")
    print("[bar_size] is 3, so the program will draw the bars with a width of 3 terminal cells")
    print("")
    print("[wait_time] is 100, meaning the program will wait 100ms before drawing again")
    print("")
    print("[algorithm] uses the bubblesort algorithm, but available algorithms are: bogosort bubblesort mergesort insertionsort quicksort gnomesort heapsort cocktailsort selectionsort shellsort oddevensort combsort bingosort radixsort")
    print("")
    print("If you want a custom array size and array range, you can do so like this:")
    print("sortty 0 3 100 bubblesort 30 20")
    print("")
    print("After you specify the algorithm, put down the array size you want then the array range you want")
    print("")
    print("[array_size] is 30, meaning it will give the program 30 items to sort")
    print("")
    print("[array_range] is 20, meaning the array that the program sorts ranges from values 1 to 20")
    print("")
    print("Note: if you do not want a custom array size and range, do not put down the array size and array range values, and the program will automatically fill your entire screen with the array instead")
    print("")

if argc == 1:
    print("run 'sortty -h' or 'sortty --help' for help")
    print("Error: arguments are missing")

elif (argc != 5) and (argc != 7):
    match str(sys.argv[1]):
        case "-h" | "--help":
            help_advanced()

        case "-hs" | "--help_short":
            print("usage:")
            print("sortty [fill]                 [fancy]           [bar_size]        [wait_time(ms)]   [algorithm]       [array_size] (optional) [array_range] (optional)")
            print("sortty [boolean integer(0/1)] [boolean integer] [boolean integer] [integer]         [string]          [integer]               [integer]")
            print("")
            print("Available algorithms: bogosort bubblesort mergesort insertionsort quicksort gnomesort heapsort cocktailsort selectionsort shellsort oddevensort combsort bingosort radixsort")
            print("")
            print("Example command:")
            print("sortty 0 3 100 bubblesort")
            print("")
            print("run sortty --help for more info")
        
        case "-v" | "--version":
            print("version: " + version)

        # Any other possible arguments display help message
        case default:
            print("run 'sortty -h' or 'sortty --help' for help")
            print("Error: invalid argument(s)")

elif ((int(sys.argv[1]) == 0) or (int(sys.argv[1]) == 1)) and sys.argv[2].isnumeric() and (int(sys.argv[2]) >= 1) and (int(sys.argv[2]) <= 6) and sys.argv[3].isnumeric() and ((str(sys.argv[4]) == "bogo") or (str(sys.argv[4]) == "bubble") or (str(sys.argv[4]) == "merge") or (str(sys.argv[4]) == "insertion") or (str(sys.argv[4]) == "quick") or (str(sys.argv[4]) == "gnome") or (str(sys.argv[4]) == "heap") or (str(sys.argv[4]) == "cocktail") or (str(sys.argv[4]) == "selection") or (str(sys.argv[4]) == "shell") or (str(sys.argv[4]) == "oddeven") or (str(sys.argv[4]) == "comb") or (str(sys.argv[4]) == "bingo") or (str(sys.argv[4]) == "radix")):
    if argc == 5:
        # passes -1 to let the python program know that it has to fill the screen
        if os.path.isdir("/usr/local/bin/sortty-bin/"):
            os.system("python3 /usr/local/bin/sortty-bin/main.py " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " -1")
        else:
            os.system("python3 src/main.py " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " -1")
    
    # user has passed custom array size and range
    elif (argc == 7) and sys.argv[5].isnumeric() and sys.argv[6].isnumeric():
        if os.path.isdir("/usr/local/bin/sortty-bin/"):
            os.system("python3 /usr/local/bin/sortty-bin/main.py " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6])
        else:
            os.system("python3 src/main.py " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6])


else:
    print("run 'sortty -h' or 'sortty --help' for help")
    print("Error: invalid argument(s)")

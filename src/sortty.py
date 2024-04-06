import argparse
import art #this is for the fancy ascii art, instead of an external program
import sys
import os

version = "v1.8-git"
algorithms = ( #edit this list to add algorithms
    'forever',
    'bogo',
    'bubble',
    'merge',
    'insertion',
    'quick',
    'gnome',
    'heap',
    'cocktail',
    'selection',
    'shell', 
    'oddeven',
    'comb',
    'bingo',
    'radix',
    'pigeonhole',
    'pancake')

class ArgumentParser(argparse.ArgumentParser): #edit print message function to make it show ascii art
    def print_help(self):
        print(art.text2art('sortty'))
        return super(ArgumentParser, self).print_help()

def main():
    parser = ArgumentParser(
        epilog='''Note: you can set the algorithm to 'forever' like this:
sortty --algorithm forever
Setting it to forever makes the program shuffles the array sorts the array with a random algorithm forever (excluding bogo sort)'''
    )

    #every command-line argument with help message and default values
    parser.add_argument(
        '-f', '--fancy',
        help='add this to make the program use a \'#\' character for the bars instead of a fancy bar',
        action='store_true',
    )
    parser.add_argument(
        '-b', '--bar_size',
        help='default is 2, meaning the program will display the bars with a width of 2 terminal characters',
        default=2,
        type=int,
    )
    parser.add_argument(
        '-w', '--wait_time',
        help='default is 75, meaning the program wlll wait 75ms before refreshing the screen',
        default=75,
        type=int,
    )
    parser.add_argument(
        '-a', '--algorithm',
        help='default is quick, meaning the program will use the quicksort algorithm to sort the array',
        default='quick',
        choices=algorithms
    )
    parser.add_argument(
        '-s', '--size',
        dest='array_size',
        help='default is 30, meaning the array will have 30 elements',
        default=30,
        type=int,
    )
    parser.add_argument(
        '-r', '--range',
        dest='array_range',
        help='default is 20, meaning the maximum value of the array will be 20',
        default=20,
        type=int,
    )
    parser.add_argument(
        '-nf', '--no-fill',
        dest='no_fill',
        help='use this if you want to specify custom sizes',
        action='store_true'
    )
    parser.add_argument(
        '-v', '--version',
        help='print version and quit',
        action='version',
        version=version
    )
    args = parser.parse_args()
    print(args)

    # runs installed program if present
    if os.path.isdir("/usr/local/bin/sortty-bin/"):
        path = "/usr/local/bin/sortty-bin/main.py"
    else:
        #i used absolute path so you can run the script from any dir
        path = os.path.join(os.path.dirname(__file__), 'main.py') 
    #finally, call the script (should change this to a function instead later)
    os.system("python3 " + path + " " + str(int(args.fancy)) + " " + str(args.bar_size) + " " + str(args.wait_time) + " " + args.algorithm + " " + str(args.array_size) + " " + str(args.array_range) + " " + str(int(not args.no_fill)))

if __name__ == '__main__':
    main()

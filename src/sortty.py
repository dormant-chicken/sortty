#!/usr/bin/env python3
version = "v1.8-git"

# edit this list to add algorithms
algorithms = (
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
    'pancake'
    )

# 'art' this is for the fancy ascii art, instead of an external program
import argparse
import curses
import random
import time
import math
import art
import sys
import os

# used for filling array with green
def draw_array(stdscr, startx, array, index, mode):
    stdscr.clear()
    # This draws the array onto the screen
    bar_size = options['bar_size']
    for i in range(len(array)):
        for j in range(array[i]):
            # Checks if [ fancy ] is True
            if options['fancy']:
                if mode == "fill":
                    if i <= index:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size, curses.color_pair(1))
                    else:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size, curses.A_REVERSE)

                elif mode == "start":
                    if i <= index:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size, curses.A_REVERSE)
                    else:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size)

                elif mode == "mark_element":
                    if i == index:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size, curses.color_pair(2))
                    else:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size, curses.A_REVERSE)

                elif (mode == "none") or (mode == "shuffle"):
                    stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size, curses.A_REVERSE)

            else:
                if mode == "fill":
                    if i <= index:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), "@" * bar_size)
                    else:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), "#" * bar_size)

                elif mode == "start":
                    if i <= index:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), "#" * bar_size)
                    else:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), " " * bar_size)
                        
                elif mode == "mark_element":
                    if i == index:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), "@" * bar_size)
                    else:
                        stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), "#" * bar_size)

                elif (mode == "none") or (mode == "shuffle"):
                    stdscr.addstr(term_height - 1 - j, startx + (i * bar_size), "#" * bar_size)


    # moves cursor to bottom right of screen (less distracting)
    stdscr.move(term_height - 1, term_width - 1)
    
    # refresh screen and wait specified time
    stdscr.refresh()

    if mode == "fill":
        time.sleep(((750 / len(array)) * bar_size) / 1000)

    elif mode == "shuffle":
        time.sleep(((1250 / len(array)) * bar_size) / 1000)

    elif mode == "start":
        time.sleep(((500 / len(array)) * bar_size) / 1000)

    else:
        time.sleep(options['wait_time'] / 1000)

# Bogosort
def bogo_sort(stdscr, startx, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if(array[i] > array[i + 1]):
                sorted = False
                break
        if not sorted:
            random.shuffle(array)
            draw_array(stdscr, startx, array, 0, "none")

# Bubblesort
def bubble_sort(stdscr, startx, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
            draw_array(stdscr, startx, array, i + 1, "mark_element")

# Mergesort
def merge_sort(stdscr, startx, arr, is_main):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(stdscr, startx, left_arr, False)
        merge_sort(stdscr, startx, right_arr, False)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                if is_main == True:
                    draw_array(stdscr, startx, arr, 0, "none")
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Insertion sort
def insertion_sort(stdscr, startx, array):
    for i in range(1, len(array)):
        j = i
        draw_array(stdscr, startx, array, j, "mark_element")

        while array[j] < array[j - 1] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            draw_array(stdscr, startx, array, j, "mark_element")

# Quicksort
def quick_sort(stdscr, startx, array, left, right):
    if left < right:
        partition_pos = partition(stdscr, startx, array, left, right)
        quick_sort(stdscr, startx, array, left, partition_pos - 1)
        quick_sort(stdscr, startx, array, partition_pos + 1, right)

# Used by quicksort function
def partition(stdscr, startx, array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
            draw_array(stdscr, startx, array, i, "mark_element")

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i

# Gnomesort
def gnome_sort(stdscr, startx, array):
    i = 0
    while i < len(array): 
        if i == 0: 
            i += 1
            
        if array[i] >= array[i - 1]: 
            i += 1
            draw_array(stdscr, startx, array, i, "mark_element")

        else: 
            array[i], array[i - 1] = array[i - 1], array[i] 
            i -= 1
            draw_array(stdscr, startx, array, i, "mark_element")

# Heapsort
def heap_sort(stdscr, startx, array):
    N = len(array)

    for i in range(N//2 - 1, -1, -1):
        heapify(stdscr, startx, array, N, i)

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]

        heapify(stdscr, startx, array, i, 0)

# Needed for heapsort
def heapify(stdscr, startx, array, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and array[largest] < array[l]:
        largest = l

    if r < N and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        draw_array(stdscr, startx, array, l, "mark_element")

        heapify(stdscr, startx, array, N, largest)

# Cocktailsort
def cocktail_sort(stdscr, startx, array):
    swapped = True
    start = 0
    end = len(array) - 1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                draw_array(stdscr, startx, array, i + 1, "mark_element")

        if (swapped == False):
            break

        swapped = False

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                draw_array(stdscr, startx, array, i, "mark_element")

        start += 1

# Selectionsort
def selection_sort(stdscr, startx, array):
    for i in range(len(array)):
        min_idx = i

        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        draw_array(stdscr, startx, array, min_idx, "mark_element")

# Shellsort
def shell_sort(stdscr, startx, array):
    gap = int(len(array) / 2)

    while gap > 0:
        j = gap

        # Sorts the array
        while j < len(array):
            i = j - gap
            
            while i >= 0:
                # Swap if value on right is lesser
                if array[i + gap] < array[i]:
                    array[i + gap], array[i] = array[i], array[i + gap]
                    draw_array(stdscr, startx, array, j, "mark_element")
                
                # Move gap to sort
                i = i - gap

            j += 1

        # Cuts gap size in half
        gap = int(gap / 2)

# Oddevensort
def oddeven_sort(stdscr, startx, array):
    sorted = False

    while sorted == False:
        sorted = True

        for i in range(1, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                draw_array(stdscr, startx, array, i, "mark_element")
                
        for i in range(0, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                draw_array(stdscr, startx, array, i, "mark_element")

# Combsort
def comb_sort(stdscr, startx, array):
    n = len(array)

    gap = n

    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)

        swapped = False

        for i in range(0, n-gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap]=array[i + gap], array[i]
                swapped = True
                draw_array(stdscr, startx, array, i, "mark_element")

# Needed for combsort
def get_next_gap(gap):

    gap = int(gap / 1.3)
    if gap < 1:
        return 1
    return gap

def bingo_sort(stdscr, startx, array):
    # smallest element From array
    bingo = min(array)
    
    # largest element from 
    largest = max(array)
    next_bingo = largest
    nextPos = 0
    
    while bingo < next_bingo:
        # keep track of element to put in correct position
        startPos = nextPos
        for i in range(startPos, len(array)):
            if array[i] == bingo:
                array[i], array[nextPos] = array[nextPos], array[i]
                nextPos += 1
                draw_array(stdscr, startx, array, nextPos, "mark_element")
                
            # finds next bingo elemnt
            elif array[i] < next_bingo:
                next_bingo = array[i]
        bingo = next_bingo
        next_bingo = largest

# Radixsort
def radix_sort(stdscr, startx, array):
    max_array = max(array)

    exp = 1
    while max_array / exp >= 1:
        counting_sort(stdscr, startx, array, exp)
        exp *= 10

# Needed for radixsort
def counting_sort(stdscr, startx, array, exp):
    n = len(array)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = int(array[i] / exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    # builds output array
    i = n - 1
    while i >= 0:
        index = int(array[i] / exp)
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    # copy the output array to array
    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]
        draw_array(stdscr, startx, array, i, "mark_element")

# Pigeonholesort
def pigeonhole_sort(stdscr, startx, array):
    array_min = min(array)
    array_max = max(array)
    array_range = array_max - array_min + 1

    # fill pigeonhole array
    holes = [0] * array_range

    # populate pigeonholes
    for i in array:
        holes[i - array_min] += 1

    # put back elements
    i = 0
    for count in range(array_range):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + array_min
            i += 1
            draw_array(stdscr, startx, array, i, "mark_element")

# Pancake sort
def pancake_sort(stdscr, startx, array, n):
    current = n

    while current > 1:

        # finds max element in array
        max = 0

        for i in range(0, current):
            if array[i] > array[max]:
                max = i
        
        if max != (current - 1):

            # flips once to bring max to first element of array
            flip(stdscr, startx, array, max)

            # flips again to bring max element next to current
            flip(stdscr, startx, array, current - 1)

        current -= 1

# needed for pancakesort
def flip(stdscr, startx, array, i):

    # swaps elements until specified part of array is flipped
    start = 0
    
    while start < i:
        array[start], array[i] = array[i], array[start]
        start += 1
        i -= 1
        draw_array(stdscr, startx, array, i, "mark_element")

# Function gives error if terminal is too small
def give_term_error(stdscr, term_required, term_current, message, needed):
    stdscr.addstr(0, 0, str(message))
    stdscr.addstr(2, 0, "required " + needed + ": " + str(term_required) + " cells")
    stdscr.addstr(3, 0, "terminal " + needed + ": " + str(term_current) + " cells")
    stdscr.addstr(5, 0, "please resize your terminal and try again")
    stdscr.addstr(7, 0, "press any key to exit")
    stdscr.getch()
    curses.endwin()

def run_sortty(stdscr):
    # Finds terminal info
    global options
    global term_height
    global term_width
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    # checks fancy bar argument
    if options['fancy']:
        fancy = True
    else:
        fancy = False

    # checks if user wants to sort forever
    if options['algorithm'] == 'forever':
        forever = True
    else:
        forever = False

    # If not filled, makes the array size and range the highest possible that can fit on the screen
    if options['size'] is None:
        fill_screen = True
        array_size = int(term_width / options['bar_size']) - 2
        array_range = term_height - 2
    else:
        fill_screen = False
        err = False
        array_size, array_range = options['size'].split('x')
        try:
            array_size = int(array_size)
            array_range = int(array_range)
        except ValueError:
            err = True
        if err:
            raise ValueError('Invalid size format: use HEIGTHxWIDTH')

    # array declaration
    array = []

    # finds slope using array range and array size (slope = rise / run)
    slope = array_range / array_size
    bar_height = 0
    
    for i in range(array_size):
        bar_height += slope
        array.append(math.ceil(bar_height))

    # Finds correct position to start drawing
    startx = math.floor(term_width / 2) - math.floor(array_size * options['bar_size'] / 2)

    # Curses initialization
    curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.timeout(-1)
    stdscr.clear()

    # color pairs for ncurses
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)

    # Quits program if terminal height too small for array_range
    if term_height < 18:
        give_term_error(stdscr, 18, "terminal height less than minimum!", "height")

    elif term_width < 90:
        give_term_error(stdscr, 90, term_width, "terminal width less than minimum!", "width")

    elif fill_screen == False and (array_range > term_height):
        give_term_error(stdscr, array_range, "terminal height too small for array range!", "height")

    elif fill_screen == False and (array_size > term_width):
        give_term_error(stdscr, array_size, term_width, "terminal width too small for array size!", "width")
    
    # Otherwise, start main script
    else:
        # Draw the array before sorting
        for i in range(array_size):
            draw_array(stdscr, startx, array, i, "start")
        
        while True:
            # creates new algorithm
            if forever:
                algorithm = algorithms[random.randint(1, len(algorithms) - 1)]
            else:
                algorithm = options['algorithm']

            # waits before shuffle
            time.sleep(750 / 1000)

            # shuffle array
            for i in range(array_size):
                temp = random.randint(0, array_size - 1)
                array[i], array[temp] = array[temp], array[i]
                draw_array(stdscr, startx, array, 0, "shuffle")

            # waits before sorting
            time.sleep(1000 / 1000)

            if forever == False:
                # Starts performance timer
                start_time = time.perf_counter()

            # Sorting algorithms determined by bash script
            match algorithm:
                case "bogo":
                    bogo_sort(stdscr, startx, array)

                case "bubble":
                    bubble_sort(stdscr, startx, array)

                case "merge":
                    merge_sort(stdscr, startx, array, True)

                case "insertion":
                    insertion_sort(stdscr, startx, array)

                case "quick":
                    quick_sort(stdscr, startx, array, 0, len(array) - 1)

                case "gnome":
                    gnome_sort(stdscr, startx, array)
                    
                case "heap":
                    heap_sort(stdscr, startx, array)

                case "cocktail":
                    cocktail_sort(stdscr, startx, array)

                case "selection":
                    selection_sort(stdscr, startx, array)

                case "shell":
                    shell_sort(stdscr, startx, array)

                case "oddeven":
                    oddeven_sort(stdscr, startx, array)
                
                case "comb":
                    comb_sort(stdscr, startx, array)

                case "bingo":
                    bingo_sort(stdscr, startx, array)

                case "radix":
                    radix_sort(stdscr, startx, array)
                
                case "pigeonhole":
                    pigeonhole_sort(stdscr, startx, array)
                
                case "pancake":
                    pancake_sort(stdscr, startx, array, len(array))
            
            if forever == False:
                # Ends performance timer
                end_time = time.perf_counter()
            
            # draws array final time
            draw_array(stdscr, startx, array, 0, "none")
            
            # if forever is false, stop running loop
            if forever == False:
                break
        
        # fills array with green after sorting
        for i in range(array_size):
            draw_array(stdscr, startx, array, i, "fill")

        # Finds where to place sort_info text
        text_x = 0

        # Shows that array is sorted and other info
        stdscr.addstr(0, text_x, "Array sorted!")
        stdscr.addstr(2, text_x, "Sorting information:")
        stdscr.addstr(4, text_x, f"sorting algorithm: {options['algorithm']} sort")
        stdscr.addstr(5, text_x, f"array size: {array_size}")
        stdscr.addstr(6, text_x, f"array range: {array_range}")
        stdscr.addstr(7, text_x, f"sorting time: {round(end_time - start_time, 3)} second(s)")
        stdscr.addstr(8, text_x, f"delay: {options['wait_time']} millisecond(s)")
        stdscr.addstr(9, text_x, f"bar size: {options['bar_size']}")
        stdscr.addstr(10, text_x, f"fill screen: {str(fill_screen).lower()}")
        stdscr.addstr(11, text_x, f"fancy bars: {str(fancy).lower()}")

        stdscr.addstr(13, text_x, "Press any key to exit")

        # moves cursor to bottom right of screen (less distracting)
        stdscr.move(term_height - 1, term_width - 1)
        
        # waits for key press and stops program
        stdscr.getch()

        # sometimes using endwin() makes ncurses give error after program ends
#        curses.endwin()


def sortty(**options):
    try:
        globals()['options'] = options
        curses.wrapper(run_sortty)
    except KeyboardInterrupt: #this way you can use ctrl+c to quit without showing an error
        sys.exit(0)

# edit print message function to make it show ascii art
class ArgumentParser(argparse.ArgumentParser):
    def print_help(self):
        print(art.text2art('sortty'))
        return super(ArgumentParser, self).print_help()

def main():
    parser = ArgumentParser(
        epilog='''Note: you can set the algorithm to 'forever' like this:
sortty --algorithm forever
Setting it to forever makes the program shuffles the array sorts the array with a random algorithm forever (excluding bogo sort)'''
    )

    # every command-line argument with help message and default values
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
        choices=algorithms + ('forever',)
    )
    parser.add_argument(
        '-s', '--size',
        help='HEIGTHxWIDTH, if not specified, adapt to terminal size.',
        default=None,
        type=str,
    )
    parser.add_argument(
        '-v', '--version',
        help='print version and quit',
        action='version',
        version=version
    )
    args = parser.parse_args()

    # finally, call the function to run sortty
    sortty(
        fancy=args.fancy,
        bar_size=args.bar_size,
        wait_time=args.wait_time,
        algorithm=args.algorithm,
        size=args.size,
    )

if __name__ == '__main__':
    main()

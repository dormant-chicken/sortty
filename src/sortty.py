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

def drawArray(stdscr, array, index, mode):
    resize = stdscr.getch()

    if resize == curses.KEY_RESIZE:
        stdscr.clear()
        curses.endwin()
        sortty(**options)
        sys.exit(0)

    stdscr.clear()

    barSize = options['barSize']

    # draws the array onto the screen
    for i in range(len(array)):
        for j in range(array[i]):
            # checks if text-only mode is enabled
            if options['textOnly']:
                # defaults
                char = "#"
                effect = None

                # special cases
                # fills with @ character
                if mode == "fill":
                    if i <= index:
                        char = "@"

                # fills with characters when starting

                elif mode == "start":
                    if i > index:
                        char = " "
                
                # shows index
                elif mode == "index" and options['noIndex'] == False:
                    if i == index:
                        char = "@"

            else:
                char = " "
                effect = curses.A_REVERSE

                if mode == "fill":
                    if i <= index:
                        effect = curses.color_pair(1)

                elif mode == "start":
                    if i > index:
                        effect = None
                
                elif mode == "index" and options['noIndex'] == False:
                    if i == index:
                        effect = curses.color_pair(2)
            
            # actual drawing
            if effect == None:
                stdscr.addstr(termHeight - 1 - j, startX + (i * barSize), char * barSize)
            else:
                stdscr.addstr(termHeight - 1 - j, startX + (i * barSize), char * barSize, effect)

    # moves cursor to bottom right of screen (less distracting)
    stdscr.move(termHeight - 1, termWidth - 1)
    
    # refresh screen and wait specified time
    stdscr.refresh()

    if mode == "fill":
        time.sleep(((500 / len(array)) * barSize) / 1000)

    elif mode == "shuffle":
        time.sleep(((600 / len(array)) * barSize) / 1000)

    elif mode == "start":
        time.sleep(((300 / len(array)) * barSize) / 1000)

    else:
        time.sleep(options['waitTime'] / 1000)

# Bogosort
def bogoSort(stdscr, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if(array[i] > array[i + 1]):
                sorted = False
                break
        if not sorted:
            random.shuffle(array)
            drawArray(stdscr, array, 0, "none")

# Bubblesort
def bubbleSort(stdscr, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
            drawArray(stdscr, array, i + 1, "index")

# Mergesort
def mergeSort(stdscr, arr, isMain):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        # recursion
        mergeSort(stdscr, leftArr, False)
        mergeSort(stdscr, rightArr, False)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
                if isMain == True:
                    drawArray(stdscr, arr, 0, "none")
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

# Insertion sort
def insertionSort(stdscr, array):
    for i in range(1, len(array)):
        j = i
        drawArray(stdscr, array, j, "index")

        while array[j] < array[j - 1] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            drawArray(stdscr, array, j, "index")

# Quicksort
def quickSort(stdscr, array, left, right):
    if left < right:
        partitionPos = partition(stdscr, array, left, right)
        quickSort(stdscr, array, left, partitionPos - 1)
        quickSort(stdscr, array, partitionPos + 1, right)

# Used by quicksort function
def partition(stdscr, array, left, right):
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
            drawArray(stdscr, array, i, "index")

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i

# Gnomesort
def gnomeSort(stdscr, array):
    i = 0
    while i < len(array): 
        if i == 0: 
            i += 1
            
        if array[i] >= array[i - 1]: 
            i += 1
            drawArray(stdscr, array, i, "index")

        else: 
            array[i], array[i - 1] = array[i - 1], array[i] 
            i -= 1
            drawArray(stdscr, array, i, "index")

# Heapsort
def heapSort(stdscr, array):
    N = len(array)

    for i in range(N//2 - 1, -1, -1):
        heapify(stdscr, array, N, i)

    for i in range(N - 1, 0, -1):
        array[i], array[0] = array[0], array[i]

        heapify(stdscr, array, i, 0)

# Needed for heapsort
def heapify(stdscr, array, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and array[largest] < array[l]:
        largest = l

    if r < N and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        drawArray(stdscr, array, l, "index")

        heapify(stdscr, array, N, largest)

# Cocktailsort
def cocktailSort(stdscr, array):
    swapped = True
    start = 0
    end = len(array) - 1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                drawArray(stdscr, array, i + 1, "index")

        if (swapped == False):
            break

        swapped = False

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                drawArray(stdscr, array, i, "index")

        start += 1

# Selectionsort
def selectionSort(stdscr, array):
    for i in range(len(array)):
        min_idx = i

        # finds smallest index
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        
        # swap
        array[i], array[min_idx] = array[min_idx], array[i]
        drawArray(stdscr, array, min_idx, "index")

# Shellsort
def shellSort(stdscr, array):
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
                    drawArray(stdscr, array, j, "index")
                
                # Move gap to sort
                i = i - gap

            j += 1

        # Cuts gap size in half
        gap = int(gap / 2)

# Oddevensort
def oddevenSort(stdscr, array):
    sorted = False

    while sorted == False:
        sorted = True

        for i in range(1, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                drawArray(stdscr, array, i, "index")
                
        for i in range(0, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                drawArray(stdscr, array, i, "index")

# Combsort
def combSort(stdscr, array):
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
                drawArray(stdscr, array, i, "index")

# Needed for combsort
def get_next_gap(gap):

    gap = int(gap / 1.3)
    if gap < 1:
        return 1
    return gap

def bingoSort(stdscr, array):
    # smallest element From array
    bingo = min(array)
    
    # largest element from 
    largest = max(array)
    nextBingo = largest
    nextPos = 0
    
    while bingo < nextBingo:
        # keep track of element to put in correct position
        startPos = nextPos
        for i in range(startPos, len(array)):
            if array[i] == bingo:
                array[i], array[nextPos] = array[nextPos], array[i]
                nextPos += 1
                drawArray(stdscr, array, nextPos, "index")
                
            # finds next bingo elemnt
            elif array[i] < nextBingo:
                nextBingo = array[i]
        bingo = nextBingo
        nextBingo = largest

# Radixsort
def radixSort(stdscr, array):
    maxArray = max(array)

    exp = 1
    while maxArray / exp >= 1:
        counting_sort(stdscr, array, exp)
        exp *= 10

# Needed for radixsort
def counting_sort(stdscr, array, exp):
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
        drawArray(stdscr, array, i, "index")

# Pigeonholesort
def pigeonholeSort(stdscr, array):
    arrayMin = min(array)
    arrayMax = max(array)
    arrayRange = arrayMax - arrayMin + 1

    # fill pigeonhole array
    holes = [0] * arrayRange

    # populate pigeonholes
    for i in array:
        holes[i - arrayMin] += 1

    # put back elements
    i = 0
    for count in range(arrayRange):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + arrayMin
            i += 1
            drawArray(stdscr, array, i, "index")

# Pancake sort
def pancakeSort(stdscr, array, n):
    current = n

    while current > 1:
        # finds max element in array
        max = 0

        for i in range(current):
            if array[i] > array[max]:
                max = i
        
        if max != (current - 1):

            # flips once to bring max to first element of array
            flip(stdscr, array, max)

            # flips again to bring max element next to current
            flip(stdscr, array, current - 1)

        current -= 1

# needed for pancakesort
def flip(stdscr, array, i):

    # swaps elements until specified part of array is flipped
    start = 0
    
    while start < i:
        array[start], array[i] = array[i], array[start]
        start += 1
        i -= 1
        drawArray(stdscr, array, i, "index")

# function gives error if terminal is too small
def giveTermError(stdscr, termRequired, termCurrent, message, needed):
    stdscr.addstr(0, 0, str(message))
    stdscr.addstr(2, 0, "required " + needed + ": " + str(termRequired) + " cells")
    stdscr.addstr(3, 0, "terminal " + needed + ": " + str(termCurrent) + " cells")
    stdscr.addstr(5, 0, "please resize your terminal and try again")
    stdscr.addstr(7, 0, "press any key to exit")
    stdscr.getch()
    curses.endwin()

def run_sortty(stdscr):
    # finds terminal info
    global options
    global termHeight
    global termWidth
    global startX
    termSize = os.get_terminal_size()
    termHeight = termSize.lines
    termWidth = termSize.columns

    # checks if user wants to sort forever
    if options['algorithm'] == 'forever':
        forever = True
    else:
        forever = False

    # if not filled, makes the array size and range the highest possible that can fit on the screen
    if options['size'] is None:
        fillScreen = True
        arraySize = int(termWidth / options['barSize']) - 2
        arrayRange = termHeight - 2
    else:
        fillScreen = False
        err = False
        arraySize, arrayRange = options['size'].split('x')
        try:
            arraySize = int(arraySize)
            arrayRange = int(arrayRange)
        except ValueError:
            err = True
        if err:
            raise ValueError('Invalid size format: use HEIGTHxWIDTH')

    # array declaration
    array = []

    # finds slope using array range and array size (slope = rise / run)
    slope = arrayRange / arraySize
    barHeight = 0
    
    for i in range(arraySize):
        barHeight += slope
        array.append(math.ceil(barHeight))

    # finds correct position to start drawing
    startX = math.floor(termWidth / 2) - math.floor((arraySize * options['barSize']) / 2)

    # curses initialization
    curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.timeout(1)
    stdscr.clear()

    # color pairs for ncurses
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)

    # quits program if terminal height too small
    if fillScreen == False and (arrayRange > termHeight):
        giveTermError(stdscr, arrayRange, termHeight, "terminal height too small for array range!", "height")

    elif fillScreen == False and (arraySize > termWidth):
        giveTermError(stdscr, arraySize, termWidth, "terminal width too small for array size!", "width")
    
    # otherwise, start main script
    else:
        # draw the array before sorting
        for i in range(arraySize):
            drawArray(stdscr, array, i, "start")
        
        while True:
            # creates new algorithm
            if forever:
                algorithm = algorithms[random.randint(1, len(algorithms) - 1)]
            else:
                algorithm = options['algorithm']

            # waits before shuffle
            time.sleep(750 / 1000)

            # shuffle array by swapping index with random element
            for i in range(arraySize):
                temp = random.randint(0, arraySize - 1)
                array[i], array[temp] = array[temp], array[i]
                drawArray(stdscr, array, 0, "shuffle")

            # waits before sorting
            time.sleep(1000 / 1000)

            if forever == False:
                # Starts performance timer
                startTime = time.perf_counter()

            # Sorting algorithms determined by bash script
            match algorithm:
                case "bogo":
                    bogoSort(stdscr, array)

                case "bubble":
                    bubbleSort(stdscr, array)

                case "merge":
                    mergeSort(stdscr, array, True)

                case "insertion":
                    insertionSort(stdscr, array)

                case "quick":
                    quickSort(stdscr, array, 0, len(array) - 1)

                case "gnome":
                    gnomeSort(stdscr, array)
                    
                case "heap":
                    heapSort(stdscr, array)

                case "cocktail":
                    cocktailSort(stdscr, array)

                case "selection":
                    selectionSort(stdscr, array)

                case "shell":
                    shellSort(stdscr, array)

                case "oddeven":
                    oddevenSort(stdscr, array)
                
                case "comb":
                    combSort(stdscr, array)

                case "bingo":
                    bingoSort(stdscr, array)

                case "radix":
                    radixSort(stdscr, array)
                
                case "pigeonhole":
                    pigeonholeSort(stdscr, array)
                
                case "pancake":
                    pancakeSort(stdscr, array, len(array))
            
            if forever == False:
                # Ends performance timer
                endTime = time.perf_counter()
            
            # draws array final time
            drawArray(stdscr, array, 0, "none")
            
            # if forever is false, stop running loop
            if forever == False:
                break
        
        # fills array after sorting
        if options['noFill'] == False:
            for i in range(arraySize):
                drawArray(stdscr, array, i, "fill")

        if options['info']:
            # Shows that array is sorted and other info
            stdscr.addstr(0, 0, "Array sorted!")
            stdscr.addstr(2, 0, "Sorting information:")
            stdscr.addstr(4, 0, f"sorting algorithm: {options['algorithm']} sort")
            stdscr.addstr(5, 0, f"array size: {arraySize}")
            stdscr.addstr(6, 0, f"array range: {arrayRange}")
            stdscr.addstr(7, 0, f"sorting time: {round(endTime - startTime, 3)} second(s)")
            stdscr.addstr(8, 0, f"delay: {options['waitTime']} millisecond(s)")
            stdscr.addstr(9, 0, f"bar size: {options['barSize']}")
            stdscr.addstr(10, 0, f"fill screen: {str(fillScreen).lower()}")
            stdscr.addstr(11, 0, f"text-only mode: {str(options['textOnly']).lower()}")

            stdscr.addstr(13, 0, "Press any key to exit")

        # moves cursor to bottom right of screen
        stdscr.move(termHeight - 1, termWidth - 1)
        
        # waits for key press and stops program
        stdscr.timeout(-1)
        stdscr.getch()

        curses.endwin()

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
        '-t', '--text',
        help='add this to make the program use text-only mode instead of using fancy bars',
        action='store_true',
    )
    parser.add_argument(
        '-i', '--info',
        help='shows sorting information after sorting',
        action='store_true',
    )
    parser.add_argument(
        '-nf', '--no_fill',
        help='when used, does not fill array after sorting',
        action='store_true',
    )
    parser.add_argument(
        '-ni', '--no_index',
        help='when used, does not show the index as a red bar if (or as  a \'@\' character if --text is enabled) when sorting',
        action='store_true',
    )
    parser.add_argument(
        '-b', '--bar_size',
        help='default is 1, meaning the program will display the bars with a width of 1 terminal character',
        default=1,
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
        textOnly = args.text,
        info = args.info,
        noFill = args.no_fill,
        noIndex = args.no_index,
        barSize = args.bar_size,
        waitTime = args.wait_time,
        algorithm = args.algorithm,
        size = args.size,
    )

if __name__ == '__main__':
    main()

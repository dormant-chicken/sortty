#!/usr/bin/env python3

version = 'v1.9-git'

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
    'pancake',
    'bead',
    'stooge',
    'inplace_merge',
    'tim'
    )

colors = (
    'red',
    'green',
    'blue',
    'cyan',
    'magenta',
    'yellow'
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
    # check for terminal resize
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
                char = options['barCharacter']
                effect = None

                # special cases
                # default is @ character
                if mode == 'fill':
                    if i <= index:
                        char = options['fillCharacter']

                # fills with characters when starting
                elif mode == 'start':
                    if i > index:
                        char = ' '

                # shows index
                elif mode == 'index' and not options['noIndex']:
                    if i == index:
                        # default is @ character
                        char = options['indexCharacter']
            else:
                char = ' '
                effect = getColor(options['barColor'])

                if mode == 'fill':
                    if i <= index:
                        # default is green
                        effect = getColor(options['fillColor'])

                elif mode == 'start':
                    if i > index:
                        effect = None

                elif mode == 'index' and not options['noIndex']:
                    if i == index:
                        # default is red
                        effect = getColor(options['indexColor'])

            # actual drawing
            if effect == None:
                stdscr.addstr(termHeight - 1 - j, startX + (i * barSize), char * barSize)
            else:
                stdscr.addstr(termHeight - 1 - j, startX + (i * barSize), char * barSize, effect)

    # moves cursor to bottom right of screen (less distracting)
    stdscr.move(termHeight - 1, termWidth - 1)

    # refresh screen and wait specified time
    stdscr.refresh()

    if mode == 'fill':
        time.sleep(((500 / len(array)) * barSize) / 1000)

    elif mode == 'shuffle':
        time.sleep(((600 / len(array)) * barSize) / 1000)

    elif mode == 'start':
        time.sleep(((300 / len(array)) * barSize) / 1000)

    else:
        time.sleep(options['waitDelay'] / 1000)

def getColor(color):
    match color:
        # default (white and reverse mean the same thing, no need to make another color pair)
        case None:
            return curses.A_REVERSE
        # if color is specified
        case 'red':
            return curses.color_pair(1)
        case 'green':
            return curses.color_pair(2)
        case 'blue':
            return curses.color_pair(3)
        case 'cyan':
            return curses.color_pair(4)
        case 'magenta':
            return curses.color_pair(5)
        case 'yellow':
            return curses.color_pair(6)

def bogoSort(stdscr, array, n):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n - 1):
            if(array[i] > array[i + 1]):
                sorted = False
                break
        if not sorted:
            random.shuffle(array)
            drawArray(stdscr, array, 0, None)

def bubbleSort(stdscr, array, n):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
            drawArray(stdscr, array, i + 1, 'index')

def merge(stdscr, array, left, mid, right):
    leftLen = mid - left + 1
    rightLen = right - mid

    leftArray = [0] * leftLen
    rightArray = [0] * rightLen

    # fill arrays
    for i in range(leftLen):
        leftArray[i] = array[left + i]
    for j in range(rightLen):
        rightArray[j] = array[mid + j + 1]

    i = 0
    j = 0
    k = left

    # sort
    while i < leftLen and j < rightLen:
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
            drawArray(stdscr, array, k, 'index')
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    while i < leftLen:
        array[k] = leftArray[i]
        i += 1
        k += 1

    while j < rightLen:
        array[k] = rightArray[j]
        j += 1
        k += 1

def mergeSort(stdscr, array, begin, end):
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    # call recursively on left subarray
    mergeSort(stdscr, array, begin, mid)
    # call recursively on right subarray
    mergeSort(stdscr, array, mid + 1, end)

    merge(stdscr, array, begin, mid, end)

def insertionSort(stdscr, array, left, right):
    for i in range(left + 1, right):
        j = i
        drawArray(stdscr, array, j, 'index')

        while array[j] < array[j - 1] and j > left:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            drawArray(stdscr, array, j, 'index')

def quickSort(stdscr, array, left, right):
    if left < right:
        partitionPos = partition(stdscr, array, left, right)
        quickSort(stdscr, array, left, partitionPos - 1)
        quickSort(stdscr, array, partitionPos + 1, right)

# used by quicksort function
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
            drawArray(stdscr, array, i, 'index')

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
    return i

def gnomeSort(stdscr, array, n):
    i = 0
    while i < n:
        if i == 0:
            i += 1

        if array[i] >= array[i - 1]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

        drawArray(stdscr, array, i, 'index')

def heapSort(stdscr, array, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(stdscr, array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]

        heapify(stdscr, array, i, 0)

# needed for heapsort
def heapify(stdscr, array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        drawArray(stdscr, array, l, 'index')

        heapify(stdscr, array, n, largest)

def cocktailSort(stdscr, array, n):
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                drawArray(stdscr, array, i + 1, 'index')

        if (not swapped):
            break

        swapped = False

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                drawArray(stdscr, array, i, 'index')

        start += 1

def selectionSort(stdscr, array, n):
    for i in range(n):
        minIdx = i

        # finds smallest index
        for j in range(i + 1, n):
            if array[minIdx] > array[j]:
                minIdx = j

        # swap
        array[i], array[minIdx] = array[minIdx], array[i]
        drawArray(stdscr, array, minIdx, 'index')

def shellSort(stdscr, array, n):
    gap = int(n / 2)

    while gap > 0:
        j = gap

        # sorts the array
        while j < n:
            i = j - gap

            while i >= 0:
                # swap if value on right is less
                if array[i + gap] < array[i]:
                    array[i + gap], array[i] = array[i], array[i + gap]
                    drawArray(stdscr, array, j, 'index')

                # move gap to sort
                i = i - gap

            j += 1

        # cuts gap size in half
        gap = int(gap / 2)

def oddevenSort(stdscr, array, n):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(1, n - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                drawArray(stdscr, array, i, 'index')

        for i in range(0, n - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                drawArray(stdscr, array, i, 'index')

def combSort(stdscr, array, n):
    gap = n

    swapped = True

    while gap != 1 or swapped:
        gap = getNextGap(gap)

        swapped = False

        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
                drawArray(stdscr, array, i, 'index')

# needed for combsort function
def getNextGap(gap):
    gap = int(gap / 1.3)

    if gap < 1:
        return 1
    return gap

def bingoSort(stdscr, array, n):
    # smallest element in array
    bingo = min(array)

    # largest element from
    largest = max(array)
    nextBingo = largest
    nextPos = 0

    while bingo < nextBingo:
        # keep track of element to put in correct position
        startPos = nextPos
        for i in range(startPos, n):
            if array[i] == bingo:
                array[i], array[nextPos] = array[nextPos], array[i]
                nextPos += 1
                drawArray(stdscr, array, nextPos, 'index')

            # finds next bingo elemnt
            elif array[i] < nextBingo:
                nextBingo = array[i]

        bingo = nextBingo
        nextBingo = largest

def radixSort(stdscr, array, n):
    maxArray = max(array)

    exp = 1
    while maxArray / exp >= 1:
        countingSort(stdscr, array, exp, n)
        exp *= 10

# needed for radixsort function
def countingSort(stdscr, array, exp, n):
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
    for i in range(0, n):
        array[i] = output[i]
        drawArray(stdscr, array, i, 'index')

def pigeonholeSort(stdscr, array, n):
    arrayMin = min(array)
    arrayMax = max(array)
    arrayRange = arrayMax - arrayMin + 1

    # fill pigeonhole array
    holes = [0] * arrayRange

    # populate pigeonholes
    j = 0
    for i in array:
        holes[i - arrayMin] += 1
        drawArray(stdscr, array, j, 'index')
        j += 1

    # put back elements
    i = 0
    for count in range(arrayRange):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + arrayMin
            i += 1
            drawArray(stdscr, array, i, 'index')

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
            pancakeFlip(stdscr, array, max)

            # flips again to bring max element next to current
            pancakeFlip(stdscr, array, current - 1)

        current -= 1

# needed for pancakesort function
def pancakeFlip(stdscr, array, i):
    # swaps elements until specified part of array is flipped
    start = 0

    while start < i:
        array[start], array[i] = array[i], array[start]
        start += 1
        i -= 1
        drawArray(stdscr, array, i, 'index')

def beadSort(stdscr, array, n):
    maximum = max(array)

    # declare beads
    beads = [[0 for i in range(maximum)] for j in range(n)]

    # mark beads
    for i in range(n):
        for j in range(array[i]):
            beads[i][j] = 1

    # move beads down
    for j in range(maximum):
        sum = 0

        # sort
        for i in range(n):
            sum += beads[i][j]
            beads[i][j] = 0

        for i in range(n - 1, n - sum - 1, -1):
            beads[i][j] = 1

        # compile into main array and draw
        for i in range(n):
            sum = 0
            for j in range(maximum):
                sum += beads[i][j]
            array[i] = sum

        drawArray(stdscr, array, 0, None)

def stoogeSort(stdscr, array, start, end):
    if start >= end:
        return

    # swap
    if array[start] > array[end]:
        array[start], array[end] = array[end], array[start]
        drawArray(stdscr, array, start, 'index')

    if end - start + 1 > 2:
        third = int((end - start + 1) / 3)

        # call recursively on first 2/3 of array
        stoogeSort(stdscr, array, start, end - third)
        # call recursively on last 2/3 of array
        stoogeSort(stdscr, array, start + third, end)
        # call recursively on first 2/3 of array again
        stoogeSort(stdscr, array, start, end - third)

def inPlaceMergeSort(stdscr, array, start, end):
    if start == end:
        return

    middle = math.floor((start + end) / 2)

    # call recursively on left subarray
    inPlaceMergeSort(stdscr, array, start, middle)
    # call recursively on right subarray
    inPlaceMergeSort(stdscr, array, middle + 1, end)

    inPlaceMerge(stdscr, array, start, end)

# needed by inPlaceMergeSort function
def inPlaceMerge(stdscr, array, start, end):
    middle = getMiddle(end - start + 1)

    while middle > 0:
        i = start
        while (i + middle) <= end:
            j = i + middle
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                drawArray(stdscr, array, i, 'index')
            i += 1

        middle = getMiddle(middle)

# needed by inPlaceMergeSort function
def getMiddle(length):
    if length <= 1:
        return 0

    return math.ceil(length / 2)

def timSort(stdscr, arr, minMerge, n):
    r = 0
    temp = n

    while temp >= minMerge:
        r |= temp & 1
        temp >>= 1
    minRun = temp + r

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(stdscr, arr, start, end + 1)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(stdscr, arr, left, mid, right)

        size = 2 * size

# function gives error if terminal is too small
def displayTermError(stdscr, termRequired, termCurrent, message, needed):
    stdscr.addstr(0, 0, str(message))
    stdscr.addstr(2, 0, f"required {needed}: {str(termRequired)} cells")
    stdscr.addstr(3, 0, f"terminal {needed}: {str(termCurrent)} cells")
    stdscr.addstr(5, 0, "please resize your terminal and try again")
    stdscr.addstr(7, 0, "press any key to exit")

    stdscr.getch()
    curses.endwin()

# check length of character given
def isSingleChar(char):
    if len(char) != 1:
        raise ValueError('character given is too long, only use a single character')

def run_sortty(stdscr):
    global options
    global termHeight
    global termWidth
    global startX

    # finds terminal info
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
        arraySize, arrayRange = options['size'].split('x')
        try:
            arraySize = int(arraySize)
            arrayRange = int(arrayRange)
        except ValueError:
            raise ValueError('Invalid size format: use HEIGTHxWIDTH')

    # check length of characters given
    isSingleChar(options['barCharacter'])
    isSingleChar(options['indexCharacter'])
    isSingleChar(options['fillCharacter'])

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
    stdscr.timeout(-1)
    stdscr.clear()

    # color pairs for ncurses
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_YELLOW)

    # quits program if terminal height too small
    if not fillScreen and (arrayRange > termHeight):
        displayTermError(stdscr, arrayRange, termHeight, "terminal height too small for array range!", "height")

    elif not fillScreen and (arraySize > termWidth):
        displayTermError(stdscr, arraySize, termWidth, "terminal width too small for array size!", "width")

    # otherwise, start main script
    else:
        # set delay for input
        stdscr.timeout(1)

        # draw the array before sorting
        if not options['noAnimation']:
            for i in range(arraySize):
                drawArray(stdscr, array, i, 'start')

        while True:
            # creates new algorithm
            if forever:
                algorithm = algorithms[random.randint(1, len(algorithms) - 1)]
            else:
                algorithm = options['algorithm']

            # waits before shuffle
            if not options['noAnimation']:
                time.sleep(750 / 1000)

            # shuffle array by swapping index with random element
            for i in range(arraySize):
                temp = random.randint(0, arraySize - 1)
                array[i], array[temp] = array[temp], array[i]
                if not options['noAnimation']:
                    drawArray(stdscr, array, 0, 'shuffle')

            if options['noAnimation']:
                drawArray(stdscr, array, 0, None)

            # waits before sorting
            time.sleep(1000 / 1000)

            if not forever:
                # starts performance timer
                startTime = time.perf_counter()

            # sorting algorithms
            match algorithm:
                case 'bogo':
                    bogoSort(stdscr, array, arraySize)

                case 'bubble':
                    bubbleSort(stdscr, array, arraySize)

                case 'merge':
                    mergeSort(stdscr, array, 0, arraySize - 1)

                case 'insertion':
                    insertionSort(stdscr, array, 0, arraySize)

                case 'quick':
                    quickSort(stdscr, array, 0, arraySize - 1)

                case 'gnome':
                    gnomeSort(stdscr, array, arraySize)

                case 'heap':
                    heapSort(stdscr, array, arraySize)

                case 'cocktail':
                    cocktailSort(stdscr, array, arraySize)

                case 'selection':
                    selectionSort(stdscr, array, arraySize)

                case 'shell':
                    shellSort(stdscr, array, arraySize)

                case 'oddeven':
                    oddevenSort(stdscr, array, arraySize)

                case 'comb':
                    combSort(stdscr, array, arraySize)

                case 'bingo':
                    bingoSort(stdscr, array, arraySize)

                case 'radix':
                    radixSort(stdscr, array, arraySize)

                case 'pigeonhole':
                    pigeonholeSort(stdscr, array, arraySize)

                case 'pancake':
                    pancakeSort(stdscr, array, arraySize)

                case 'bead':
                    beadSort(stdscr, array, arraySize)

                case 'stooge':
                    stoogeSort(stdscr, array, 0, arraySize - 1)

                case 'inplace_merge':
                    inPlaceMergeSort(stdscr, array, 0, arraySize - 1)

                case 'tim':
                    timSort(stdscr, array, 16, arraySize)

            if not forever:
                # ends performance timer
                endTime = time.perf_counter()

            # draws array final time
            drawArray(stdscr, array, 0, None)

            # if forever is false, stop running loop
            if not forever:
                break

        # fills array after sorting
        if not options['noFill']:
            for i in range(arraySize):
                drawArray(stdscr, array, i, 'fill')

        if options['info'] and termHeight > 15 and termWidth > 35:
            # shows sorting info
            stdscr.addstr(0, 0, "Array sorted!")

            stdscr.addstr(2, 0, "Sorting information:")

            stdscr.addstr(4, 0, f"sorting algorithm: {options['algorithm']} sort")
            stdscr.addstr(5, 0, f"array size: {arraySize}")
            stdscr.addstr(6, 0, f"array range: {arrayRange}")
            stdscr.addstr(7, 0, f"sorting time: {round(endTime - startTime, 3)} second(s)")
            stdscr.addstr(8, 0, f"delay: {options['waitDelay']} millisecond(s)")
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
    # this way you can use ctrl+c to quit without showing an error
    except KeyboardInterrupt:
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
        '-na', '--no_animation',
        help='when used, does not show fill and shuffle animation before sorting',
        action='store_true',
    )
    parser.add_argument(
        '-b', '--bar_size',
        help='default is 1, meaning the program will display the bars with a width of 1 terminal character',
        default=1,
        type=int,
    )
    parser.add_argument(
        '-w', '--wait',
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
        '-bc', '--bar_color',
        help='changes color of bars when sorting, does nothing if --text is used',
        default=None,
        choices=colors
    )
    parser.add_argument(
        '-ic', '--index_color',
        help='changes color of index pointer when sorting, does nothing if --text is used',
        default='red',
        choices=colors
    )
    parser.add_argument(
        '-fc', '--fill_color',
        help='changes color that fills the array after sorting, does nothing if --text is used',
        default='green',
        choices=colors
    )
    parser.add_argument(
        '-bch', '--bar_character',
        help='changes character for the bars when sorting, does nothing if --text is not used',
        default='@',
        type=str,
    )
    parser.add_argument(
        '-ich', '--index_character',
        help='changes character for the index pointer when sorting, does nothing if --text is not used',
        default='@',
        type=str,
    )
    parser.add_argument(
        '-fch', '--fill_character',
        help='changes character that fills the array after sorting, does nothing if --text is not used',
        default='#',
        type=str,
    )
    parser.add_argument(
        '-s', '--size',
        help='HEIGTHxWIDTH, if not specified, the program will adapt to terminal size',
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
        noAnimation = args.no_animation,
        barSize = args.bar_size,
        waitDelay = args.wait,
        algorithm = args.algorithm,
        barColor = args.bar_color,
        indexColor = args.index_color,
        fillColor = args.fill_color,
        barCharacter = args.bar_character,
        indexCharacter = args.index_character,
        fillCharacter = args.fill_character,
        size = args.size,
    )

if __name__ == '__main__':
    main()

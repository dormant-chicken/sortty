#!/usr/bin/env python3

version = 'v1.9-git'

import argparse
import curses
import random
import time
import math
import sys
import os
import pysine

logo = '''
                   _    _          
 ___   ___   _ __ | |_ | |_  _   _ 
/ __| / _ \ | '__|| __|| __|| | | |
\__ \| (_) || |   | |_ | |_ | |_| |
|___/ \___/ |_|    \__| \__| \__, |
                             |___/ 
'''

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
	'tim',
	'circle'
	)

colors = (
	'red',
	'green',
	'blue',
	'cyan',
	'magenta',
	'yellow',
	'white',
	'transparent'
	)

def drawArray(stdscr, array: list[int], *args: list[str, int]) -> None:
	# check for terminal resize
	resize = stdscr.getch()

	if resize == curses.KEY_RESIZE:
		stdscr.clear()
		curses.endwin()
		sortty(**options)
		sys.exit(0)

	stdscr.clear()

	barSize = options['barSize']

	mode = None

	# get mode
	if len(args) > 0:
		mode = args[0]

	# draws the array onto the screen
	for i in range(len(array)):
		for j in range(array[i]):
			# checks if text-only mode is enabled
			if options['textOnly']:
				# defaults
				char = options['barCharacter']
				effect = None

				# handles cases where mode is specified
				if mode is not None:
					# special cases
					# default is @ character
					if mode == 'fill':
						if i <= args[1]:
							char = options['fillCharacter']

					# fills with characters when starting
					elif mode == 'start':
						if i > args[1]:
							char = ' '

					# shows index
					elif mode == 'index' and not options['noIndex']:
						# goes through arguments to check index given
						for k in range(1, len(args)):
							if i == args[k]:
								# default is @ character
								char = options['indexCharacter']
			else:
				char = ' '
				effect = getColor(options['barColor'])

				if mode is not None:
					if mode == 'fill':
						if i <= args[1]:
							# default is green
							effect = getColor(options['fillColor'])

					elif mode == 'start':
						if i > args[1]:
							effect = None

					elif mode == 'index' and not options['noIndex']:
						for k in range(1, len(args)):
							if i == args[k]:
								# default is red
								effect = getColor(options['indexColor'])

			# actual drawing
			if effect is None:
				stdscr.addstr(termHeight - 1 - j, startX + (i * barSize), char * barSize)
			else:
				stdscr.addstr(termHeight - 1 - j, startX + (i * barSize), char * barSize, effect)

	# moves cursor to bottom right of screen (less distracting)
	stdscr.move(termHeight - 1, termWidth - 1)

	# refresh screen and wait specified time
	stdscr.refresh()

	# play sound
	if not options['noSound']:
		match mode:
			case 'fill' | 'shuffle' | 'index':
				# in gnome sort, the index goes over the length of the array and causes an error, this checks if the index given is too high
				if args[1] < len(array):
					pysine.sine(frequency=float(array[args[1]] * options['soundPitch']), duration=0.05)

	# available modes: fill, start, index, shuffle
	match mode:
		case 'fill' | 'shuffle' | 'start':
			if options['animationDelay'] is None:
				# dynamic option if not specified
				time.sleep(800 / len(array) / 1000)
			else:
				time.sleep(options['animationDelay'] / 1000)

		case default:
			time.sleep(options['delay'] / 1000)

# dictionary of colors
def getColor(color: str):
	match color:
		case 'red':			return curses.color_pair(1)
		case 'green':		return curses.color_pair(2)
		case 'blue':		return curses.color_pair(3)
		case 'cyan':		return curses.color_pair(4)
		case 'magenta':		return curses.color_pair(5)
		case 'yellow':		return curses.color_pair(6)
		# white and reverse mean the same thing, no need to make another color pair
		case 'white':		return curses.A_REVERSE
		case 'transparent':	return None

def bogoSort(stdscr, array: list[int], n: int) -> None:
	sorted = False

	while not sorted:
		sorted = True
		for i in range(n - 1):
			if(array[i] > array[i + 1]):
				sorted = False
				break
		if not sorted:
			random.shuffle(array)
			drawArray(stdscr, array)

def bubbleSort(stdscr, array: list[int], n: int) -> None:
	sorted = False

	while not sorted:
		sorted = True
		for i in range(n - 1):
			if array[i] > array[i + 1]:
				sorted = False
				array[i], array[i + 1] = array[i + 1], array[i]
			drawArray(stdscr, array, 'index', i + 1)

def merge(stdscr, array: list[int], left: int, mid: int, right: int) -> None:
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
			drawArray(stdscr, array, 'index', k)
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

def mergeSort(stdscr, array: list[int], begin: int, end: int) -> None:
	if begin >= end:
		return

	mid = begin + (end - begin) // 2
	# call recursively on left subarray
	mergeSort(stdscr, array, begin, mid)
	# call recursively on right subarray
	mergeSort(stdscr, array, mid + 1, end)

	merge(stdscr, array, begin, mid, end)

def insertionSort(stdscr, array: list[int], left: int, right: int) -> None:
	for i in range(left + 1, right):
		j = i
		drawArray(stdscr, array, 'index', j)

		while array[j] < array[j - 1] and j > left:
			array[j - 1], array[j] = array[j], array[j - 1]
			j -= 1
			drawArray(stdscr, array, 'index', j)

def quickSort(stdscr, array, left, right) -> None:
	if left < right:
		partitionPos = partition(stdscr, array, left, right)
		quickSort(stdscr, array, left, partitionPos - 1)
		quickSort(stdscr, array, partitionPos + 1, right)

# used by quicksort function
def partition(stdscr, array: list[int], left: int, right: int) -> int:
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
			drawArray(stdscr, array, 'index', i, j)

	if array[i] > pivot:
		array[i], array[right] = array[right], array[i]

	return i

def gnomeSort(stdscr, array: list[int], n: int) -> None:
	i = 0
	while i < n:
		if i == 0:
			i += 1

		if array[i] >= array[i - 1]:
			i += 1
		else:
			array[i], array[i - 1] = array[i - 1], array[i]
			i -= 1

		drawArray(stdscr, array, 'index', i)

def heapSort(stdscr, array: list[int], n: int) -> None:
	for i in range(n//2 - 1, -1, -1):
		heapify(stdscr, array, n, i)

	for i in range(n - 1, 0, -1):
		array[i], array[0] = array[0], array[i]

		heapify(stdscr, array, i, 0)

# needed for heapsort
def heapify(stdscr, array: list[int], n: int, i: int) -> None:
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and array[largest] < array[l]:
		largest = l

	if r < n and array[largest] < array[r]:
		largest = r

	if largest != i:
		array[i], array[largest] = array[largest], array[i]
		drawArray(stdscr, array, 'index', l)

		heapify(stdscr, array, n, largest)

def cocktailSort(stdscr, array: list[int], n: int) -> None:
	swapped = True
	start = 0
	end = n - 1
	while (swapped == True):

		swapped = False

		for i in range(start, end):
			if (array[i] > array[i + 1]):
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True
				drawArray(stdscr, array, 'index', i + 1)

		if (not swapped):
			break

		swapped = False

		end -= 1

		for i in range(end - 1, start - 1, -1):
			if (array[i] > array[i + 1]):
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True
				drawArray(stdscr, array, 'index', i)

		start += 1

def selectionSort(stdscr, array: list[int], n: int) -> None:
	for i in range(n):
		minIdx = i

		# finds smallest index
		for j in range(i + 1, n):
			if array[minIdx] > array[j]:
				minIdx = j
			drawArray(stdscr, array, 'index', j)

		# swap
		array[i], array[minIdx] = array[minIdx], array[i]
		drawArray(stdscr, array, 'index', minIdx)

def shellSort(stdscr, array: list[int], n: int) -> None:
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
					drawArray(stdscr, array, 'index', i, j)

				# move gap to sort
				i = i - gap

			j += 1

		# cuts gap size in half
		gap = int(gap / 2)

def oddevenSort(stdscr, array: list[int], n: int) -> None:
	sorted = False

	while not sorted:
		sorted = True

		for i in range(1, n - 1, 2):
			if array[i] > array[i + 1]:
				# swap elements
				array[i], array[i + 1] = array[i + 1], array[i]
				sorted = False
				drawArray(stdscr, array, 'index', i)

		for i in range(0, n - 1, 2):
			if array[i] > array[i + 1]:
				# swap elements
				array[i], array[i + 1] = array[i + 1], array[i]
				sorted = False
				drawArray(stdscr, array, 'index', i)

def combSort(stdscr, array: list[int], n: int) -> None:
	gap = n

	swapped = True

	while gap != 1 or swapped:
		gap = getNextGap(gap)

		swapped = False

		for i in range(0, n - gap):
			if array[i] > array[i + gap]:
				array[i], array[i + gap] = array[i + gap], array[i]
				swapped = True
				drawArray(stdscr, array, 'index', i)

# needed for combsort function
def getNextGap(gap: int) -> int:
	gap = int(gap / 1.3)
	if gap < 1:
		return 1

	return gap

def bingoSort(stdscr, array: list[int], n: int) -> None:
	# smallest element in array
	bingo = min(array)

	# largest element in array
	arrayMax = max(array)
	nextBingo = arrayMax
	nextPos = 0

	while bingo < nextBingo:
		# keep track of element to put in correct position
		startPos = nextPos
		for i in range(startPos, n):
			drawArray(stdscr, array, 'index', i)

			if array[i] == bingo:
				array[i], array[nextPos] = array[nextPos], array[i]
				nextPos += 1
				drawArray(stdscr, array, 'index', nextPos)

			# finds next bingo elemnt
			elif array[i] < nextBingo:
				nextBingo = array[i]

		bingo = nextBingo
		nextBingo = arrayMax

def radixSort(stdscr, array: list[int], n: int) -> None:
	arrayMax = max(array)

	exp = 1
	while arrayMax / exp >= 1:
		countingSort(stdscr, array, exp, n)
		exp *= 10

# needed for radixsort function
def countingSort(stdscr, array: list[int], exp: int, n: int) -> None:
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
		drawArray(stdscr, array, 'index', i)

def pigeonholeSort(stdscr, array: list[int], n: int) -> None:
	arrayMin = min(array)
	arrayMax = max(array)
	arrayRange = arrayMax - arrayMin + 1

	# fill pigeonhole array
	holes = [0] * arrayRange

	# populate pigeonholes
	j = 0
	for i in array:
		holes[i - arrayMin] += 1
		drawArray(stdscr, array, 'index', j)
		j += 1

	# put back elements
	i = 0
	for count in range(arrayRange):
		while holes[count] > 0:
			holes[count] -= 1
			array[i] = count + arrayMin
			i += 1
			drawArray(stdscr, array, 'index', i)

def pancakeSort(stdscr, array: list[int], n: int) -> None:
	current = n
	while current > 1:
		# finds max element in array
		arrayMax = 0

		for i in range(current):
			if array[i] > array[arrayMax]:
				arrayMax = i

		if arrayMax != (current - 1):
			# flips once to bring max to first element of array
			pancakeFlip(stdscr, array, arrayMax)

			# flips again to bring max element next to current
			pancakeFlip(stdscr, array, current - 1)

		current -= 1

# needed for pancakesort function
def pancakeFlip(stdscr, array: list[int], n: int) -> None:
	# swaps elements until specified part of array is flipped
	start = 0

	while start < n:
		array[start], array[n] = array[n], array[start]
		start += 1
		n -= 1
		drawArray(stdscr, array, 'index', start, n)

def beadSort(stdscr, array: list[int], n: int) -> None:
	arrayMax = max(array)

	# declare beads
	beads = [[0 for i in range(arrayMax)] for j in range(n)]

	# mark beads
	for i in range(n):
		for j in range(array[i]):
			beads[i][j] = 1

	# move beads down
	for j in range(arrayMax):
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
			for j in range(arrayMax):
				sum += beads[i][j]
			array[i] = sum

		drawArray(stdscr, array)

def stoogeSort(stdscr, array: list[int], start: int, end: int) -> None:
	if start >= end:
		return

	# swap
	if array[start] > array[end]:
		array[start], array[end] = array[end], array[start]
		drawArray(stdscr, array, 'index', start)

	if end - start + 1 > 2:
		third = int((end - start + 1) / 3)

		# call recursively on first 2/3 of array
		stoogeSort(stdscr, array, start, end - third)
		# call recursively on last 2/3 of array
		stoogeSort(stdscr, array, start + third, end)
		# call recursively on first 2/3 of array again
		stoogeSort(stdscr, array, start, end - third)

def inPlaceMergeSort(stdscr, array: list[int], start: int, end: int) -> None:
	if start == end:
		return

	middle = int((start + end) / 2)

	# call recursively on left subarray
	inPlaceMergeSort(stdscr, array, start, middle)
	# call recursively on right subarray
	inPlaceMergeSort(stdscr, array, middle + 1, end)

	inPlaceMerge(stdscr, array, start, end)

# needed by inPlaceMergeSort function
def inPlaceMerge(stdscr, array: list[int], start: int, end: int) -> None:
	middle = getMiddle(end - start + 1)

	while middle > 0:
		i = start
		while (i + middle) <= end:
			j = i + middle
			if array[i] > array[j]:
				array[i], array[j] = array[j], array[i]
				drawArray(stdscr, array, 'index', i, j)
			i += 1

		middle = getMiddle(middle)

# needed by inPlaceMergeSort function
def getMiddle(length: int) -> int:
	if length <= 1:
		return 0

	return math.ceil(length / 2)

def timSort(stdscr, array: list[int], minMerge: int, n: int) -> None:
	r = 0
	temp = n

	while temp >= minMerge:
		r |= temp & 1
		temp >>= 1
	minRun = temp + r

	for start in range(0, n, minRun):
		end = min(start + minRun - 1, n - 1)
		insertionSort(stdscr, array, start, end + 1)

	size = minRun
	while size < n:

		for left in range(0, n, 2 * size):
			mid = min(n - 1, left + size - 1)
			right = min((left + 2 * size - 1), (n - 1))

			if mid < right:
				merge(stdscr, array, left, mid, right)

		size = 2 * size

def circleSort(stdscr, array: list[int], arraySize: int) -> None:
	notSorted = True
	while notSorted:
		notSorted = circle(stdscr, array, 0, arraySize - 1)

# needed by circleSort function
def circle(stdscr, array: list[int], low: int, high: int) -> bool:
		swapped = False

		if low == high:
			return swapped

		left = low
		right = high

		while left < right:
			if array[left] > array[right]:
				array[left], array[right] = array[right], array[left]
				swapped = True
			drawArray(stdscr, array, 'index', left, right)

			left += 1
			right -= 1

		if left == right and array[left] > array[right + 1]:
			array[left], array[right + 1] = array[right + 1], array[left]
			swapped = True
		drawArray(stdscr, array, 'index', left, right)

		mid = low + int((high - low) / 2)
		left_swap = circle(stdscr, array, low, mid)
		right_swap = circle(stdscr, array, mid + 1, high)

		return swapped or left_swap or right_swap

# function gives error if terminal is too small
def displayTermError(stdscr, termRequired: int, termCurrent: int, message: str, needed: str) -> None:
	stdscr.addstr(0, 0, str(message))

	stdscr.addstr(2, 0, f'required {needed}: {str(termRequired)} cells')
	stdscr.addstr(3, 0, f'terminal {needed}: {str(termCurrent)} cells')

	stdscr.addstr(5, 0, 'please resize your terminal and try again')

	stdscr.addstr(7, 0, 'press any key to exit')

	stdscr.getch()
	curses.endwin()
	os.system('clear')
	sys.exit(0)

# check length of character given
def isSingleChar(char: str) -> None:
	if len(char) != 1:
		raise ValueError('character given is too long, please only use a single character')

def runSortty(stdscr):
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
		sortForever = True
	else:
		sortForever = False

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
	for i in ('barCharacter', 'indexCharacter', 'fillCharacter'):
		isSingleChar(options[i])

	# array declaration
	array = []

	# finds slope using array range and array size (slope = rise / run)
	slope = arrayRange / arraySize
	barHeight = 0

	for i in range(arraySize):
		barHeight += slope
		array.append(math.ceil(barHeight))

	# finds correct position to start drawing
	startX = int(termWidth / 2) - int((arraySize * options['barSize']) / 2)

	# curses initialization
	curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.timeout(-1)
	stdscr.clear()

	# initialize color pairs for ncurses
	for count, pair in enumerate((curses.COLOR_RED, curses.COLOR_GREEN, curses.COLOR_BLUE, curses.COLOR_CYAN, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)):
		curses.init_pair(count + 1, pair, pair)

	# quits program if terminal height too small
	if not fillScreen and (arrayRange > termHeight):
		displayTermError(stdscr, arrayRange, termHeight, 'terminal height too small for array range!', 'height')

	if not fillScreen and (arraySize > termWidth):
		displayTermError(stdscr, arraySize, termWidth, 'terminal width too small for array size!', 'width')

	# otherwise, start main script
	# set delay for input
	stdscr.timeout(1)

	# draw the array before sorting
	if not options['noAnimation']:
		for i in range(arraySize):
			drawArray(stdscr, array, 'start', i)

	# not using --algorithm forever will break this loop
	while True:
		# creates new algorithm
		if sortForever:
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
				drawArray(stdscr, array, 'shuffle', i)

		if options['noAnimation']:
			drawArray(stdscr, array)

		# waits before sorting
		time.sleep(1000 / 1000)

		# starts performance timer
		if not sortForever:
			startTime = time.perf_counter()

		# sorting algorithms
		match algorithm:
			case 'bogo':			bogoSort		(stdscr, array, arraySize)
			case 'bubble':			bubbleSort		(stdscr, array, arraySize)
			case 'merge':			mergeSort		(stdscr, array, 0, arraySize - 1)
			case 'insertion':		insertionSort	(stdscr, array, 0, arraySize)
			case 'quick':			quickSort		(stdscr, array, 0, arraySize - 1)
			case 'gnome':			gnomeSort		(stdscr, array, arraySize)
			case 'heap':			heapSort		(stdscr, array, arraySize)
			case 'cocktail':		cocktailSort	(stdscr, array, arraySize)
			case 'selection':		selectionSort	(stdscr, array, arraySize)
			case 'shell':			shellSort		(stdscr, array, arraySize)
			case 'oddeven':			oddevenSort		(stdscr, array, arraySize)
			case 'comb':			combSort		(stdscr, array, arraySize)
			case 'bingo':			bingoSort		(stdscr, array, arraySize)
			case 'radix':			radixSort		(stdscr, array, arraySize)
			case 'pigeonhole':		pigeonholeSort	(stdscr, array, arraySize)
			case 'pancake':			pancakeSort		(stdscr, array, arraySize)
			case 'bead':			beadSort		(stdscr, array, arraySize)
			case 'stooge':			stoogeSort		(stdscr, array, 0, arraySize - 1)
			case 'inplace_merge':	inPlaceMergeSort(stdscr, array, 0, arraySize - 1)
			case 'tim':				timSort			(stdscr, array, 16, arraySize)
			case 'circle':			circleSort		(stdscr, array, arraySize)

		# ends performance timer
		if not sortForever:
			endTime = time.perf_counter()

		# draws array final time
		drawArray(stdscr, array)

		# if forever is false, stop running loop
		if not sortForever:
			break

	# fills array after sorting
	if not options['noFill']:
		for i in range(arraySize):
			drawArray(stdscr, array, 'fill', i)

	# show info if terminal is big enough
	if options['info'] and termHeight > 15 and termWidth > 35:
		# shows sorting info
		stdscr.addstr(0, 0, 'Array sorted!')

		stdscr.addstr(2, 0, 'Sorting information:')

		stdscr.addstr(4, 0, f'sorting algorithm: {options["algorithm"]} sort')
		stdscr.addstr(5, 0, f'array size: {arraySize}')
		stdscr.addstr(6, 0, f'array range: {arrayRange}')
		stdscr.addstr(7, 0, f'sorting time: {round(endTime - startTime, 3)} second(s)')
		stdscr.addstr(8, 0, f'delay: {options["delay"]} millisecond(s)')
		stdscr.addstr(9, 0, f'bar size: {options["barSize"]}')
		stdscr.addstr(10, 0, f'fill screen: {str(fillScreen).lower()}')
		stdscr.addstr(11, 0, f'text-only mode: {str(options["textOnly"]).lower()}')

		stdscr.addstr(13, 0, 'Press any key to exit')

	# moves cursor to bottom right of screen
	stdscr.move(termHeight - 1, termWidth - 1)

	# waits for key press and stops program
	stdscr.timeout(-1)
	stdscr.getch()

	curses.endwin()

	# clear terminal to get rid of audio logs
	os.system('clear')

def sortty(**options):
	try:
		globals()['options'] = options
		curses.wrapper(runSortty)
	# clear screen and exit when pressing ctrl + c
	except KeyboardInterrupt:
		os.system('clear')
		sys.exit(0)

# edit print message function to make it show ascii art
class ArgumentParser(argparse.ArgumentParser):
	def print_help(self):
		print(logo)
		return super(ArgumentParser, self).print_help()

def main():
	parser = ArgumentParser(
		epilog='''Note: you can set the algorithm to 'forever' like this:
\'sortty --algorithm forever\'
Setting it to forever makes the program shuffle the array and sort it with a random algorithm forever (excluding bogo sort)'''
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
		help='when used, does not show the index as a red bar if (or as a \'@\' character if --text is enabled) when sorting',
		action='store_true',
	)
	parser.add_argument(
		'-na', '--no_animation',
		help='when used, does not show fill and shuffle animation before sorting',
		action='store_true',
	)
	parser.add_argument(
		'-ns', '--no_sound',
		help='disables playing sound depending on current index',
		action='store_true',
	)
	parser.add_argument(
		'-sp', '--sound_pitch',
		help='default is 30, increasing it will increase the pitch depending on current index, does nothing if --no_sound is used',
		default='30',
		type=int,
	) 
	parser.add_argument(
		'-bs', '--bar_size',
		help='default is 2, increasing it will lower the size of the bars based on your terminal',
		default=2,
		type=int,
	)
	parser.add_argument(
		'-d', '--delay',
		help='default is 50, meaning the program will wait 50ms before refreshing the screen',
		default=50,
		type=int,
	)
	parser.add_argument(
		'-ad', '--animation_delay',
		help='if not specified, the program will wait wait a dynamic amount of time based on the size of the array before refreshing animations',
		default=None,
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
		default='white',
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
		default='#',
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
		default='$',
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

	# clears audio logs
	try:
		args = parser.parse_args()
	except:
		os.system('clear')
		args = parser.parse_args()
		sys.exit(0)

	# finally, call the function to run sortty
	sortty(
		textOnly = args.text,
		info = args.info,
		noFill = args.no_fill,
		noIndex = args.no_index,
		noAnimation = args.no_animation,
		noSound = args.no_sound,
		soundPitch = args.sound_pitch,
		barSize = args.bar_size,
		delay = args.delay,
		animationDelay = args.animation_delay,
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

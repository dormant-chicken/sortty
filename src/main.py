import os, sys, curses, time, random, math
from curses import wrapper

# Finds terminal info
term_size = os.get_terminal_size()
term_height = term_size.lines
term_width = term_size.columns

# used for filling array with green
def draw_array(stdscr, wait_delay, startx, array, index, mode):
    stdscr.clear()

    # This draws the array onto the screen
    bar_size = int(sys.argv[2])
    for i in range(len(array)):
        for j in range(array[i]):
            # Checks if [ fancy ] is True
            match int(sys.argv[1]):
                case 1:
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
                case 0:
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
        time.sleep(5 / 1000)

    elif mode == "shuffle":
        time.sleep(5 / 1000)

    elif mode == "start":
        time.sleep(3 / 1000)

    else:
        time.sleep(int(sys.argv[3]) / 1000)

# Bogosort
def bogo_sort(stdscr, wait_delay, startx, array):

    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if(array[i] > array[i + 1]):
                sorted = False
                break
        if not sorted:
            random.shuffle(array)
            if wait_delay:
                draw_array(stdscr, wait_delay, startx, array, 0, "none")

# Bubblesort
def bubble_sort(stdscr, wait_delay, startx, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
            if wait_delay:
                draw_array(stdscr, wait_delay, startx, array, i + 1, "mark_element")

# Mergesort
def merge_sort(stdscr, wait_delay, startx, arr, is_main):

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(stdscr, wait_delay, startx, left_arr, False)
        merge_sort(stdscr, wait_delay, startx, right_arr, False)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                if is_main == True and wait_delay:
                    draw_array(stdscr, wait_delay, startx, arr, 0, "none")
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
def insertion_sort(stdscr, wait_delay, startx, arr):
    for i in range(1, len(arr)):
        j = i
        if wait_delay:
            draw_array(stdscr, wait_delay, startx, arr, j, "mark_element")
        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            if wait_delay:
                draw_array(stdscr, wait_delay, startx, arr, j, "mark_element")

# Quicksort
def quick_sort(stdscr, wait_delay, startx, arr, left, right):
    if left < right:
        partition_pos = partition(stdscr, wait_delay, startx, arr, left, right)
        quick_sort(stdscr, wait_delay, startx, arr, left, partition_pos - 1)
        quick_sort(stdscr, wait_delay, startx, arr, partition_pos + 1, right)

# Used by quicksort function
def partition(stdscr, wait_delay, startx, arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            if wait_delay:
                draw_array(stdscr, wait_delay, startx, arr, i, "mark_element")
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

# Gnomesort
def gnome_sort(stdscr, wait_delay, startx, arr):
    i = 0
    while i < len(arr): 
        if i == 0: 
            i += 1
            
        if arr[i] >= arr[i - 1]: 
            i += 1
            if wait_delay:
                draw_array(stdscr, wait_delay, startx, arr, i, "mark_element")

        else: 
            arr[i], arr[i - 1] = arr[i - 1], arr[i] 
            i -= 1
            if wait_delay:
                draw_array(stdscr, wait_delay, startx, arr, i, "mark_element")

# Heapsort
def heap_sort(stdscr, wait_delay, startx, arr):
    N = len(arr)

    for i in range(N//2 - 1, -1, -1):
        heapify(stdscr, wait_delay, startx, arr, N, i)

    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(stdscr, wait_delay, startx, arr, i, 0)

# Needed for heapsort
def heapify(stdscr, wait_delay, startx, arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        if wait_delay:
            draw_array(stdscr, wait_delay, startx, arr, l, "mark_element")

        heapify(stdscr, wait_delay, startx, arr, N, largest)

# Cocktailsort
def cocktail_sort(stdscr, wait_delay, startx, array):
    swapped = True
    start = 0
    end = len(array) - 1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                if wait_delay:
                    draw_array(stdscr, wait_delay, startx, array, i + 1, "mark_element")

        if (swapped == False):
            break

        swapped = False

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                if wait_delay:
                    draw_array(stdscr, wait_delay, startx, array, i, "mark_element")

        start += 1

# Selectionsort
def selection_sort(stdscr, wait_delay, startx, array):
    for i in range(len(array)):
        min_idx = i

        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        if wait_delay:
            draw_array(stdscr, wait_delay, startx, array, min_idx, "mark_element")

# Shellsort
def shell_sort(stdscr, wait_delay, startx, array):
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
                    if wait_delay:
                        draw_array(stdscr, wait_delay, startx, array, j, "mark_element")
                
                # Move gap to sort
                i = i - gap

            j += 1

        # Cuts gap size in half
        gap = int(gap / 2)

# Oddevensort
def oddeven_sort(stdscr, wait_delay, startx, array):
    sorted = False

    while sorted == False:
        sorted = True

        for i in range(1, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                if wait_delay:
                    draw_array(stdscr, wait_delay, startx, array, i, "mark_element")
                
        for i in range(0, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # swap elements
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                if wait_delay:
                    draw_array(stdscr, wait_delay, startx, array, i, "mark_element")

# Combsort
def comb_sort(stdscr, wait_delay, startx, array):
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
                if wait_delay:
                    draw_array(stdscr, wait_delay, startx, array, i, "mark_element")

# Needed for combsort
def get_next_gap(gap):

    gap = int(gap / 1.3)
    if gap < 1:
        return 1
    return gap

def bingo_sort(stdscr, wait_delay, startx, array):
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
                if wait_delay:
                    draw_array(stdscr, wait_delay, startx, array, nextPos, "mark_element")
                
            # finds next bingo elemnt
            elif array[i] < next_bingo:
                next_bingo = array[i]
        bingo = next_bingo
        next_bingo = largest

# Radixsort
def radix_sort(stdscr, wait_delay, startx, array):
    max_array = max(array)

    exp = 1
    while max_array / exp >= 1:
        counting_sort(stdscr, wait_delay, startx, array, exp)
        exp *= 10

# Needed for radixsort
def counting_sort(stdscr, wait_delay, startx, array, exp):
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
        if wait_delay:
            draw_array(stdscr, wait_delay, startx, array, i, "mark_element")

# Function gives error if terminal is too small
def give_term_error(stdscr, term_required, term_current, message, needed):
    stdscr.addstr(0, 0, str(message))
    stdscr.addstr(2, 0, "required " + needed + ": " + str(term_required) + " cells")
    stdscr.addstr(3, 0, "terminal " + needed + ": " + str(term_current) + " cells")
    stdscr.addstr(5, 0, "please resize your terminal and try again")
    stdscr.addstr(7, 0, "press any key to exit")
    stdscr.getch()
    curses.endwin()

def main(stdscr):
    # If True, instantly sort the array without drawing
    if int(sys.argv[3]) == 0:
        wait_delay = False
    else:
        wait_delay = True

    # If not filled, makes the array size and range the highest possible that can fit on the screen
    if int(sys.argv[5]) == -1:
        fill_screen = True
        array_size = int(term_width / (int(sys.argv[2]))) - 2
        array_range = term_height - 2
    else:
        fill_screen = False
        array_size = int(sys.argv[5])
        array_range = int(sys.argv[6])
    
    # array declaration
    array = []

    # finds slope using array range and array size (slope = rise / run)
    slope = array_range / array_size
    bar_height = 0
    
    for i in range(array_size):
        bar_height += slope
        array.append(math.ceil(bar_height))

    # Finds correct position to start drawing
    startx = math.floor(term_width / 2) - math.floor(array_size * (int(sys.argv[2])) / 2)

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
        if wait_delay:
            for i in range(array_size):
                draw_array(stdscr, wait_delay, startx, array, i, "start")

        # waits before shuffle
        time.sleep(750 / 1000)

        # shuffle array
        for i in range(array_size):
            temp = random.randint(0, array_size - 1)
            array[i], array[temp] = array[temp], array[i]
            draw_array(stdscr, wait_delay, startx, array, 0, "shuffle")
        
        # waits before sorting
        time.sleep(1000 / 1000)

        # Starts performance timer
        start_time = time.perf_counter()

        # Sorting algorithms determined by bash script
        match sys.argv[4]:
            case "bogo":
                bogo_sort(stdscr, wait_delay, startx, array)

            case "bubble":
                bubble_sort(stdscr, wait_delay, startx, array)

            case "merge":
                merge_sort(stdscr, wait_delay, startx, array, True)

            case "insertion":
                insertion_sort(stdscr, wait_delay, startx, array)

            case "quick":
                quick_sort(stdscr, wait_delay, startx, array, 0, len(array) - 1)

            case "gnome":
                gnome_sort(stdscr, wait_delay, startx, array)
                
            case "heap":
                heap_sort(stdscr, wait_delay, startx, array)

            case "cocktail":
                cocktail_sort(stdscr, wait_delay, startx, array)

            case "selection":
                selection_sort(stdscr, wait_delay, startx, array)

            case "shell":
                shell_sort(stdscr, wait_delay, startx, array)

            case "oddeven":
                oddeven_sort(stdscr, wait_delay, startx, array)
            
            case "comb":
                comb_sort(stdscr, wait_delay, startx, array)

            case "bingo":
                bingo_sort(stdscr, wait_delay, startx, array)

            case "radix":
                radix_sort(stdscr, wait_delay, startx, array)
        
        # Ends performance timer
        end_time = time.perf_counter()

        # Only draw at the end of sorting when wait_delay is on, otherwise it would just show the array being unsorted
        if not wait_delay:
            draw_array(stdscr, wait_delay, startx, array, 0, "none")
        
        # fills array with green after sorting
        for i in range(array_size):
            draw_array(stdscr, wait_delay, startx, array, i, "fill")

        # Finds where to place sort_info text
        text_x = 0

        # Shows that array is sorted and other info
        stdscr.addstr(0, text_x, "Array sorted!")
        stdscr.addstr(2, text_x, "Sorting information:")
        stdscr.addstr(4, text_x, "sorting algorithm: " + str(sys.argv[4]) + "sort")
        stdscr.addstr(5, text_x, "array size: " + str(array_size))
        stdscr.addstr(6, text_x, "array range: " + str(array_range))
        stdscr.addstr(7, text_x, "time taken to sort: " + str(round(end_time - start_time, 3)) + " second(s)")
        stdscr.addstr(8, text_x, "delay: " + str(sys.argv[3]) + " millisecond(s)")
        stdscr.addstr(9, text_x, "bar size: " + sys.argv[2])

        # only attempt to display extra arguments if user specified
        if int(sys.argv[5]) == -1:
            stdscr.addstr(10, text_x, "command used: sortty " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4])
        else:
            stdscr.addstr(10, text_x, "command used: sortty " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " " + sys.argv[6])

        stdscr.addstr(12, text_x, "Press any key to exit")
        
        # Waits for key press and stops program
        stdscr.getch()
        curses.endwin()

wrapper(main)

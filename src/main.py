import os, sys, curses, time, random, math
from curses import wrapper

def draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, array):
    stdscr.clear()

    # This draws the array onto the screen
    i = 0
    j = 0
    for i in range(len(array)):
        for j in range(array[i]):
            if reverse:
                stdscr.addstr(term_height - 1 - j, startx - (i * 2), "#")
            else:
                stdscr.addstr(term_height - 1 - j, startx + (i * 2), "#")

    stdscr.refresh()
    if wait_delay:
        time.sleep(int(sys.argv[6]) / 1000)

# Maybe merge this into the bogosort function if it is unused by other functions
def is_array_sorted(array):
    sorted = True
    i = 1
    while i < len(array):
        if(array[i] < array[i - 1]):
            sorted = False
        i += 1
    return sorted

# Bogosort
def bogo_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array):

    sorted = False

    while not sorted:
        sorted = is_array_sorted(array)
        if not sorted:
            random.shuffle(array)
            if wait_delay:
                draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, array)

# Bubblesort
def bubble_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
                if wait_delay:
                    draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, array)

# Mergesort
def merge_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, is_main):

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, left_arr, False)
        merge_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, right_arr, False)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                if is_main == True and wait_delay:
                    draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)
            else:
                arr[k] = right_arr[j]
                j += 1
                if is_main == True and wait_delay:
                    draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            if is_main == True and wait_delay:
                draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            if is_main == True and wait_delay:
                draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)

# Insertion sort
def insertion_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            if wait_delay:
                draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)

# Quicksort
def quick_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, left, right):
    if left < right:
        partition_pos = partition(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, left, right)
        quick_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, left, partition_pos - 1)
        quick_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, partition_pos + 1, right)

# Used by quicksort function
def partition(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, left, right):
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
                draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        if wait_delay:
            draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)
    return i

# Gnomesort
def gnome_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr):
    i = 0
    while i < len(arr): 
        if i == 0: 
            i += 1
            
        if arr[i] >= arr[i - 1]: 
            i += 1
            draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)

        else: 
            arr[i], arr[i - 1] = arr[i - 1], arr[i] 
            i -= 1
            draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)

# Heapsort
def heap_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, arr):
    N = len(arr)

    for i in range(N//2 - 1, -1, -1):
        heapify(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, N, i)

    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)
        heapify(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, i, 0)

# Needed for heapsort
def heapify(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, arr)

        heapify(reverse, stdscr, array_size, wait_delay, term_height, startx, arr, N, largest)

def main(stdscr):
    # Finds terminal info
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    # Set variables and lists
    array_size = int(sys.argv[1])
    array_range = int(sys.argv[2])

    # If True, instantly sort the array without drawing
    if int(sys.argv[6]) == 0:
        wait_delay = False
    else:
        wait_delay = True

    # Makes the array sort from greatest to least instead of least to greatest
    if int(sys.argv[4]) == 0:
        reverse = False
    else:
        reverse = True

    # Shows info after sorting
    if int(sys.argv[5]) == 0:
        show_info = False
    else:
        show_info = True

    # If True, makes the array size and range the highest possible that can fit on the screen
    fill_screen = int(sys.argv[3])
    
    if fill_screen == 1:
        array_size = int(term_width / 2) - 2
        array_range = term_height - 2
    
    # Fills the array with random integers
    array = []
    for i in range(array_size):
        temp = random.randint(1, array_range)
        array.append(temp)

    # Finds correct position to start drawing
    if reverse:
        startx = math.floor(term_width / 2) + math.floor(array_size)
    else:
        startx = math.floor(term_width / 2) - math.floor(array_size)

    # Curses initialization
    curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.clear()

    # Quits program if terminal height too small for array_range
    if (array_range + 2) > term_height:
        stdscr.addstr(0, 0, "terminal height too small for array range!")
        stdscr.addstr(2, 0, "press any key to exit")
        stdscr.getch()
        curses.endwin()

    # Same if terminal width too small for array_size
    elif (array_size + 2) > term_width:
        stdscr.addstr(0, 0, "terminal width too small for array size!")
        stdscr.addstr(2, 0, "press any key to exit")
        stdscr.getch()
        stdscr.endwin

    # Otherwise, start main script
    else:
        # Draw the array before sorting
        if wait_delay:
            draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, array)

        # Starts performance timer
        start_time = time.perf_counter()

        # Sorting algorithms determined by bash script
        if sys.argv[7] == "bogosort":
            bogo_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array)

        elif sys.argv[7] == "bubblesort":
            bubble_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array)

        elif sys.argv[7] == "mergesort":
            merge_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array, True)

        elif sys.argv[7] == "insertionsort":
            insertion_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array)
            
        elif sys.argv[7] == "quicksort":
            quick_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array, 0, len(array) - 1)
            
        elif sys.argv[7] == "gnomesort":
            gnome_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array)
        
        elif sys.argv[7] == "heapsort":
            heap_sort(reverse, stdscr, array_size, wait_delay, term_height, startx, array)
        
        # Ends performance timer
        end_time = time.perf_counter()

        # Only draw at the end of sorting when wait_delay is on, otherwise it would just show the array being unsorted
        if not wait_delay:
            draw_array(reverse, stdscr, array_size, wait_delay, term_height, startx, array)

        # Finds where to place sort_info text
        if reverse:
            text_x = term_width - 50
        else:
            text_x = 0

        if show_info == True:
            # Shows that array is sorted and other info
            stdscr.addstr(0, text_x, "Array sorted!")
            stdscr.addstr(2, text_x, "Sorting information:")
            stdscr.addstr(4, text_x, "sorting algorithm: " + str(sys.argv[7]))
            stdscr.addstr(5, text_x, "array size: " + str(array_size))
            stdscr.addstr(6, text_x, "array range: " + str(array_range))
            stdscr.addstr(7, text_x, "time taken to sort: " + str(round(end_time - start_time, 3)) + " second(s)")
            stdscr.addstr(8, text_x, "delay: " + str(sys.argv[6]) + " millisecond(s)")
            if reverse:
                stdscr.addstr(9, text_x, "Greatest to least")

            else:
                stdscr.addstr(9, text_x, "Least to greatest")

            stdscr.addstr(11, text_x, "Press any key to exit")
        
        else:
            stdscr.addstr(0, term_width - 25, "Array sorted!")
            stdscr.addstr(1, term_width - 25, "Press any key to exit")
        
        # Waits for key press and stops program
        stdscr.getch()
        curses.endwin()

wrapper(main)

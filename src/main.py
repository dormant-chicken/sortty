import os, sys, curses, time, random, math
from curses import wrapper

def draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, array):

    stdscr.clear()

    # This draws the array onto the screen
    i = 0
    j = 0
    for i in range(len(array)):
        for j in range(array[i]):
            stdscr.addstr(term_height - 1 - j, startx + (i * 2), "#")

    stdscr.refresh()
    if wait_delay:
        time.sleep(int(sys.argv[4]) / 1000)

# Maybe merge this into the bogosort function if it is unused by other functions
def is_array_sorted(array):
    sorted = True
    i = 1
    while i < len(array):
        if(array[i] < array[i - 1]):
            sorted = False
        i += 1
    return sorted

def bogo_sort(stdscr, array_size, wait_delay, term_height, startx, array):

    sorted = False

    while not sorted:
        sorted = is_array_sorted(array)
        if not sorted:
            random.shuffle(array)
            if wait_delay:
                draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, array)

def bubble_sort(stdscr, array_size, wait_delay, term_height, startx, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
                if wait_delay:
                    draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, array)

def merge_sort(stdscr, array_size, wait_delay, term_height, startx, arr, is_main):

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(stdscr, array_size, wait_delay, term_height, startx, left_arr, False)
        merge_sort(stdscr, array_size, wait_delay, term_height, startx, right_arr, False)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                if is_main == True:
                    draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, arr)
            else:
                arr[k] = right_arr[j]
                j += 1
                if is_main == True:
                    draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, arr)
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            if is_main == True:
                draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, arr)
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            if is_main == True:
                draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, arr)

def insertion_sort(stdscr, array_size, wait_delay, term_height, startx, arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, arr)


def main(stdscr):
    # Finds terminal info
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    # Set variables and lists
    array_size = int(sys.argv[1])
    array_range = int(sys.argv[2])

    # If True, instantly sort the array without drawing
    if int(sys.argv[4]) == 0:
        wait_delay = False
    else:
        wait_delay = True

    # If True, makes the array size and range the highest possible that can fit on the screen
    fill_screen = int(sys.argv[3])
    
    if fill_screen == 1:
        array_size = int(term_width / 2) - 1
        array_range = term_height - 2
    
    # Fills the array with random integers
    array = []
    for i in range(array_size):
        temp = random.randint(1, array_range)
        array.append(temp)

    # Draws the shuffled array before sorting
    # Only if specified by wait_delay variable

    # Finds correct position to start drawing
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
            draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, array)

        # Starts performance timer
        start_time = time.perf_counter()

        # Sorting algorithms determined by bash script
        if sys.argv[5] == "bogosort":
            bogo_sort(stdscr, array_size, wait_delay, term_height, startx, array)

        elif sys.argv[5] == "bubblesort":
            bubble_sort(stdscr, array_size, wait_delay, term_height, startx, array)

        elif sys.argv[5] == "mergesort":
            merge_sort(stdscr, array_size, wait_delay, term_height, startx, array, True)

        elif sys.argv[5] == "insertionsort":
            insertion_sort(stdscr, array_size, wait_delay, term_height, startx, array)
        
        # Ends performance timer
        end_time = time.perf_counter()

        # Only draw at the end of sorting when wait_delay is on, otherwise it would just show the array being unsorted
        if not wait_delay:
            draw_array(sorted, stdscr, array_size, wait_delay, term_height, startx, array)
        
        # Shows that array is sorted and other info
        stdscr.addstr(0, 0, "Array sorted!")
        stdscr.addstr(2, 0, "Sorting information:")
        stdscr.addstr(4, 0, "sorting algorithm: " + str(sys.argv[5]))
        stdscr.addstr(5, 0, "array size: " + str(array_size))
        stdscr.addstr(6, 0, "array range: " + str(array_range))
        stdscr.addstr(7, 0, "time taken to sort: " + str(math.floor(end_time - start_time)) + " second(s)")
        stdscr.addstr(9, 0, "Press any key to exit")
        
        # Waits for key press and stops program
        stdscr.getch()
        curses.endwin()

wrapper(main)

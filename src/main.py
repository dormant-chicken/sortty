import os, sys, curses, time, random, math
from curses import wrapper

def draw_array(stdscr, wait_delay, term_height, startx, array):
    stdscr.clear()

    # This draws the array onto the screen
    i = 0
    j = 0
    for i in range(len(array)):
        for j in range(array[i]):
            # Checks if [ reverse ] is True
            match int(sys.argv[4]):
                case 1:
                    # Checks if [ fancy ] is True
                    match int(sys.argv[6]):
                        case 1:
                            stdscr.addstr(term_height - 1 - j, startx - (i * 2), " ", curses.A_REVERSE)
                        case 0:
                            stdscr.addstr(term_height - 1 - j, startx - (i * 2), "#")
                case 0:
                    match int(sys.argv[6]):
                        case 1:
                            stdscr.addstr(term_height - 1 - j, startx + (i * 2), " ", curses.A_REVERSE)
                        case 0:
                            stdscr.addstr(term_height - 1 - j, startx + (i * 2), "#")

    stdscr.refresh()
    if wait_delay:
        time.sleep(int(sys.argv[7]) / 1000)

# Bogosort
def bogo_sort(stdscr, wait_delay, term_height, startx, array):

    sorted = False

    while not sorted:
        sorted = True
        for i in range(1, len(array)):
            if(array[i] < array[i - 1]):
                sorted = False
        if not sorted:
            random.shuffle(array)
            if wait_delay:
                draw_array(stdscr, wait_delay, term_height, startx, array)

# Bubblesort
def bubble_sort(stdscr, wait_delay, term_height, startx, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
                if wait_delay:
                    draw_array(stdscr, wait_delay, term_height, startx, array)

# Mergesort
def merge_sort(stdscr, wait_delay, term_height, startx, arr, is_main):

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(stdscr, wait_delay, term_height, startx, left_arr, False)
        merge_sort(stdscr, wait_delay, term_height, startx, right_arr, False)

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                if is_main == True and wait_delay:
                    draw_array(stdscr, wait_delay, term_height, startx, arr)
            else:
                arr[k] = right_arr[j]
                j += 1
                if is_main == True and wait_delay:
                    draw_array(stdscr, wait_delay, term_height, startx, arr)
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            if is_main == True and wait_delay:
                draw_array(stdscr, wait_delay, term_height, startx, arr)
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            if is_main == True and wait_delay:
                draw_array(stdscr, wait_delay, term_height, startx, arr)

# Insertion sort
def insertion_sort(stdscr, wait_delay, term_height, startx, arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            if wait_delay:
                draw_array(stdscr, wait_delay, term_height, startx, arr)

# Quicksort
def quick_sort(stdscr, wait_delay, term_height, startx, arr, left, right):
    if left < right:
        partition_pos = partition(stdscr, wait_delay, term_height, startx, arr, left, right)
        quick_sort(stdscr, wait_delay, term_height, startx, arr, left, partition_pos - 1)
        quick_sort(stdscr, wait_delay, term_height, startx, arr, partition_pos + 1, right)

# Used by quicksort function
def partition(stdscr, wait_delay, term_height, startx, arr, left, right):
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
                draw_array(stdscr, wait_delay, term_height, startx, arr)
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        if wait_delay:
            draw_array(stdscr, wait_delay, term_height, startx, arr)
    return i

# Gnomesort
def gnome_sort(stdscr, wait_delay, term_height, startx, arr):
    i = 0
    while i < len(arr): 
        if i == 0: 
            i += 1
            
        if arr[i] >= arr[i - 1]: 
            i += 1
            if wait_delay:
                draw_array(stdscr, wait_delay, term_height, startx, arr)

        else: 
            arr[i], arr[i - 1] = arr[i - 1], arr[i] 
            i -= 1
            if wait_delay:
                draw_array(stdscr, wait_delay, term_height, startx, arr)

# Heapsort
def heap_sort(stdscr, wait_delay, term_height, startx, arr):
    N = len(arr)

    for i in range(N//2 - 1, -1, -1):
        heapify(stdscr, wait_delay, term_height, startx, arr, N, i)

    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        if wait_delay:
            draw_array(stdscr, wait_delay, term_height, startx, arr)

        heapify(stdscr, wait_delay, term_height, startx, arr, i, 0)

# Needed for heapsort
def heapify(stdscr, wait_delay, term_height, startx, arr, N, i):
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
            draw_array(stdscr, wait_delay, term_height, startx, arr)

        heapify(stdscr, wait_delay, term_height, startx, arr, N, largest)

# Cocktailsort
def cocktail_sort(stdscr, wait_delay, term_height, startx, array):
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
                    draw_array(stdscr, wait_delay, term_height, startx, array)

        if (swapped == False):
            break

        swapped = False

        end -= 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                if wait_delay:
                    draw_array(stdscr, wait_delay, term_height, startx, array)

        start += 1

# Selectionsort
def selection_sort(stdscr, wait_delay, term_height, startx, array):
    for i in range(len(array)):
        min_idx = i

        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
        if wait_delay:
            draw_array(stdscr, wait_delay, term_height, startx, array)

# Shellsort
def shellSort(stdscr, wait_delay, term_height, startx, array):
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
                        draw_array(stdscr, wait_delay, term_height, startx, array)
                
                # Move gap to sort
                i = i - gap

            j += 1

        # Cuts gap size in half
        gap = int(gap / 2)

def oddeven_sort(stdscr, wait_delay, term_height, startx, array):
    sorted = False

    while sorted == False:
        sorted = True

        for i in range(1, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # Swap
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                if wait_delay:
                    draw_array(stdscr, wait_delay, term_height, startx, array)
                
        for i in range(0, len(array) - 1, 2):
            if array[i] > array[i + 1]:
                # Swap
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
                if wait_delay:
                    draw_array(stdscr, wait_delay, term_height, startx, array)

def give_term_error(stdscr, term_required, term_current, message):
    stdscr.addstr(0, 0, str(message))
    stdscr.addstr(2, 0, "required height: " + str(term_required) + " cells")
    stdscr.addstr(3, 0, "terminal height: " + str(term_current) + " cells")
    stdscr.addstr(5, 0, "please resize your terminal and try again")
    stdscr.addstr(7, 0, "press any key to exit")
    stdscr.getch()
    curses.endwin()

def main(stdscr):
    # Finds terminal info
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    # Set variables and lists
    array_size = int(sys.argv[1])
    array_range = int(sys.argv[2])

    # If True, instantly sort the array without drawing
    if int(sys.argv[7]) == 0:
        wait_delay = False
    else:
        wait_delay = True

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
    if int(sys.argv[4]) == 0:
        startx = math.floor(term_width / 2) - math.floor(array_size)
    else:
        startx = math.floor(term_width / 2) + math.floor(array_size)

    # Curses initialization
    curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.clear()

    # Quits program if terminal height too small for array_range
    # This does not acount for array range if fill_screen is True
    if term_height < 20:
        give_term_error(stdscr, 20, term_height, "terminal height less than minimum!")

    elif term_width < 80:
        give_term_error(stdscr, 100, term_width, "terminal width less than minimum!")

    elif fill_screen == False and (array_range >= term_height):
        give_term_error(stdscr, array_range, term_height, "terminal height too small for array range!")

    elif (fill_screen == False and array_size > term_width):
        give_term_error(stdscr, array_size, term_width, "terminal width too small for array size!")
    
    # Otherwise, start main script
    else:
        # Draw the array before sorting
        if wait_delay:
            draw_array(stdscr, wait_delay, term_height, startx, array)

        # Starts performance timer
        start_time = time.perf_counter()

        # Sorting algorithms determined by bash script
        match sys.argv[8]:
            case "bogosort":
                bogo_sort(stdscr, wait_delay, term_height, startx, array)

            case "bubblesort":
                bubble_sort(stdscr, wait_delay, term_height, startx, array)

            case "mergesort":
                merge_sort(stdscr, wait_delay, term_height, startx, array, True)

            case "insertionsort":
                insertion_sort(stdscr, wait_delay, term_height, startx, array)

            case "quicksort":
                quick_sort(stdscr, wait_delay, term_height, startx, array, 0, len(array) - 1)

            case "gnomesort":
                gnome_sort(stdscr, wait_delay, term_height, startx, array)
                
            case "heapsort":
                heap_sort(stdscr, wait_delay, term_height, startx, array)

            case "cocktailsort":
                cocktail_sort(stdscr, wait_delay, term_height, startx, array)

            case "selectionsort":
                selection_sort(stdscr, wait_delay, term_height, startx, array)

            case "shellsort":
                shellSort(stdscr, wait_delay, term_height, startx, array)

            case "oddevensort":
                oddeven_sort(stdscr, wait_delay, term_height, startx, array)
        
        # Ends performance timer
        end_time = time.perf_counter()

        # Only draw at the end of sorting when wait_delay is on, otherwise it would just show the array being unsorted
        if not wait_delay:
            draw_array(stdscr, wait_delay, term_height, startx, array)

        # Finds where to place sort_info text
        match int(sys.argv[4]):
            case 1:
                text_x = term_width - 50
            case 0:
                text_x = 0

        if show_info == True:
            # Shows that array is sorted and other info
            stdscr.addstr(0, text_x, "Array sorted!")
            stdscr.addstr(2, text_x, "Sorting information:")
            stdscr.addstr(4, text_x, "sorting algorithm: " + str(sys.argv[8]))
            stdscr.addstr(5, text_x, "array size: " + str(array_size))
            stdscr.addstr(6, text_x, "array range: " + str(array_range))
            stdscr.addstr(7, text_x, "time taken to sort: " + str(round(end_time - start_time, 3)) + " second(s)")
            stdscr.addstr(8, text_x, "delay: " + str(sys.argv[7]) + " millisecond(s)")
            
            match int(sys.argv[4]):
                case 1:
                    stdscr.addstr(9, text_x, "sorted greatest to least")
                case 0:
                    stdscr.addstr(9, text_x, "sorted least to greatest")

            stdscr.addstr(11, text_x, "Press any key to exit")
        
        else:
            stdscr.addstr(0, term_width - 25, "Array sorted!")
            stdscr.addstr(1, term_width - 25, "Press any key to exit")
        
        # Waits for key press and stops program
        stdscr.getch()
        curses.endwin()

wrapper(main)

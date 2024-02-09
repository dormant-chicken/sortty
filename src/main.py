import os, sys, curses, time, random, math
from curses import wrapper

def draw_array(sorted, stdscr, array_size, show_delay, array):
    import math
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    stdscr.clear()

    # If True, show array into and if it sorted
    debug = False

    startx = math.floor(term_width / 2) - math.floor(array_size)

    i = 0
    j = 0
    for i in range(len(array)):
        for j in range(array[i]):
            stdscr.addstr(term_height - 1 - j, startx + (i * 2), "#")

    if debug:
        stdscr.addstr(0, 0, str(array))
        stdscr.addstr(1, 0, str(sorted))

    stdscr.refresh()
    if show_delay:
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

def bogo_sort(stdscr, array_size, show_delay, array):
    sorted = False
    while not sorted:
        sorted = is_array_sorted(array)
        if not sorted:
            random.shuffle(array)
            if show_delay:
                draw_array(sorted, stdscr, array_size, show_delay, array)

def bubble_sort(stdscr, array_size, show_delay, array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
                if show_delay:
                    draw_array(sorted, stdscr, array_size, show_delay, array)

def main(stdscr):
    # Finds terminal info
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    # Curses initialization
    curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.clear()

    # Set variables and lists
    array_size = int(sys.argv[1])
    array_range = int(sys.argv[2])

    # If True, instantly sort the array without drawing
    show_delay = True

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

    # Draws the shuffled array before sorting
    # Only if specified by show_delay variable
    if show_delay:
        draw_array(sorted, stdscr, array_size, show_delay, array)

    if sys.argv[5] == "bogosort":
        bogo_sort(stdscr, array_size, show_delay, array)

    elif sys.argv[5] == "bubblesort":
        bubble_sort(stdscr, array_size, show_delay, array)

    # If show_delay is True, redraw after sorting
    if not show_delay:
        draw_array(sorted, stdscr, array_size, show_delay, array)
    
    stdscr.addstr(0, 0, "Array sorted!")
    
    # Waits for key press and stops program
    stdscr.getch()
    curses.endwin()

wrapper(main)

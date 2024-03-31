# sortty
sortty - A lightweight, minimal, and beautiful program to visualize sorting algorithms in your Unix terminal / TTY, written in python and ncurses

## Gallery

![quicksort3](https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort3.png)
![quicksort2](https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort2.png)
![heapsort1](https://github.com/dormant-chicken/sortty/blob/main/assets/heapsort1.png)

<br>

## Table of contents

* [Features](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#features)

* [Dependencies](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#dependencies)

* [Installation](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#installation)

    * [Latest git](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#latest-git)

    * [Stable release](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#stable-release)

* [Last step of install](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#last-step-of-install)

* [Trying sortty without installing](https://github.com/dormant-chicken/sortty/tree/main?tab=readme-ov-file#trying-sortty-without-installing)

* [Usage](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#usage)

* [Uninstalling](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#uninstalling)

* [The name](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#the-name)

<br>

## Features

- Draws every step of a specified sorting algorithm quickly using ncurses
- Currently has 14 built-in sorting algorithms (specified in the [usage](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#usage) tab of the README)
- Detects if terminal is too small for the specified array_size / array_range
- animation before shuffling array
- animation during shuffling of array
- red bar to indicate index when sorting array
- animation that fills the array green after shuffling array
- #### Options to:
- change array size
- change array range
- fill the entire terminal / TTY with the array or not
- change the delay (how fast or slow the algorithm sorts the array)
- change what algorithm to use
- change size of bars (increasing this can improve performance)

<br>

## Flashing Light Warning

> [!WARNING]
> There may be flashing on the screen if fancy bars are used instead of a text-based character, if the terminal text is small, if the bar size is small, or if your GPU is low-end. This can be fixed by lowering the size of your terminal, increasing the size of the bars, increasing terminal font size, or increasing the wait delay for the program.

## Dependencies

These dependencies are needed:

`python ncurses git figlet`

<br>

They are most likely preinstalled, but it is still good to check.

<br>

Arch:
```
sudo pacman -S python ncurses git figlet
```

Fedora:
```
sudo dnf install python ncurses ncurses-devel git figlet
```

Debian:
```
sudo apt install python3 libncurses5 libncurses6 libncurses-dev git figlet
```

<br>

## Installation

### Latest git

After installing the needed dependencies, clone this repository to get the very latest git release:

```
git clone https://github.com/dormant-chicken/sortty
```

<br>

### Stable release

<br>

> [!WARNING]
> I recommend using the newest stable release, as the older ones might have a few small bugs

<br>

If you want the stable release, install the dependencies above and use wget to get the tar.gz file from the releases page:

```
wget https://github.com/dormant-chicken/sortty/releases/download/v1.7/sortty.tar.gz
```

<br>

Or you can also get it with a web browser from the [releases page](https://github.com/dormant-chicken/sortty/releases)

<br>

Then, you can decompress the tar.gz file by typing:

```
tar -xzvf sortty.tar.gz
```

<br>

You can remove the tar.gz file if you want to:

```
rm sortty.tar.gz
```

<br>

## Last step of install

Finally, change your directory into sortty/, make install.sh executable, and run install.sh:

```
cd sortty/
chmod +x install.sh
./install.sh
```

<br>

After installing, you can remove the sortty/ directory, as the needed files are already copied to the correct paths:

```
cd ..
rm -r -f sortty/
```

The command above also changes your directory to the parent directory of sortty/ with 'cd ..', which is the directory that it is located in, so that it can remove the directory

<br>

## Trying sortty without installing

If you just want to try sortty without installing, the script has support for that

Just get the files by using git to clone this repostory (shown in the [latest git](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#latest-git) tab) or get the latest stable release and decompress it (shown in the [stable release](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#stable-release) tab). Then, run this command to go into the sortty/src/ directory that you just got:

```
cd sortty/
chmod +x src/sortty.sh
src/sortty.sh
```

<br>

After trying sortty, you can still install it (shown in the [last step of install](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#last-step-of-install) tab) without problems

<br>

## Usage

<br>

`sortty [fancy] [bar_size] [wait_time(ms)] [algorithm] [array_size(optional)] [array_range(optional)]`

Example command:

```
sortty 0 3 100 bubble
```

In the example command above,

[fancy] is 0 (AKA False), so the program will use a '#' character and a '@' character for highlight instead of a fancy bar with colors for highlight

[bar_size] is 3, so the program will draw the bars with a width of 3 terminal cells

[wait_time] is 100, meaning the program will wait 100ms before drawing again

[algorithm] uses the bubblesort algorithm, but available algorithms are: bogo bubble merge insertion quick gnome heap cocktail selection shell oddeven comb bingo radix

If you want a custom array size and array range, you can do so like this:

```
sortty 0 3 100 bubble 30 20
```

After you specify the algorithm, put down the array size you want then the array range you want

[array_size] is 30, meaning it will give the program 30 items to sort

[array_range] is 20, meaning the array that the program sorts ranges from values 1 to 20

[ wait_time ] waits 0.01 seconds before refreshing the screen.

<br>

> [!NOTE]
> I had trouble getting the mergesort algorithm to be drawn properly, because the mergesort function uses multiple arrays. The algorithm still works, and it is still drawn, but the items in the array do not get merged, as seen [here](https://www.youtube.com/watch?v=ZRPoEKHXTJg).

> [!WARNING]
> I do not recommend running an inefficient sorting algorithm, especially bogosort with a delay of 0, I ran it and it made my cpu go to the highest clock speed :\

<br>

## Uninstalling

Run this command to remove the sortty binaries:

```
sudo rm -rf -r /usr/local/bin/sortty-bin/ /usr/local/bin/sortty
```

<br>

## The Name

The name is the word "sort", because this is a program to visualize sorting algorithms, plus the word "TTY", which is similar to a terminal. "sort" plus "TTY" equals "sortty", it's a great name, I know.

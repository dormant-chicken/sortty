# sortty

sortty - sorting algorithms in the terminal

## Gallery

![quicksort3](https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort3.png)
![quicksort2](https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort2.png)
![heapsort1](https://github.com/dormant-chicken/sortty/blob/main/assets/heapsort1.png)

<br>

## Table of contents

* [Features](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#features)

* [AUR](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#aur)

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
- Currently has 16 built-in sorting algorithms (specified in the [usage](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#usage) tab of the README)
- Detects if terminal is too small for the specified array size / array range
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
- use fancy bars (shown in the gallery)
- sort arrays forever with random algorithms

<br>

## Flashing Light Warning

> [!WARNING]
> There may be flashing on the screen if fancy bars are used instead of a text-based character, if the terminal text is small, if the bar size is small, or if your computer is low-end. This can be fixed by lowering the size of your terminal, increasing the size of the bars, increasing terminal font size, or increasing the wait delay for the program, but the best solution I found is to use a lightweight terminal such as [st](https://wiki.archlinux.org/title/st) or [foot](https://wiki.archlinux.org/title/Foot)

<br>

## AUR

If you don't want to install sortty manually, sortty is available on the AUR [here](https://aur.archlinux.org/packages/sortty)

<br>

## Dependencies

These dependencies are needed:

`python ncurses git figlet`

These pip dependencies are also needed:

`argparse art`

<br>

Some of the package dependencies are most likely preinstalled, but it is still good to check.

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

You can install the pip dependencies with

```
pip install argparse art
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
wget https://github.com/dormant-chicken/sortty/releases/download/v1.8/sortty.tar.gz
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
python3 src/sortty.py
```

<br>

After trying sortty, you can still install it (shown in the [last step of install](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#last-step-of-install) tab) without any problems

<br>

## Usage

<br>

`sortty [--fancy or -f] [--bar_size or -b] [--wait_time or -w (ms)] [--algorithm or -a] [--size or -s] [--range or -r] [--no-fill or -nf]`

Example command:

```
sortty
```

Since only the name of the program is run, and there are no arguments, these are the defaults:

[--fancy or -f] is not used by default, meaning the program will use a '#' character for the bars instead of a fancy bar

[--bar_size or -b] is 2, meaning the program will display the bars with a width of 2 terminal characters

[--wait_time or -w] is 75, meaning the program wlll wait 75ms before refreshing the screen

[--algorithm or -a] is quick, meaning the program will use the quicksort algorithm to sort the array

[--size or -s] of array is 30, meaning the array will have 30 elements

[--range or -r] of array is 20, meaning the maximum value of the array will be 20

[--no-fill or -nf] is not used by default, so the array will not fill the screen and ignore the array size and range given

Available algorithms: bogo bubble merge insertion quick gnome heap cocktail selection shell oddeven comb bingo radix pigeonhole pancake

If you want custom options different from the default ones, do so like this:

```
sortty --algorithm insertion --fancy
```

The command above runs sortty with the insertion sort algorithm and sets fancy bars to 1 (true)

More options are available above in the usage part

Note: you can set the algorithm to 'forever' like this:

```
sortty --algorithm forever
```

Setting it to forever makes the program shuffles the array sorts the array with a random algorithm forever (excluding bogo sort)


<br>

> [!NOTE]
> I had trouble getting the mergesort algorithm to be drawn properly, because the mergesort function uses multiple arrays. The algorithm still works, and it is still drawn, but the items in the array do not get merged, as seen [here](https://www.youtube.com/watch?v=ZRPoEKHXTJg).

> [!WARNING]
> I do not recommend running an inefficient sorting algorithm, especially bogosort with a delay of 0, I ran it and it made my cpu go to the highest clock speed

<br>

## Uninstalling

Run this command to remove the sortty binaries:

```
sudo rm -rf -r /usr/local/bin/sortty-bin/ /usr/local/bin/sortty
```

Also, edit your ~/.bashrc file to remove these lines:

```
alias sortty='python3 /usr/local/bin/sortty-bin/sortty.py'
```

<br>

## The Name

The name is the word "sort", because this is a program to visualize sorting algorithms, plus the word "TTY", which is similar to a terminal. "sort" plus "TTY" equals "sortty", it's a great name, I know.

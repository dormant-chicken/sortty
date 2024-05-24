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
- Currently has 17 built-in sorting algorithms (specified in the [usage](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#usage) tab of the README)
- Auto-adjusts if terminal is resized
- Detects if terminal is too small for the specified array size / array range
- Animation before shuffling array
- Animation during shuffling of array
- Shows index when sorting array
- Animation that fills the array green after shuffling array
- #### Options to:
- Change array heigth and width
- Fill the entire terminal / TTY with the array or not
- Change the delay (how fast or slow the algorithm sorts the array)
- Change what algorithm to use
- Change size of bars (increasing this can improve performance)
- Use fancy bars or text-only mode (shown in the gallery)
- Sort arrays forever with random algorithms

<br>

## Flashing Light Warning

> [!WARNING]
> There may be flashing on the screen if text-only mode is not used, if the terminal text is small, or if the bar size is small. This can be fixed by lowering the size of your terminal, increasing the size of the bars, increasing terminal font size, or increasing the wait delay for the program, but the best solution I found is to use a lightweight terminal such as [st](https://wiki.archlinux.org/title/st) if you use Xorg or [foot](https://wiki.archlinux.org/title/Foot) if you use Wayland

<br>

## AUR

If you don't want to install sortty manually, sortty is available on the AUR [here](https://aur.archlinux.org/packages/sortty)

<br>

## Dependencies

These dependencies are needed:

`python ncurses git`

These pip dependencies are also needed:

`art`

<br>

Some of the package dependencies are most likely preinstalled, but it is still good to check.

Arch:
```
sudo pacman -S python ncurses git
```

Fedora:
```
sudo dnf install python ncurses ncurses-devel git
```

Debian:
```
sudo apt install python3 libncurses5 libncurses6 libncurses-dev git
```

You can install the pip dependencies with

```
pip install art
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
wget https://github.com/dormant-chicken/sortty/releases/download/v1.9/sortty.tar.gz
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
rm -rvf sortty/
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

`sortty.py [-h] [-f] [-i] [-nf] [-ni] [-b BAR_SIZE] [-w WAIT_TIME] [-a ALGORITHM] [-s HEIGHTxWIDTH] [-v]`

Example command:

```
sortty
```

Since only the name of the program is run, and there are no arguments, these are the defaults:

[-t --text] add this to make the program use text-only mode instead of using fancy bars

[-i --info] is off, meaning it will not show the sorting information after sorting

[-nf --no_fill] is off, meaning it will not fill the array after sorting

[-ni --no_index] when used, does not show the index as a red bar if (or as a '@' character if --text is enabled) when sorting

[--bar_size or -b] is 1, meaning the program will display the bars with a width of 1 terminal characters

[--wait_time or -w] is 75, meaning the program wlll wait 75ms before refreshing the screen

[--algorithm or -a] is quick, meaning the program will use the quicksort algorithm to sort the array

[--size or -s] if not specified, size will be depending from the screen size, otherwise you can do HEIGTHxWIDTH, for example 30x20

Available algorithms: bogo bubble merge insertion quick gnome heap cocktail selection shell oddeven comb bingo radix pigeonhole pancake bead

If you want custom options different from the default ones, do so like this example:

```
sortty --algorithm insertion --text
```

The command above runs sortty with the insertion sort algorithm and sets text-only mode to true

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
rm ~/.local/bin/sortty
```

Also, remove this line from your shell rc file (~/.basrc if you use bash or ~/.zshrc if you use zsh):

```
export PATH=\$PATH:\$HOME/.local/bin
```

<br>

## The Name

The name is the word "sort", because this is a program to visualize sorting algorithms, plus the word "TTY", which is similar to a terminal. "sort" plus "TTY" equals "sortty", it's a great name, I know.

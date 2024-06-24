# sortty

sortty - sorting algorithms in the terminal

## Gallery

![quicksort3](https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort3.png)

<img src="https://github.com/dormant-chicken/sortty/blob/main/assets/heapsort1.png" width=49%> <img src="https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort2.png" width=49%>

![quicksort3](https://github.com/dormant-chicken/sortty/blob/main/assets/quicksort4.png)

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
- Currently has 21 built-in sorting algorithms (specified in the [usage](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#usage) tab of the README)
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
wget https://github.com/dormant-chicken/sortty/releases/latest/download/sortty.tar.gz
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

This command also changes your directory to the parent directory of sortty/ with 'cd ..' so that it can remove the installed files

<br>

## Trying sortty without installing

If you just want to try sortty without installing, the program has support for that

Just get the files by using git to clone this repostory (shown in the [latest git](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#latest-git) tab) or get the latest stable release and decompress it (shown in the [stable release](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#stable-release) tab). Then, run this command to go into the sortty directory and make the program executable:

```
cd sortty/
chmod +x src/sortty.py
```

Then, run this to execute the program:

```
src/sortty.py
```

<br>

After trying sortty, you can still install it (shown in the [last step of install](https://github.com/dormant-chicken/sortty?tab=readme-ov-file#last-step-of-install) tab) without any problems

<br>

## Usage

<br>

Example command:

```
sortty
```

Use these arguments to change how the program behaves:

```
[-h --help] shows help message

[-t --text] add this to make the program use text-only mode instead of using fancy bars

[-i --info] is off, meaning it will not show the sorting information after sorting

[-nf --no_fill] is off, meaning it will not fill the array after sorting

[-ni --no_index] when used, does not show the index as a red bar if (or as a '@' character if --text is enabled) when sorting

[-na --no_animation] when used, does not show fill and shuffle animation before sorting

[-b --bar_size] is 1, meaning the program will display the bars with a width of 1 terminal characters

[-d --delay] is 75, meaning the program wlll wait 75ms before refreshing the screen

[-a --algorithm] is quick, meaning the program will use the quicksort algorithm to sort the array

[-bc --bar_color] changes color of bars when sorting, does nothing if --text is used

[-ic --index_color] changes color of index pointer when sorting, does nothing if --text is used

[-fc --fill_color] changes color that fills the array after sorting, does nothing if --text is used

[-bch --bar_character] changes character for the bars when sorting, does nothing if --text is not used

[-ich --index_character] changes character for the index pointer when sorting, does nothing if --text is not used

[-fch --fill_character] changes character that fills the array after sorting, does nothing if --text is not used

[-s --size] if not specified, size will be depending from the screen size, otherwise you can do HEIGTHxWIDTH, for example 30x20

[-v --version] print version and quit
```

Available algorithms: bogo bubble merge insertion quick gnome heap cocktail selection shell oddeven comb bingo radix pigeonhole pancake bead stooge inplace_merge tim circle

Available colors for bars: red green blue cyan magenta yellow white transparent

Here is another example command, but with arguments:

```
sortty --algorithm insertion --text --bar_character o
```

The command above runs sortty with the insertion sort algorithm, sets text-only mode to true, and makes the program use an 'o' character instead of the default '#' character for the bars

Note: you can set the algorithm to 'forever' like this:

```
sortty --algorithm forever
```

Setting it to forever makes the program shuffle the array and sort the array forever, with a different random algorithm every time (excluding bogo sort)

<br>

## Uninstalling

Run this command to remove the sortty binaries:

```
rm ~/.local/bin/sortty
```

Optionally, you can also remove this line from your shell rc file (located in '\~/.basrc' if you use bash or '\~/.zshrc' if you use zsh):

```
export PATH=$PATH:$HOME/.local/bin
```

<br>

## The Name

The name is the word "sort", because this is a program to visualize sorting algorithms, plus the word "TTY", which is similar to a terminal. "sort" plus "TTY" equals "sortty", it's a great name, I know.

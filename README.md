# sorTTY
sorTTY - A lightweight program to visualize sorting algorithms in your unix terminal / TTY, written in python and ncurses

<br>

## Table of contents

* [Features](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#features)

* [Dependencies](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#dependencies)

* [Installation](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#installation)

    * [Latest git](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#latest-git)

    * [Stable release](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#stable-release)

* [Last step of install](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#last-step-of-install)

* [Usage](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#usage)

* [Uninstalling](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#uninstalling)

* [The name](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#the-name)

<br>

## Features

- Draws every step of a specified sorting algorithm quickly using ncurses
- Currently has 10 built-in sorting algorithms (specified in the [usage](https://github.com/dormant-chicken/sorTTY?tab=readme-ov-file#usage) tab of the README)
- Detects if terminal is too small for the specified array_size / array_range
- #### Options to:
- change array size
- change array range
- fill the entire terminal / TTY with the array or not
- sort from greatest to least or least to greatest
- show or not to show sorting information (like the array size chosen, the array range chosen, the time taken to sort, the delay chosen, and if it was sorted greatest to least or least to greatest)
- change the delay (how fast or slow the algorithm sorts the array)
- change what algorithm to use

<br>

![quicksort1](https://github.com/dormant-chicken/sorTTY/blob/main/assets/quicksort1.png)
![sortty-help](https://github.com/dormant-chicken/sorTTY/blob/main/assets/sortty-help.png)
![mergesort2](https://github.com/dormant-chicken/sorTTY/blob/main/assets/mergesort2.png)

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
sudo dnf install python ncurses git figlet
```

Debian:
```
sudo apt install python3 libncurses5 git figlet
```

<br>

## Installation

### Latest git

After installing the needed dependencies, clone this repository to get the very latest git release:

```
git clone https://github.com/dormant-chicken/sorTTY
```

<br>

### Stable release

If you want the stable release, install the dependencies above and use wget to get the tar.gz file from the releases page:

```
wget https://github.com/dormant-chicken/sorTTY/releases/download/v1.0-stable/sorTTY.tar.gz
```

<br>

Or you can also get it with a web browser from the [releases page](https://github.com/dormant-chicken/sorTTY/releases)

<br>

Then, you can decompress the tar.gz file by typing:

```
tar -xzvf sorTTY.tar.gz
```

<br>

You can remove the tar.gz file if you want to:

```
rm sorTTY.tar.gz
```

<br>

## Last step of install

Finally, change your directory into sorTTY/, make install.sh executable, and run install.sh:

```
cd sorTTY/
chmod +x install.sh
./install.sh
```

<br>

After installing, you can remove the sorTTY/ directory, as the needed files are already copied to the correct paths:

```
cd ..
rm -r -f sorTTY/
```

The command above also changes your directory to the parent directory of sorTTY/ with 'cd ..', which is the directory that it is located in, so that it can remove the directory

<br>

## Usage

`sortty [ array_size (integer) ] [ array_range (integer) ] [ fill (boolean integer (0 or 1)) ] [ reversed (boolean integer) ] [ show_info (boolean integer) ] [ wait_time (milliseconds) (integer) ] [ algorithm (string) ]`

Example command:

```
sortty 15 10 0 0 1 100 bubblesort
```

In the example command above,

[ array_size ] is 15, meaning it will give the program 15 items to sort.

[ array_range ] is 10, meaning the array that the program sorts ranges from values 0 to 10.

[ fill ] is 0 (AKA False), meaning that the program will not ignore the values above and use the highest possible array size and array range, limited by the size of the screen.

[ reversed ] is 0 (AKA False), so the program will not sort from greatest to least, but least to greatest.

[ show_info ] is 1 (AKA True), so the program will show the sorting information after sorting

[ wait_time ] waits 0.01 seconds before refreshing the screen.

[ algorithm ] uses the bubblesort algorithm, but available algorithms are: bogosort, bubblesort, mergesort, insertionsort, quicksort, gnomesort, heapsort, cocktailsort, selectionsort, shellsort, and oddevensort, making 10 available algorithms to chose from

<br>

> [!NOTE]
> If [ fill ] is 1 (AKA True), the program will ignore [ array_size ] and [ array_range ], as it makes the program use the screen dimensions for [ array_size ] and [ array_range ] instead.

> [!NOTE]
> I had trouble getting the mergesort algorithm to be drawn properly, because the mergesort function uses multiple arrays. The algorithm still works, and it is still drawn, but the items in the array do not get merged, as seen [here](https://www.youtube.com/watch?v=ZRPoEKHXTJg).

> [!WARNING]
> I do not recommend running an inefficient sorting algorithm, especially bogosort with a delay of 0, I ran it and it made my cpu go to the highest clock speed

<br>

## Uninstalling

Run this command to remove the sorTTY binaries:

```
sudo rm -rf -r /usr/local/bin/sortty-bin/ /usr/local/bin/sortty
```

<br>

## The Name

The name is the word "sort", because this is a program to visualize sorting algorithms, plus the word "TTY", which is similar to a terminal. "sort" plus "TTY" equals "sorTTY", it's a great name, I know.

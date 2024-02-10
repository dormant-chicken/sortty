# sorTTY
sorTTY - A program to visualize sorting algorithms in your terminal / TTY, written in python and ncurses

<br>

![mergesort1](https://github.com/dormant-chicken/sorTTY/blob/main/assets/mergesort1.png)
![bogosort1](https://github.com/dormant-chicken/sorTTY/blob/main/assets/bogosort1.png)
![mergesort2](https://github.com/dormant-chicken/sorTTY/blob/main/assets/mergesort2.png)

## Dependencies

These dependencies are needed:

`python`

`ncurses`

`git`

<br>

Arch:
```
sudo pacman -S python ncurses git
```

Fedora:
```
sudo dnf install python ncurses git
```

Debian:
```
sudo apt install python3 libncurses5 git
```

<br>

## Installation

After installing the needed dependencies, clone this repository:

```
git clone https://github.com/dormant-chicken/sorTTY
cd sorTTY/
chmod +x install.sh
```

The command above also makes the install script executable

<br>

Finally, to install the program, type this command to run the install script:

```
./install.sh
```

<br>

> [!NOTE]
> After installing, you can remove the sorTTY/ directory, as the needed files are already copied to the correct paths

<br>

## Usage

`sortty [ array_size ] [ array_range] [ fill ] [ wait_time (milliseconds) ] [ algorithm ]`

Enter the value types as follows:

`sortty [ integer ] [ integer ] [ boolean integer (0 or 1) ] [ integer ] [ string ]`

Example command:

```
sortty 15 10 0 100 bubblesort
```

In the example command above,

[ array_size ] is 15, meaning it will give the program 15 items to sort.

[ array_range ] is 10, meaning the array that the program sorts ranges from values 0 to 10.

[ fill ] is 0 (AKA False), meaning that the program will not ignore the values above and use the highest possible array size and array range, limited by the size of the screen.

[ wait_time ] waits 0.01 seconds before refreshing the screen.

[ algorithm ] uses the bubblesort algorithm, but available algorithms are: bogosort, bubblesort

> [!NOTE]
> If [ fill ] is 1 (AKA True), the program will ignore [ array_size ] and [ array_range ], as it makes the program use the screen dimensions for [ array_size ] and [ array_range ] instead.

> [!WARNING]
> I had trouble getting the mergesort algorithm to be drawn properly, because the mergesort function uses multiple arrays. The algorithm still works, and it is still drawn, but the items in the array do not get merged, as seen [here](https://www.youtube.com/watch?v=ZRPoEKHXTJg).

<br>

## Uninstalling

Run this command to remove the sorTTY binaries:

```
sudo rm -rf -r /usr/local/bin/sortty-bin/ /usr/local/bin/sortty
```

<br>

## The Name

The name is the word "sort", because this is a program to visualize sorting algorithms, plus the word "TTY", which is similar to a terminal. "sort" plus "TTY" equals "sorTTY"

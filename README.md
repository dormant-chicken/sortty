# sorTTY
sorTTY - A program to visualize sorting algorithms in your terminal / TTY, written in python and ncurses

<br>

![bubblesort1](https://github.com/dormant-chicken/sorTTY/blob/main/assets/bubblesort1.png)
![bogosort1](https://github.com/dormant-chicken/sorTTY/blob/main/assets/bogosort1.png)
![sortty](https://github.com/dormant-chicken/sorTTY/blob/main/assets/sortty.png)

## Dependencies

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

After installing dependencies, clone this repository:
```
git clone https://github.com/dormant-chicken/sorTTY
cd sorTTY/
chmod +x install.sh
```

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

[ algorithm ] uses the bubblesort algorithm, but availible algorithms are: bogosort, bubblesort

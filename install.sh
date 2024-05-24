#!/bin/bash
set -e

# ask yes or no function
function yes_or_no {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0
            ;;
            [Nn]*) return 1
            ;;
        esac
    done
}

echo "Creating ~/.local/bin/"
mkdir -p ~/.local/bin

echo "Copying sortty.py from src into ~/.local/bin"
# note it has no extention (so that you can call it by typing 'sortty')
cp src/sortty.py ~/.local/bin/sortty
chmod +x ~/.local/bin/sortty
echo

# ask if you want to add directory to PATH
if yes_or_no "Add ~/.local/bin to PATH?"; then
    if [ "$SHELL" == "/bin/bash" ] || [ "$SHELL" == "/usr/bin/bash" ]; then
        echo
        echo "Appending 'export PATH=\$PATH:\$HOME/.local/bin' to ~/.bashrc so that sortty can be run directly from the terminal"
        echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.bashrc
        echo "reopen your terminal so that you can run sortty directly from your terminal"

    elif [ "$SHELL" == "/bin/zsh" ] || [ "$SHELL" == "/usr/bin/zsh" ]; then
        echo
        echo "Appending 'export PATH=\$PATH:\$HOME/.local/bin' to ~/.zshrc so that sortty can be run directly from the terminal"
        echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.zshrc
        echo "reopen your terminal so that you can run sortty directly from your terminal"

    else
        echo "Unrecognized shell (only bash and zsh are supported)"
    fi
fi

echo
echo "Done!"
echo "Run 'sortty --help' for instructions"
echo
echo "Have fun using sortty!"

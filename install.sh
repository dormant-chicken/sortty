#!/bin/bash
set -e

function yes_or_no { # ask yes or no function
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) return  1 ;;
        esac
    done
}

echo "Creating ~/.local/bin/"
mkdir -p ~/.local/bin

# echo "You might have to enter your root password"
#not anymore, all installed for the current user
# echo

echo "Copying sortty.py from src into ~/.local/bin"
cp src/sortty.py ~/.local/bin/sortty #note it has no extention (so that you can call it by typing 'sortty')
chmod +x ~/.local/bin/sortty

# echo
# echo

#ask if you want to add directory to PATH
if yes_or_no "Add ~/.local/bin to PATH?"; then
    if [ "$SHELL" == "/bin/bash" ] || [ "$SHELL" == "/usr/bin/bash" ]; then
        echo "Appending 'export PATH=\$PATH:\$HOME/.local/bin' to ~/.bashrc so that sortty can be run directly from the terminal"
        echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.bashrc
        echo "Done, reopen your terminal so that you can run sortty directly from your terminal"

    elif [ "$SHELL" == "/bin/zsh" ] || [ "$SHELL" == "/usr/bin/zsh" ]; then
        echo "Appending 'export PATH=\$PATH:\$HOME/.local/bin' to ~/.zshrc so that sortty can be run directly from the terminal"
        echo "export PATH=\$PATH:\$HOME/.local/bin" >> ~/.zshrc
        echo "Done, reopen your terminal so that you can run sortty directly from your terminal"

    else
        echo "Unrecognized shell (only bash and zsh are supported)"
    fi
fi
echo "Done!"
echo "Run 'sortty --help' for instructions"
echo
echo "Have fun using sortty!"

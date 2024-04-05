#!/bin/bash

if [ "$SHELL" == "/bin/bash" ] || [ "$SHELL" == "/usr/bin/bash" ] || [ "$SHELL" == "/bin/zsh" ] || [ "$SHELL" == "/usr/bin/zsh" ]; then
    echo "Creating /usr/local/bin/sortty-bin/"
    echo

    echo "You might have to enter your root password"
    echo
    sudo mkdir /usr/local/bin/sortty-bin/

    echo "Moving main.py from src into /usr/local/bin/sortty-bin/"
    echo
    sudo cp src/main.py /usr/local/bin/sortty-bin/

    echo "Moving sortty.py from src into /usr/local/bin/sortty-bin/"
    echo
    sudo touch /usr/local/bin/sortty-bin/sortty.py
    sudo cp src/sortty.py /usr/local/bin/sortty-bin/sortty.py

    # places alias in rc file depending on shell
    if [ "$SHELL" == "/bin/bash" ] || [ "$SHELL" == "/usr/bin/bash" ]; then
        echo "Appending 'alias sortty='python3 /usr/local/bin/sortty.py'' to ~/.bashrc so that sortty can be run directly from the terminal"
        echo "alias sortty='python3 /usr/local/bin/sortty-bin/sortty.py'" >> ~/.bashrc
        
    elif [ "$SHELL" == "/bin/zsh" ] || [ "$SHELL" == "/usr/bin/zsh" ]; then
        echo "Appending 'alias sortty='python3 /usr/local/bin/sortty.py'' to ~/.zshrc so that sortty can be run directly from the terminal"
        echo "alias sortty='python3 /usr/local/bin/sortty-bin/sortty.py'" >> ~/.zshrc
        
    fi

    echo
    echo "Done, reopen your terminal so that you can run sortty directly from your terminal"
    echo
    echo "Run 'sortty --help' for instructions"
    echo
    echo "Have fun using sortty!"
    echo
else
    echo "Unrecognized shell (only bash and zsh are supported)"
fi

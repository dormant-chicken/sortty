echo "Creating /usr/local/bin/sortty-bin/"

sudo mkdir /usr/local/bin/sortty-bin/

echo "Moving main.py into /usr/local/bin/"

sudo cp main.py /usr/local/bin/sortty-bin/

echo "moving sortty.sh into /usr/local/bin/"

sudo touch /usr/local/bin/sortty
sudo cp sortty.sh /usr/local/bin/sortty

echo

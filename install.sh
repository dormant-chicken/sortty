echo "Creating /usr/local/bin/sortty-bin/"

sudo mkdir /usr/local/bin/sortty-bin/

echo "Moving main.py from src into /usr/local/bin/"

sudo cp src/main.py /usr/local/bin/sortty-bin/

echo "moving sortty.sh from src into /usr/local/bin/"

sudo touch /usr/local/bin/sortty
sudo cp src/sortty.sh /usr/local/bin/sortty

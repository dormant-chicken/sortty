echo "Creating /usr/local/bin/sortty-bin/"
echo "You might have to enter your root password"

sudo mkdir /usr/local/bin/sortty-bin/

echo "Moving main.py from src into /usr/local/bin/sortty-bin/"

sudo cp src/main.py /usr/local/bin/sortty-bin/

echo "Moving sortty.py from src into /usr/local/bin/"

sudo touch /usr/local/bin/sortty-bin/sortty.py
sudo cp src/sortty.py /usr/local/bin/sortty-bin/sortty.py

echo "Moving sortty.sh from src into /usr/local/bin/"

sudo touch /usr/local/bin/sortty
sudo cp src/sortty.sh /usr/local/bin/sortty

echo "Making /usr/local/bin/sortty executable"
sudo chmod +x /usr/local/bin/sortty

echo
echo "Done, now you can run sortty directly from your terminal"
echo
echo "Run 'sortty --help' for instructions"
echo
echo "Have fun using sorTTY!"
echo

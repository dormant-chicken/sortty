echo "Creating /usr/local/bin/sortty-bin/"

sudo mkdir /usr/local/bin/sortty-bin/

echo "Moving main.py from src into /usr/local/bin/sortty-bin/"

sudo cp src/main.py /usr/local/bin/sortty-bin/

echo "Moving sortty.sh from src into /usr/local/bin/"

sudo touch /usr/local/bin/sortty
sudo cp src/sortty.sh /usr/local/bin/sortty

echo "Making /usr/local/bin/sortty executable"
sudo chmod +x /usr/local/bin/sortty

echo
echo "Done, now you can run sortty directly from your terminal"
echo "Have fun using sorTTY!"
echo

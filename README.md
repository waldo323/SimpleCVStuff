SimpleCVStuff
=============

for my work on this I intend to be working with mostly the photobooth script

I found some issues with the instructions for installing SimpleCV.
I will list what I did in hopes that it will help others.
Also, if there are things I can improve this will be a good way for me to find out about the improvements.


(you can also install into a virtualenv. I didn't in this case)


sudo apt-get update


sudo apt-get -f install python-opencv python-scipy python-numpy python-pip 


git clone https://github.com/sightmachine/SimpleCV.git SimpleCV


cd SimpleCV


sudo setup.py install

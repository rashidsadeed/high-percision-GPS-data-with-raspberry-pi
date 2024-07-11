#High percision GPS data using raspberry pi

real time GPS data can be used in many different cases to accomodate location-boun systems and applications.
and often the general navigation data (longitude, latitude, altitude) doesn't suffice, and more in depth information 
such as psuedorange measurement, carrier phase measurement,  GNSS_ID etc... might be required by the application.

Here I have used a Ublox neo-M8P high percision GPS module connected to a raspberryPi to get GPS data
including navigation and raw data in real time. the GPS module is connected via a seiral port and operates at 
8Hz. you can change the frequency and the opertaion baudrate of the GPS module as per your needs. 

in order to make said changes, you either need to use the Ublox's "u-center" app which is quite helpfull and full of 
functionality, or you could do so programatically, in which case you would need to know the specific UBX message
class and payload to communicate with the GPS module and make the changes. 

the code is written in python, and you need the some libraries to run and use the application.
the following commands will help you install those libraries

> sudo pip install sparkfun-ublox-gps

> sudo pip install pyserial

> sudo pip install pyubx2

''' diff
- __NOTE: I'd advise to use a virtal environment to install the libraries and run the program to avoid contradictions__
- __with other libraries you might be using. You can do so using the following commands,__
'''

> python -m venv /path/to/new/virtual/environment

> source your_environment_name/bin/activate

after you activate the environment, go ahead and install the libraries, and then then run the program



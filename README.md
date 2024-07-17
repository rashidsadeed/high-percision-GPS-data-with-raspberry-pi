<h1>High percision GPS data using Raspberry pi</h1>

real time GPS data can be used in many different cases to accomodate location-bound systems and applications.
and often the general navigation data (longitude, latitude, altitude) doesn't suffice, and more in-depth information 
such as pseudorange measurement, carrier phase measurement,  GNSS_ID etc... might be required by the application.

Here I have used a Ublox neo-M8P high percision GPS module connected to a Raspberry Pi to get GPS data
including navigation(UBX-RXM-RAWX) and raw data(UBX-NAV-PVT) in real time. The module transmitts data in UBX format to the Raspberry Pi, which is then parsed to be human readable.
the GPS module is connected via a seiral port and operates at 8Hz.you can change the frequency and the opertaion baudrate of the GPS module as per your needs. 
in order to make said changes, you either need to use the Ublox's "u-center" app which is quite helpfull and full of 
functionality, or you could do so programatically, in which case you would need to know the specific UBX message
class and payload to communicate with the GPS module and make the changes. to make changes to the GPS's configutaion using the "u-center" windows application,
you would need to connect your GPS directly to your PC. depending on your GPS version, it might have a built in USB connection on board, otherwise you would need 
to use the TTL-USB converter board. 


**NOTE: I'd advise to use a virtal environment to install the libraries and run the program to avoid contradictions**
**with other libraries you might be using. You can do so using the following commands**


> python -m venv /path/to/new/virtual/environment

> source your_environment_name/bin/activate

after you activate the environment, go ahead and install the libraries, and then then run the program


**Not every GPS module can output RAWX data, please refer to the documentation and data sheets for your particular GPS model**

the code is written in python, and you need the some libraries to run and use the application.
the following commands will help you install those libraries

> sudo pip install sparkfun-ublox-gps

> sudo pip install pyserial

> sudo pip install pyubx2


You can also fetch AID-EPH ephemeris data from the GPS moduel using the eph_cls.py file. The ublox gps module outputs this data in 
form of Subframes, which then need to the parsed/decoded in order to get meaningful data. The Ephemeris_data class carries out bitwise manipulation 
and translation in order to make sense of the incoming data. The scheme to decode the data has been taken from the IS-GPS-200 standard for 
GPS data. feel free to take a look at the official docuementation and check in the code for any mishaps. 

**Note: as of NEO-M8, the AID-EPH data is no longer available and you have to use MGA-BDS-EPH data to get satalite data for GPS-fix which needs a subscription**
**This code is meant for legacy ublox GPS moduels prior to the  M8 series**




***Appalatian Trail Tracker***

Baasic overview:  my friend is hiking the Appalatian Trail and I wanted to make a gift for his family to track his progress
    on the way.  This is a map that hangs on their wall and an LED lights up where he is.

It works like this:

Friend goes to website I set up and website grabs his GPS data.

Microprocessor in the map logs onto the web and grabs the GPS data.

The LEDs are linked to GPS ranges and the LED lights up where he is at.

The processor goes to sleep for 24 hours and then starts over.

Video showing off the project - https://www.youtube.com/watch?v=0sJObhxlEMU


***Display***
ATmap.svg is the file for the laser cutter.  The LEDs are 3mm and are set 5mm apart.

The whole thing was set inside a puzzle box for easy back removal for repair and battery changing.


***Components***
NodeMCU esp8266

74HC595 shift registers

schematic file coming soon


***Some of the tutorials I used to get into micropython***

Using micropython with the esp8266 - http://docs.micropython.org/en/latest/esp8266/

Pushing code to the micropython - https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview

Dealing with shift registers (using the pyboard, but similar) - http://multiwingspan.co.uk/micro.php?page=pyshift


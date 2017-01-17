# appalachian-trail-tracker

***This project is in its initial stages still. 
Please see the devlog for a more complete step by step of how this is being created.***

This project is for a friend who is hiking the Appalachian Trail by himself.  
A trail tracker was out of the question, but his family back home still wanted a way to keep an eye on him 
and join him in his journey in some small way.

The process (thus far) is as follows:
1.  When he has cell access, friend uses his cell phone to go to a website set up for this project and click "Log location".
2.  The website will grab the GPS data from his phone and put it into a database.
3.  Arduino at home reads website and is connected to LEDs that run the length of the trail on a map.
4.  Arduino lights up the appropriate LED.

This is not meant to be super accurate - each of the LEDs will cover about 50 miles.  
But it will serve as a nice represenation - especially for his younger kids - as well as a rememberance/art piece
for when he is home.

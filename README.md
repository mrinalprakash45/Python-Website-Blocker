# Python Website Blocker

### Description ###

Python script that can be used to block certain websites during specified time periods throughout your working hours.

### Process ###

This script continuously checks the current time and blocks or unblocks websites accordingly. It uses the datetime module to define the start and end times for blocking websites, and the time module to pause the script for one minute between each time check. It also uses the with statement and the open function to open the /etc/hosts file in read and write

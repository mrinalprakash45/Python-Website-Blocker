# Python Website Blocker

### Description ###

Python script that can be used to block certain websites during specified time periods throughout your working hours.

### Process ###

This script continuously checks the current time and blocks or unblocks websites accordingly. It uses the datetime module to define the start and end times for blocking websites, and the time module to pause the script for one minute between each time check. It also uses the with statement and the open function to open the /etc/hosts file in read and write. If the current time is within the start and end times, the script appends the websites to the hosts file, which is used to block access to the specified websites. If the current time is outside of the start and end times, the script removes the websites from the hosts file to restore access to the websites.

Note: This script is designed to work on Windows systems, and it assumes that the hosts file is located at C:\\Windows\\System32\\drivers\\etc\\hosts. You may need to modify the script if you are using a different operating system or the hosts file is located in a different location. Also, be aware that modifying the hosts file can have unintended consequences, so use this script with caution.

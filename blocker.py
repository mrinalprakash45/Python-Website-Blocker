# Import the necessary modules
import time
import datetime
from datetime import datetime, timedelta

# Define a list of websites to block
websites = ["www.facebook.com", "www.twitter.com"]

# Define the start and end times for blocking websites
start_time = datetime(year=2022, month=1, day=1, hour=8, minute=0, second=0)
end_time = datetime(year=2022, month=1, day=1, hour=17, minute=0, second=0)

# Continuously check the current time and block websites if necessary
while True:
  # Get the current time
  current_time = datetime.now()

  # Check if the current time is within the specified time period
  if start_time <= current_time <= end_time:
    # Open the hosts file in read mode
    with open("/etc/hosts", "r") as file:
      # Read the contents of the hosts file
      content = file.readlines()

    # Open the hosts file in write mode
    with open("/etc/hosts", "w") as file:
      # Loop through the lines in the hosts file
      for line in content:
        # Check if the line contains a blocked website
        if not any(website in line for website in websites):
          # Write the line to the hosts file
          file.write(line)

      # Loop through the list of websites to block
      for website in websites:
        # Check if the website is already in the hosts file
        if website not in content:
          # Append the website to the hosts file
          file.write(f"\n127.0.0.1 {website}")

    # Print a success message
    print("Blocked websites successfully!")

  # Check if the current time is outside the specified time period
  elif current_time > end_time or current_time < start_time:
    # Open the hosts file in read mode
    with open("/etc/hosts", "r") as file:
      # Read the contents of the hosts file
      content = file.readlines()

    # Open the hosts file in write mode
    with open("/etc/hosts", "w") as file:
      # Loop through the lines in the hosts file
      for line in content:
        # Check if the line contains a blocked website
        if not any(website in line for website in websites):
          # Write the line to the hosts file
          file.write(line)

    # Print a success message
    print("Unblocked websites successfully!")

  # Sleep for one minute before checking the time again
  time.sleep(60)



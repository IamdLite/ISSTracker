# ISSTracker
ISSTracker is an intermediate program written in Python that notifies you with an email when the ISS satellite is overhead so
you can watch ride in the sky

# Note | Prerequisites to run this program

Before running this program ensure that:

Step 1 - You create a random email to test the program

Step 2 - In the "manage account" settings of the email, go to "Security" and actived the option "Allow insecure access from apps"

[?] The purpose of step 2 is to allow the smtp library to access the newly created account at the time the email is sent

Step 3 - The code is designed to tun indefinitely after every 60 seconds, so all you have to do is run to run the program once your computer is own, enable gmail notifications and within 24 hours, you'll see the satellite travelling a couple of  times over your head in the sky.

Step 4 - Follow the comments in the code for appropriate guidance,

## Concepts Practised

- Understanding API endpoints and interracting with external systems
- Hands-on the smtp library
- Using the .split() method to refactor time

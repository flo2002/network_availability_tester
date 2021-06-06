# import all the required packages
import os
import time
import datetime

# define a function to check, if we can ping
def check_ping():
    # define the domain, which I want to ping
    hostname = "google.com"
    # generate the raw response if I ping the upper hostname
    response = os.system("ping -n 1 " + hostname)

    # convert the response into human readable text
    if response == 0:
        response = "Network Active"
    else:
        response = "Network Error"

    # return the result of this test
    return response

# open a while loop, which will never end
while True:
    # call the function
    response = check_ping()
    # create the a string with the current datetime and the response of the ping
    status = str(str(datetime.datetime.now()) + ", " + response + "\n")

    # write the result into a text file
    with open("protocol.txt", "a") as myfile:
        myfile.write(status)

    # wait a second until the next iteration of this tester begins
    time.sleep(1)

# To be compatible with Linux and other distros

#!/usr/bin/env python

# Import the shodan library
# and import the sys library

import shodan
import sys

def usage():

    print("[!]Usage: ", sys.argv[0] + " <file_name> <shodan_api_key> <parameters> \n")
    sys.exit()

# Now start the crutial part of the program...
# The code to search for Apache using Shodan API

def shodan_search():

    # The first line of code in this function
    # takes the user input (command line arg)
    # and launches off with their api key. lol.

    api = shodan.Shodan(sys.argv[2])

    try:

        # Try to open the file specified in the argv[1]

        result_file = open(sys.argv[1], "w")

        if(result_file == 0):

            print("[!]Cannot open file")
            sys.exit()

        # Else continue on your merry way. :)

        results = api.search(sys.argv[3])

        for result in results['matches']:

            result_file.write(result['ip_str'])
            result_file.write("\n") # Add a newline so that way the IPs show up line by line
            
    # Or throw an error
    # Usually is caused by non members (didn't pay the one time fee)

    except shodan.APIError as error: # If a error is thrown, print the error and exit the script

        print("[!]Error: ", error)
        sys.exit()  # Just in case that this program doesn't exit properly

# now the main() function

def main():

    # If no arguments are supplied...
    # Throw a error and exit   

    # Also, len is used so that way I can compare the args to usage...
    # If it's less than 2, throw the error

    if(len(sys.argv) < 3):
        usage()

    # Else run through shodan_apache()
    shodan_search()

main()

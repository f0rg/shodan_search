# shodan_search
A script that allows the user to scrape Shodan API using certain parameters that are provided via sys.argv[] in Python.

# How to use:
Quick note: this script was meant to run on python 3.7.x.

In order to run this script you have to install the shodan Python lib. The command to install it is as follows:

pip install shodan

Usage: python shodan_search.py <file> <shodan_api_key> <parameters>
  
All the args are required. 

# Example:

python shodan_search.py search.txt (shodan_api_key) os:"linux" product:"OpenSSH"

API Key can be found at: https://account.shodan.io/




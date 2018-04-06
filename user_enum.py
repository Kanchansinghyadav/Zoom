# Required modules
import argparse
import requests
import re

parser = argparse.ArgumentParser() # defines the parser
parser.add_argument('-u', '--url', help='Target wordpress website') # Adding argument to the parser
args = parser.parse_args() # Parsing the arguments

users = [] # List for storing found usernames

def manual(url):
	print 'Scan Started' 
	for number in range(0, 9999):
		response = requests.get(url + '/?d3v=x&author=' + str(number)).text # Makes request to webpage
		match = re.search(r'/author/[^<]*/', response) # Regular expression to extract username
		if match:
			username = match.group().split('/author/')[1][:-4] # Taking what we need from the regex match
			print username.replace('/feed', '') # Print the username without '/feed', if present
			users.append(username) # Appending the username to users list
		
print("\n\n\t\t\t***********Disclaimer*************\n\n use this script on those targets on which you have permission, the creator is not resposible for any harm done by the one using this script\n\n ")
print("credits:- UltimateHackers(D3V) ")
print("Modified by:- K$Y")
print("\n\n\n\t\t\t*****White hats never do Illegel Things and They never leave trails*****")





if args.url:
	url = args.url # args.url contains value of -u option
	if 'http' not in url:
		url = 'http://' + url 
	manual(url)
else:
	parser.print_help()

if users: #checking the user list 
	print(users) #printing usernames
else:
	print("Some sort of problem, check url or might be Security Measure")

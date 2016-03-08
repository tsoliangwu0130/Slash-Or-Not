''' 
---- Tso-Liang Wu 03-07-2016 ---- 
*** Using a Crawler to retrieve courses data from http://catalog.oregonstate.edu/
*** According to the course data, return whether this course is a Slash course or not
'''

import requests
import re

while True:
	slashMsg = "Does not meet Graduate School's stand-alone requirement."
	course = raw_input('Enter Course Number (e.g: CS544) or Enter "quit" to Leave: ')

	if course == 'quit':
		exit()
	else:
		# Get course category and course number
		fstDigit    = re.search("\d", course).start()
		subjectCode = course[:fstDigit]
		courseNum   = course[fstDigit:]

		# Send request by GET method to http://catalog.oregonstate.edu/
		reqURL = "http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode="+subjectCode+"&coursenumber="+courseNum
		resq = requests.get(reqURL)

		# See the course is Slash or not
		if slashMsg in resq.text:
			print "Warning! " + course + " is a Slash course!"
		elif course in resq.text:
			print "Safe! " + course + " is not a Slash course!"
		else:
			print "Sorry, " + course + " is an invalid course number."
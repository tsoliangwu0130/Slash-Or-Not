''' 
---- Tso-Liang Wu 03-07-2016 ---- 
*** Using a Crawler to retrieve courses data from http://catalog.oregonstate.edu/
*** According to the course data, return whether this course is a Slash course or not
'''

import requests
import re

while True:
	course = raw_input('Enter Course Number ("quit" to leave): ')

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

		if "Does not meet Graduate School's stand-alone requirement." in resq.text:
			print "Warning! This is a Slash course!"
		else:
			print "Safe! This is not a Slash course!"
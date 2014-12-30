import requests
import tempfile
import re
from lxml import html
import csv
import sqlite3

from requests.auth import HTTPBasicAuth



db = sqlite3.connect('db.sqlite3')
#with open('itravel_report.csv', 'wb') as csvfile:
	#spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	#spamwriter.writerow(["iTravel", "bluetooth_logger", "system_time","wan_status","sdcard_status"]) 		
cursor = db.cursor()
#21,22,23,24,25,26,27,28,29,30,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,71,76,77,78,79,80,81,82,
for iTravel in [25,26,27,28,29,30,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,78,79,80,81,82,200,201,202]:
	try:			
		s = requests.Session()
		r = s.get('http://itravel'+str(iTravel)+'.mooo.com/')
		working=s.get('http://itravel'+str(iTravel)+'.mooo.com', auth=HTTPBasicAuth('root', 'miz@rw3b'))			
		tree = html.fromstring(r.text)		
		bluetooth_logger = tree.xpath('//span[@id="bt-logger-status"] //font /text()')
		if bluetooth_logger:
			system_time = tree.xpath('//span[@id="system-time"]/text()')
			wan_status = tree.xpath('//span[@id="wan-status"] //font /text()')
			sdcard_status = tree.xpath('//span[@id="sdcard-status"] //font /text()')					
			cursor.execute('''INSERT INTO report_question
                 VALUES(1,iTravel,bluetooth_logger, system_time, wan_status,sdcard_status)''')
		else:
			cursor.execute('''INSERT INTO report_question VALUES(1,'iTravel','---', '---', '---', '---')''')
	except  Exception, e:
			cursor.execute('''INSERT INTO report_question VALUES(1,'iTravel','---', '---', '---', '---')'''	)


db.commit()
csvfile.close()
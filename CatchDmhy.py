#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#Project:Catch img and link
#Descript:
#Author:CRoot

import urllib2,MySQLdb
from xml.etree import ElementTree as ET

def main:
	page = urllib2.urlopen('https://share.dmhy.org/topics/rss/rss.xml')
	html = page.read()
	dom = ET.fromstring(html)
	#dom = ET.parse('rss.xml')
	channel = dom.find('channel')
	item = channel.findall('item')
	for x in item:
		child = x.find('title')
		print '\n\n title:',child.text.encode('UTF-8')
		child = x.find('description')
		print '\ndescription',child.text.encode('UTF-8')
		child = x.find('enclosure')
		emurl = child.get('url')
		print '\nenclosure:',emurl
def InsertDate(title,content):
	db = MySQLdb.connect("localhost","***","***","***")
	cursor = db.cursor()
	sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
	try:
		cursor.execute(sql)
   		db.commit()
   	except:
   		db.rollback()
	db.close()
if __name__ == '__main__':
	main()

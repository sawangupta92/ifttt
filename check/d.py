from json import load
from urllib2 import urlopen
def get_temp():
	b='new delhi'
	n='http://openweathermap.org/data/2.1/find/name?q='+b.replace(' ','/')
	data = urlopen('http://openweathermap.org/data/2.1/find/name?q='+b.replace(' ','/'))
	# data=urlopen(n)
	c=load(data)
	# b='d b'
	# c=b.replace(' ','')
	# k=c['list'][0]['weather'][0]['main']
	# print city['weather']
	# k=city['weather'][0]
	# print k
	print c
 	# return k
get_temp()
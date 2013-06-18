from json import load
from urllib2 import urlopen
from pprint import pprint
def get_temp():
	data = urlopen('http://openweathermap.org/data/2.1/find/name?q=new/delhi')
	c=load(data)
	return c
	pprint(c['list'])
# get_temp()
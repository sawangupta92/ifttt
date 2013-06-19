from django.shortcuts import render_to_response
from json import load
from urllib2 import urlopen
# from smtplib import SMTP
# import smtplib
from django.core.mail import send_mail
def index(request):
	return render_to_response('index.html')
def view_temp(request):
	c = load(urlopen('http://openweathermap.org/data/2.1/find/name?q='+request.GET.get('location','oops').replace(' ','/')))
	if c['cod']=='404.3' or c['cod']=='404':
		k='oops wrong keyword'
	else:
		k=c['list'][0]['weather'][0]['main']
	return render_to_response('view_temp.html',{'c':k})
def mail(request):
	send_mail('hi','good','sawan.gupta92@gmail.com',['sawan.gupta92@gmail.com'])
	return render_to_response('test.html')
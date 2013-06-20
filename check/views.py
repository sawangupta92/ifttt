from django.shortcuts import render_to_response
from json import load
from urllib2 import urlopen
from django.core.mail import send_mail
# import django_cron
from django_cron import CronJobBase, Schedule

import datetime
def index(request):
	return render_to_response('index.html')
def view_temp(request):
	c = load(urlopen('http://openweathermap.org/data/2.1/find/name?q='+request.GET.get('location','oops').replace(' ','/')))
	if c['cod']=='404.3' or c['cod']=='404':
		k='oops wrong keyword'
	else:
		k=c['list'][0]['weather'][0]['main']
	if k=='Haze':
		mail(True,k)
	return render_to_response('view_temp.html',{'c':k})
def mail(request,msg):
	send_mail('hi','good','sawan.gupta92@gmail.com',['sawan.gupta92@gmail.com'])
	return render_to_response('mail.html')
# def test(CronJobBase):
# 	c=datetime.datetime.now()
# 	return render_to_response('test.html',{'a':c})
def test(request):
	c=datetime.datetime.now()
	return render_to_response('test.html',{'a':c})
class MyCronJob(CronJobBase):
	RUN_EVERY_MINS=1
	CRON_POLLING_FREQUENCY=10
	schedule=Schedule(run_every_mins=RUN_EVERY_MINS)
	code='check.1'
	ALLOW_PARALLEL_RUNS = True
	def do(self):
		send_mail('hi22','good','sawan.gupta92@gmail.com',['sawan.gupta92@gmail.com'])
		pass


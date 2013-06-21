#python manage.py installtasks
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from json import load
# from django.template.defaulttags import csrf_token
from urllib2 import urlopen
from django.core.mail import send_mail
import datetime
# from django.core.context_processors import csrf
# from django.core.context_processors import csrf
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
def test(request):
	c=datetime.datetime.now()
	return render_to_response('test.html',{'a':c})
def create_user(request):
	return render_to_response('create_user.html')
# @csrf_token
def mysave(request):	
	pass_word=request.GET.get('password','')
	user_name=request.GET.get('username','')
	email_id=request.GET.get('email_id','')
	a=User.objects.create_user(username=user_name,password=pass_word,email=email_id)
	a.save()
	return render_to_response('mysave.html')
	pass
def create_query(request):
	return render_to_response('create_query.html')
def save_query(request):
	return render_to_response('save_query.html')
	pass
# Create your views here
# from d import get_temp
from django.shortcuts import render_to_response
# from d import get_temp

def index(self):
	return render_to_response('index.html')
	pass
def view_temp(self):
	a=__import__('check/d.py')
	print a['list']

	pass
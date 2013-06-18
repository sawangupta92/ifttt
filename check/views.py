# Create your views here
from d import LazyEncoder
from django.shortcuts import render_to_response
# from d import get_temp

def index(self):
	return render_to_response('index.html')
	pass
def view_temp(self):
	c=LazyEncoder.get_temp()
	return render_to_response('view_temp.html',{'c':c})
	pass
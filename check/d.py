from json import load,dumps
from urllib2 import urlopen
from pprint import pprint
import json
from django.utils.functional import Promise
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)
    def get_temp(self):
    	data = urlopen('http://openweathermap.org/data/2.1/find/name?q=new/delhi')
			self.default(data)
			# c=load(data)
			return c

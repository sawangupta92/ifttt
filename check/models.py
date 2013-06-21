from django.db import models
from django.contrib.auth.models import User
class weather(models.Model):
	u_id=models.ForeignKey(User)
	city=models.CharField(max_length=50)
	weather_condition=models.CharField(max_length=50)
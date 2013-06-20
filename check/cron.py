import kronos
from django.core.mail import send_mail
@kronos.register('* * * * 1')
def p_task():
	send_mail('cronjobs','good','sawan.gupta92@gmail.com',['sawan.gupta92@gmail.com'])
	pass
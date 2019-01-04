from django.db import models
from django import forms



# Create your models here.
class SignUp(models.Model):
	JIN="金"
	FEMALE='女'
	ADD_ATTR = (("金","金"),("木","木"),("水","水"),("火","火"),("土","土"))
	# ADD_ATTR = (('Gold',"金"),("Wood","木"),("Water","水"),("Fire","火"),("Earth","土"))
	ADD_GENDER = (('男','男'),("女","女"))
	ADD_LAN= (('中国','中国'),('其他','其他'))
	"""docstring for NewsLetter"""
	email = models.EmailField(blank=False)
	full_name = models.CharField(max_length = 120, blank=False, null=False,unique=True)
	country = models.CharField(max_length=6,choices=ADD_LAN)
	gender = models.CharField(max_length=6,choices=ADD_GENDER,default=FEMALE)
	attribute = models.CharField(max_length=6,choices=ADD_ATTR,default=JIN)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	

	def __unicode__(self): 
		return self.full_name

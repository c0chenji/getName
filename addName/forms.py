from django import forms
from .models import SignUp
from django.db import models

class SignUpForm(forms.ModelForm):
	class Meta:
		"""docstring for Meta"""
		model = SignUp
		fields = ['full_name','gender','attribute','country']
	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base, provider = email.split("@")
	# 	domain,extention = provider.split(".")
	# 	if  not "usc" == domain:
	# 		raise forms.ValidationError("please use a valid usc domain")
	# 		return email
	# 	if not "edu"== extention:
	# 		raise forms.ValidationError("Please use a valid .EDU email address")
	# 	return email		
		
			

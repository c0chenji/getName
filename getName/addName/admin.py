from django.contrib import admin
from .forms import SignUpForm
# Register your models here.
from .models import SignUp
class SignUpAdmin(admin.ModelAdmin):
	list_display =["__unicode__", "timestamp","updated",'gender',"attribute"]
	form = SignUpForm
	# class meta(object):
	# 	"""docstring for meta"""
	# 	model = SignUp
	# 	def __init__(self, arg):
	# 		super(meta, self).__init__()
	# 		self.arg = arg
			

admin.site.register(SignUp,SignUpAdmin)
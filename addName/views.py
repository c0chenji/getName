from django.shortcuts import render
from .forms import SignUpForm
from django.conf import settings
from .models import SignUp
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
import random
from random import randint

# Create your views here.
# save data and display it on the page
def add_display(request):
    title = "已添加的名字："
    message=""
    signup = SignUp.objects.all()
    form = SignUpForm(request.POST or None)
    # if request.user.is_authenticated():
    #     title= "My Title is %s" %(request.user)
    context = {
        "entries" : signup,
        "template_title":title,
        "new_message":message,
        "form":form,
        
    } 

    if form.is_valid():
        instance=form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if instance.full_name == None:
            full_name = "New full_name"
        instance.full_name= full_name
        instance.save()
        message="new name added"
        context={
            "entries" : signup,
            "new_message":message,
            "form":form,
        }  

    return render(request, "addName.html", context)


# Get the request datas and show random one of them
def search(request):
  if ('country' in request.GET and request.GET['country']) and ('gender' in request.GET and request.GET['gender']) and('attr' in request.GET and request.GET['attr']):
    a = request.GET['country']
    b  = request.GET['gender']
    c  = request.GET['attr']
    query = a + " , " + b +" 以及 " + c
    results =SignUp.objects.filter(country__icontains=a, gender__icontains=b,attribute__icontains=c)
    count = results.count()
    single_result=results[randint(0,count-1)]
   
    return render_to_response('search_results.html',
      {'results': single_result ,  'query':query})
  else:
    return HttpResponse('Please submit a search term.')

def search_form(request):

  return render_to_response('search_form.html')

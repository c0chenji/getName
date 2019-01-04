from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
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

# def contact(request):
#     form = ContactForm(request.POST or None)

#     if form.is_valid():
#         # print(form.cleaned_data)
#         form_email = form.cleaned_data.get("email")
#         form_message = form.cleaned_data.get("message")
#         form_full_name = form.cleaned_data.get("full_name")
#         subject = "site contact form"
#         from_email = settings.EMAIL_HOST_USER
#         to_email = [from_email ]
#         contact_message ="%s: %s via %s"%(form_full_name,form_message, form_email)
#         send_mail(subject,
#             contact_message,
#             from_email,
#             to_email,
#             fail_silently=False)
#     context={
#         "form":form,
#     }
#     return render(request, "forms.html",context)


def search(request):
  if ('country' in request.GET and request.GET['country']) and ('gender' in request.GET and request.GET['gender']) and('attr' in request.GET and request.GET['attr']):
    a = request.GET['country']
    b  = request.GET['gender']
    c  = request.GET['attr']
    query = a + " , " + b +" 以及 " + c
    # attri = SignUp.objects.filter(attribute__icontains=q)
    # results = attri.filter(gender__icontains=l)
    results =SignUp.objects.filter(country__icontains=a, gender__icontains=b,attribute__icontains=c)
    return render_to_response('search_results.html',
      {'results': results ,  'query':query})
  else:
    return HttpResponse('Please submit a search term.')

def search_form(request):

  return render_to_response('search_form.html')

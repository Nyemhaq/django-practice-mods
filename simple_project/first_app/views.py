from django.shortcuts import render
from django.http import HttpResponse

def about (req):
    return render (req, 'first_app/about.html')
def contact (req):
    return render (req, 'first_app/contact.html')
def service (req):
    return render (req, 'first_app/service.html')
 
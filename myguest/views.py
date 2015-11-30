from django.shortcuts import render, render_to_response
from myguest.models import Guest

# Create your views here.
def main(request):
    return render_to_response('main.html')

# http://127.0.0.1:8000/guest?startPage=600&perPage=6300  
def guest(request):
    index = request.GET['startPage']
    perPage = request.GET['perPage']
    #return render_to_response('guest.html',{'guests':Guest.objects.all()})
    #return render_to_response('guest.html',{'guests':Guest.objects.filter(id = 100)})
    #return render_to_response('guest.html',{'guests':Guest.objects.all().order_by('-id')[int(index):int(perPage)] })
    return render_to_response('guest.html',{'guests':Guest.objects.all()[int(index):int(perPage)] })
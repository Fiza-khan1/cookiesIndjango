from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
def setCookie(request):
    response= render(request,'setcookie.html')
    # response.set_cookie('Name','Fiza',max_age=60)
    expires = timezone.now() + timedelta(days=2)
    # response.set_cookie('Name','Fiza',expires=expires)
    response.set_signed_cookie('Name','Fiza',expires=expires,salt='nm')

    return response

def getCookie(request):
    # name=request.COOKIES['Name']
    # name=request.COOKIES.get('Name','None')
    name=request.get_signed_cookie('Name',salt='nm',default='None')
    return render(request,'getcookie.html',{'name':name})


def delCookie(request):
    
    response=render(request,'delcookie.html')
    response.delete_cookie('Name')
    return response
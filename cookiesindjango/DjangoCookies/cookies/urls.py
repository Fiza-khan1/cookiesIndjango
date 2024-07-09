
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('setCookie/',views.setCookie,name='setcookie'),
    path('getcookie/',views.getCookie,name='getcookie'),
    path('delCookie/',views.delCookie,name="delCookie")
]
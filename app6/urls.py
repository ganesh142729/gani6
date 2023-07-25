from django.urls import path
from app6.views import *
app_name='thred'
urlpatterns = [
    path('index3/',index3,name='index3'),
    path('index4/',index4,name='index4'),
]
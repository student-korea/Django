
from django.urls import path,include
from . import views
app_name='member'
urlpatterns = [
    path('',views.member,name='member')
]

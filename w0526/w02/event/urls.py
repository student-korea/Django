
from django.urls import path,include
from . import views
app_name=''
urlpatterns = [
    path('event/',views.event,name='event.html')
]

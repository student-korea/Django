from django.urls import path
from . import views
app_name=''
urlpatterns = [
    path('',views.index,name="index"),
    path('write/',views.write,name="write"),
]
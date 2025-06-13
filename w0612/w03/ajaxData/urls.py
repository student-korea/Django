from django.urls import path,include
from . import views

app_name = 'ajaxData'
urlpatterns = [
    path('bWrite/', views.bWrite, name='bWrite'),
]

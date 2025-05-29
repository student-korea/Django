from django.urls import path,include
from . import views
app_name='studdents'
urlpatterns = [
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'),
    path('update/{{int:no}}/',views.update,name='update'),
    path('view/{{int:no}}/',views.view,name='view'),
]

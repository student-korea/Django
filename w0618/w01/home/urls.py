
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

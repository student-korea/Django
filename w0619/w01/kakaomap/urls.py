
from django.urls import path,include
from . import views

app_name='kakaomap'
urlpatterns = [
    path('list/',views.list,name='lsit'),
    
]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

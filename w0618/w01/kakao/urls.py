
from django.urls import path,include
from . import views

app_name='kakao'
urlpatterns = [
    path('oauth/',views.oauth,name='oauth'),
    
]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

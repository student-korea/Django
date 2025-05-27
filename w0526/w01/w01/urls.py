
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), #students 앱에 있는 urls.py 연결
    path('', include('home.urls')),
]

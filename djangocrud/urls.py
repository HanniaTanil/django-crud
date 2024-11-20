from django.contrib import admin
from django.urls import path
from tasks.views import helloworld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', helloworld), 
]

from django.contrib import admin
from django.urls import path
from core.views import index, message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', message, name='messages'),
    path('', index, name='index')
]

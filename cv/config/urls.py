
from django.contrib import admin
from django.urls import path
from cv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name='accept'),
]


from django.contrib import admin
from django.urls import path
from cv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name='accept'),
    path('cv-list/', views.cv_list, name='cv_list'),
    path('cv/<int:id>', views.cv, name='cv'),
]

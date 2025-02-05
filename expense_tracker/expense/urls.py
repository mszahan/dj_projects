from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homepage' ),
    path('edit/<int:id>/', views.edit, name='edit_expense'),
    path('delete/<int:id>/', views.delete, name='delete_expense'),
]
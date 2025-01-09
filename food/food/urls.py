from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='food_list' ),
    path('<int:id>/', views.product_detail, name='food_detail'),
    path('add-product/', views.create_product, name='create_product'),
    path('update-product/<int:id>/', views.update_product, name='update_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
]
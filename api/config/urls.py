
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet

router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('action', ActionViewSet, basename='action')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

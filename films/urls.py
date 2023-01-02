from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'films', views.FilmViewSet)
router.register(r'series', views.SeriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

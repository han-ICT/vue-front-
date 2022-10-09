from django.urls import path, include
from location import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('',views.LocationViewSet)
from . import views

urlpatterns = [
    path('', include(router.urls)),
    path('location_list/', views.location_list),
    path('<int:pk>/', views.person_location)
]
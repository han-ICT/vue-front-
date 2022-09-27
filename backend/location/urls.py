from django.urls import path
from location import views

urlpatterns = [
    path('', views.location_list),
    path('<int:pk>/', views.person_location)
]
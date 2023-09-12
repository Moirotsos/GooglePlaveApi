from django.urls import path
from . import views


urlpatterns = [
    path('places/', views.getPlace),
    path('save_place/', views.save_place),
    path('description_place/<str:place_id>/', views.description_place),
]
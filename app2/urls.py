from django.urls import path

from app2 import views

urlpatterns = [
    path('index1/', views.app2_index1),
]
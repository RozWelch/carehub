from . import views
from django.urls import path

urlpatterns = [
    path('', views.CarearticleList.as_view(), name='home')
]
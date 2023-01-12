from . import views
from django.urls import path

urlpatterns = [
    path('', views.CarearticleList.as_view(), name='home'),
    path('<slug:slug>/', views.CarearticleDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.CarearticleTick.as_view(), name='post_tick'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('image/<int:image_id>/', views.image_detail, name='image_detail'),
    path('recentimage/<int:image_id>/', views.recent_image_detail, name='recent_image_detail'),

] 

from django.urls import path
from . import views


urlpatterns = [
    path('', views.public_feed, name='home'),
    path('add/', views.add_post)
]
from django.urls import path
from . import views

urlpatterns = [
    path('web/', views.dhol, name = 'dhol'),
    path('websid/', views.dhola, name = 'dhola'),
    path('website/', views.web_app, name = 'page')
]

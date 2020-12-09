from django.urls import path
from .views import index, CV, projects, contact



app_name= 'core'


urlpatterns= [
    path('', index, name='index'),
    path('CV/', CV, name='CV'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]

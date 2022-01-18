from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('skills',views.skills, name='skills'),
    path('service',views.service, name='service'),
    path('contact',views.contact, name='contact'),
    path('blog',views.blog, name='blog'),
    path('demo', views.demo, name='demo'),
 ]
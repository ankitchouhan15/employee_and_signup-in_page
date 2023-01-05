from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('index', views.index, name='index'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('signinpage', views.signinpage, name='signinpage'),
    path('signinsuccess_logout', views.signinsuccess_logout, name='signinsuccess_logout'),
    path('logout', views.logout, name='logout'),
]

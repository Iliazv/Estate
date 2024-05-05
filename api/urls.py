from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('searched/', views.searched, name='searched'),
    path('report/', views.report, name='report'),
    path('contact/', views.contact, name='contact'),
    path('<int:year>', views.index, name='index'),
    path('estate/<int:pk>', views.estate_object, name='estate_object'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registered/', views.registered, name='registered'),
    path('logout/', views.logout_view, name='logout_view'),
    path('agreement/', views.agreement, name='agreement'),
    path('change_currency/', views.change_currency, name='change_currency'),
    path('remain_currency/', views.remain_currency, name='remain_currency'),
]
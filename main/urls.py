from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('form0/', views.form0, name='0_level'),
    path('form1/', views.form1, name='1_level'),
    path('form2/', views.form2, name='2_level'),
    path('form3/', views.form3, name='3_level'),
    path('form4/', views.form4, name='4_level'),
    path('form5/', views.form5, name='5_level'),
]

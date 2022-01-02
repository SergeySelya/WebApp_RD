from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('form0/', views.PostListView0.as_view(), name='0_level'),
    path('form1/', views.PostListView1.as_view(), name='1_level'),
    path('form2/', views.PostListView2.as_view(), name='2_level'),
    path('form3/', views.PostListView3.as_view(), name='3_level'),
    path('form4/', views.PostListView4.as_view(), name='4_level'),
    path('form5/', views.PostListView5.as_view(), name='5_level'),
]

from django.urls import path
from . import views



urlpatterns = [
    # path('', views.index, name='main'),
    # path('about', views.about, name='about'),
    # path('create', views.create, name='create')
    path('', views.create, name='create'),
    path('about', views.about, name='about'),
    path('admin/', views.index, name='main'),
    path('login/', views.user_login, name='login'),

]


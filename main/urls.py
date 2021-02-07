from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('objects_map', views.objects_map, name='objects_map'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/<int:id>/', views.portfolio_single, name='portfolio_single'),
    path('about', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('add_comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('blog/<str:slug>/', views.post, name='post'),
    path('contacts', views.contacts, name='contacts'),
]
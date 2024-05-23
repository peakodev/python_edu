from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('<slug:author_slug>/', views.author_detail, name='author_detail'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('', views.index, name='index'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Assigns a "view" called post_list to the root urls
    path('', views.post_list, name='post_list'),

    # url for a specific post will beginwith 'post/'' then converts that
    # specific post instance's pk (primary key; like a unique identifier for
    # each post 1, 2, 3, etc) to and int and is followed by another /
    # All together it will be something like http://127.0.0.1:8000/post/5/
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

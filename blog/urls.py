from django.urls import path
from . import views

urlpatterns = [
    # Assigns a "view" called post_list to the root urls
    path('', views.post_list, name='post_list'),
]

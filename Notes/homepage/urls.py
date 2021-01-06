from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.show_index),
    path('index',views.show_index),
    path('',views.show_index),
]
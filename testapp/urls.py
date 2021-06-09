from django.urls import path

from . import views


urlpatterns = [
    path('create_users/', views.create_users, name="create_users"),
    path('heapify_users/', views.heapify_users, name="heapify_users"),


]

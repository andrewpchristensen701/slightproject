
from django.contrib import admin
from django.urls import path
from twitterclone.twitteruser import views

urlpatterns = [
    path('user/<int:id>/', views.profile_view, name='profile'),
    path('follow_user/<int:id>/', views.follow_user, name='follow_user'),
    path('unfollow_user/<int:id>/', views.unfollow_user, name='unfollow_user')
]
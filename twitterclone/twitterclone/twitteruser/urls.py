from django.urls import path
from twitterclone.twitteruser import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('profile/<int:id>', views.viewprofile, name='profile_view'),
    path('follow/<int:id>', views.followuser, name='follow_view'),
    path('unfollow/<int:id>', views.unfollowuser, name='unfollow_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
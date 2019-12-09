from django.urls import path
from twitterclone.tweet import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.viewmainpage, name='homepage'),
    path('addtweet/', views.maketweet, name='make_tweet_view'),
    path('view_tweet/<int:id>/', views.viewtweet, name='view_tweet_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
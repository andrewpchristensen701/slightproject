from django.urls import path
from twitterclone.notification import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('notification/<int:id>/', views.notificationpage,
         name='notify_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
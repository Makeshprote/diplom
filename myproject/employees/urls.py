from django.contrib import admin
from django.urls import path, include
from employees import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('event_list/', views.event_list),
    path('api/events/', views.EventListAPIView.as_view(), name = 'event_list'),
    path('api/events/<int:pk>/', views.EventDetailAPIView.as_view(), name='event-detail'),
    path('', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

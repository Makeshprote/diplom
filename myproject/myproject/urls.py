from django.contrib import admin
from django.urls import path, include
from employees import views
from django.conf import settings
from django.conf.urls.static import static
from controller.views import handle_controller_message


urlpatterns = [
    path('', admin.site.urls),
    path('handle-controller-message/', handle_controller_message, name='handle_controller_message'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


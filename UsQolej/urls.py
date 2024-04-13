from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('my_admin_panel_vsc/', admin.site.urls),
    path('',include('main.urls')),
    path('en/',include('English.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

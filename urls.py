from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views  
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')), 
    path('', views.home, name='home'),  
    path('', include('main.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


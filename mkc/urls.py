
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('customer/', include('customer.urls')),
    path('authentication/', include('user_authentication.urls')),
    path('Book/', include('Book.urls')), 

    
]
if settings.DEBUG:
  urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    
    
    

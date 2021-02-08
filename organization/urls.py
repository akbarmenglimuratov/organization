from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/organization/', include('core.urls')),
    path('api/account/', include('user.urls')),
    # path('', include('gui.urls')),
]
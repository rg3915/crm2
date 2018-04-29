from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myproject.core.urls')),
    path('accounts/', include('myproject.accounts.urls')),
    path('crm/', include('myproject.crm.urls')),
    path('admin/', admin.site.urls),
]

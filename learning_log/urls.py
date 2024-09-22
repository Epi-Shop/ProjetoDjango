from django.contrib import admin
from django.urls import path, include

# O include leva as informações para o arquivo learning_log.urls e users.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
    path('users/', include('users.urls')),
]

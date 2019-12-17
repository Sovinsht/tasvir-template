
from django.contrib import admin
from django.urls import path, include
from photo_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo_app.urls')),
    path('user/', include('user_app.urls'))
]


from django.contrib import admin
from django.urls import path, include

import webstudio28

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webstudio28.common.urls')),

]

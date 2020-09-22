from django.contrib import admin
from django.urls import include, path
from links.tasks import *

urlpatterns = [
    path('', admin.site.urls),
    path('upload/', include('links.urls')),
]

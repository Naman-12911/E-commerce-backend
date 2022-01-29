from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import url

# apps urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')), # auth url
]

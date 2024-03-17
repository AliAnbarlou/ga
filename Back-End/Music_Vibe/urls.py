"""
URL configuration for Music_Vibe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_404_error_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/',include("all.urls")), #Show all the music
    path('about/', views.About, name='About'), #Show About us page
    path('contact-us/', views.Contact, name='Contact'), #Show Contact us page
    path('', views.Home_Page, name='Home'), #Show Home page
    path('artists/',include('artists.urls'), name='Artist'), #Show
]
handler404 = custom_404_error_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
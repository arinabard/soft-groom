"""soft_groom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from app import views as app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path('comments/', app_views.comments, name='comments'),
    path('comments/add_model/', app_views.add_model_comment, name='add_model_comment'),
    path('about-us/', app_views.about, name='about'),
    path('gallery/', app_views.gallery, name='gallery'),
    path('services/', app_views.services, name='services'),
    path('register/', app_views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]
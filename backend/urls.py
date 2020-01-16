"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from backend import settings
from codes.views import (
    event_cities, csrf, reg_user, login_user,
    create_profile,
    upload_profile_pic, get_user, get_all_users, get_all_events, get_event,
    check_auth, user_logout, create_event, event_preview, event_main)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event-cities', event_cities, name='event_cities'),
    path('csrf', csrf),
    path('reg/', reg_user),
    path('login/', login_user),
    path('create_profile/', create_profile),
    path('upload_profile_pic/', upload_profile_pic),
    path('user/', get_user),
    path('get_all_users/', get_all_users),
    path('get_all_events/', get_all_events),
    path('events/', get_event),
    path('check_auth/', check_auth),
    path('logout/', user_logout),
    path('create_event', create_event),
    path('upload_event_preview_pic/<int:pk>/', event_preview),
    path('upload_event_main_pic/<int:pk>/', event_main),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for readtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tracker import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.IndexView.as_view(),name="home"),
    path('read/create/',views.ReadCreateView.as_view(),name="read-create"),
    path('read/list/',views.ReadListView.as_view(),name="read-list"),
    path('read/<int:pk>/',views.ReadDetailView.as_view(),name="read-detail"),
    path('read/<int:pk>remove/',views.ReadDeleteView.as_view(),name="read-delete"),
    path('read/<int:pk>change/',views.ReadUpdateView.as_view(),name="read-update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


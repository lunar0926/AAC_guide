"""aac_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mainapp import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('community/', views.community, name='community'),
    path('contact/', views.contact, name='contact'),
    path('search/',views.search, name="search"),
    path('conclusion/', views.conclusion, name='conclusion'),
    path('thank/', views.thank, name='thank'),

    # Commumity 탭의 기능
    path('summernote/', include('django_summernote.urls')),
    path('detail/<int:post_id>', views.detail, name='detail'),
    

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

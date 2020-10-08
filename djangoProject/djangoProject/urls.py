"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views, views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^logout/$', auth_views.LoginView.as_view(template_name="registration/logout.html"), name="logout"),

    path('', include('surveillance_bot_webapp.urls'))
#    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

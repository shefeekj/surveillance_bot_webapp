from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# import views from local directory.
from . import views
urlpatterns = [
    path('', views.index_page, name='index'),
]
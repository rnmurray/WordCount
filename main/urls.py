from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  path("count/", views.count, name='count')
]

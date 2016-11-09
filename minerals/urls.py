from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<name>.*)/$', views.mineral_detail, name='mineral'),
    url(r'^$', views.random_mineral, name='random_mineral'),
]

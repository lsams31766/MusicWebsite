from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/71/  number 0 to 9, any number of digits
    url(r'^(?P<song_id>[0-9]+)/$', views.detail, name='detail'),
]

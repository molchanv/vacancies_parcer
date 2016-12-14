from django.conf.urls import include, url

from base.views import panel, start

urlpatterns = [
    url(r'^$', panel, name='panel'),
    url(r'^start/$', start, name='start'),
]

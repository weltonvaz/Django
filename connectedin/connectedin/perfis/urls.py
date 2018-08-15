# arquivo connectedin/perfis/urls.py

from django.conf.urls import url
from perfis.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^heros/$', views.Heros2View.as_view()),
    url(r'^heros/(?P<pk>\d+)/$', views.Hero2View.as_view()),
]

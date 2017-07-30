from django.conf.urls import url
from warehouse import views

urlpatterns = [
    url(r'^$', views.start, name = "start"),
]

from django.conf.urls import url
from calc import views

urlpatterns = [
    url(r'^$', views.make_form, name = "make_form"),
]

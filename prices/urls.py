from django.conf.urls import url
from prices import views

urlpatterns = [
    url(r'^prices/$', views.PricesList.as_view()),
    url(r'^prices/(?P<pk>[0-9]+)/$', views.PriceDetail.as_view()),
]

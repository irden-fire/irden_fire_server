from django.conf.urls import url
from orders import views

urlpatterns = [
    url('^orders/$', views.OrdersList.as_view()),
    url(r'^orders/(?P<pk>[0-9]\d+)/$', views.OrderDetail.as_view()),
]

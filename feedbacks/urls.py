from django.conf.urls import url
from feedbacks import views

urlpatterns = [
    url(r'^feedbacks_custom_size/$', views.FeedbacksListCustomSize.as_view()),
    url(r'^feedbacks/$', views.FeedbacksList.as_view()),
    url(r'^feedbacks/(?P<pk>[0-9]\d+)/$', views.FeedbackDetail.as_view()),
]

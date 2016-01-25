from django.conf.urls import include, patterns, url
from authentication.views import UserListAPIView
from authentication.views import CurrentUserView
from authentication.views import CreateUserView
from authentication.views import CreateUserDataView
from authentication.views import UpdateUserDataView

urlpatterns = [
    'rest_framework_jwt.views',
    url(r'api/v1/auth/login/', 'obtain_jwt_token'),
    url(r'api/v1/current_user/', CurrentUserView.as_view()),
    url(r'api/v1/create_user/', CreateUserView.as_view()),
    url(r'create_user_data/', CreateUserDataView.as_view()),
    url(r'^update_user_data/(?P<pk>[0-9]\d+)/$', UpdateUserDataView.as_view()),
]

from django.conf.urls import include, patterns, url
from authentication.views import UserListAPIView
from authentication.views import CurrentUserView
from authentication.views import CreateUserView
from authentication.views import CreateUserDataView


urlpatterns = [
    url(r'api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'api/v1/current_user/', CurrentUserView.as_view()),
    url(r'api/v1/create_user/', CreateUserView.as_view()),
    url(r'create_user_data/', CreateUserDataView.as_view()),
]

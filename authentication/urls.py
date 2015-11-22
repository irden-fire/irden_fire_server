from django.conf.urls import include, patterns, url
from authentication.views import UserListAPIView
from authentication.views import CurrentUserView


urlpatterns = [
    url(r'api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'api/v1/current_user/', CurrentUserView.as_view()),
]

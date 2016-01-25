from django.test import TestCase
from feedbacks.models import Feedback
from rest_framework.test import APIRequestFactory
from rest_framework import status
from authentication import views
from rest_framework.test import force_authenticate

factory = APIRequestFactory()
user = User.objects.get(username='forrana')
view = UserData.as_view()

# Make an authenticated request to the view...
request = factory.get('/api/v1/auth/login/')
force_authenticate(request, user=user)
response = view(request)

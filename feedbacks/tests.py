from django.test import TestCase
from feedbacks.models import Feedback
from rest_framework.test import APIRequestFactory
from rest_framework import status
from feedbacks import views

class FeedbackTestSort(TestCase):
    def setUp(self):
        Feedback.objects.create(title='test1', rate=9)
        Feedback.objects.create(title='test2', rate=10)

    def test_sorting_order(self):
        tests = Feedback.objects.all()
        self.assertEqual(tests[0].title, 'test2')
        self.assertEqual(tests[1].title, 'test1')

class FeedbackTestPost(TestCase):
    def setUp(self):
        Feedback.objects.create(title='test1', rate=9)
        Feedback.objects.create(title='test2', rate=10)

    def test_posting_order_fail(self):
        view = views.FeedbacksList.as_view()
        factory = APIRequestFactory()
        request = factory.post('/feedbacks/', {'title': 'new feedback'}, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_posting_order_pass(self):
        view = views.FeedbacksList.as_view()
        factory = APIRequestFactory()
        feedback = {'title': 'new feedback', 'message': 'test message',
                    'author': 'test author', 'rate':'10', 'email':'test email'}
        request = factory.post('/feedbacks/', feedback, format='json')
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_feedbacks(self):
        

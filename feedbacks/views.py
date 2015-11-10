from feedbacks.models import Feedback
from feedbacks.serializers import FeedbackSerializer
from feedbacks.paginators import CustomSizeSetPagination

from rest_framework import generics

class FeedbacksList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbacksListCustomSize(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = CustomSizeSetPagination

class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

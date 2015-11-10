from rest_framework import serializers
from feedbacks.models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'created', 'title', 'message', 'author', 'rate')

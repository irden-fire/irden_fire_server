from django.contrib import admin
from feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'created')

admin.site.register(Feedback, FeedbackAdmin)

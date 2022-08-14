from django.contrib import admin
from .models import Answers, Question, Quiz

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'question')

admin.site.register(Answers)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)

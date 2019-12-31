from django.contrib import admin  #

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date informtaion', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]
  # fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
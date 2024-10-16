from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):  # change layout from Stacked to Tabular
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

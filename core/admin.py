from django.contrib import admin

from . models import *

admin.site.site_header = 'Zago Admin Area'
admin.site.site_title = 'Admin zone'
admin.site.index_title = 'Welcome to the zone'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
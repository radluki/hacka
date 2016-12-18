from django.contrib import admin

# Register your models here.

from .models import Question, User

class UserAdmin(admin.ModelAdmin):
    # ...
    list_display = ('login', 'password', 'date','longitude','latitude')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','answer','user_id')

admin.site.register(Question,QuestionAdmin)
admin.site.register(User,UserAdmin)

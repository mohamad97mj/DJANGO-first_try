from django.contrib import admin
from .models import Question, Choice, Token, NewUser

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Token)
admin.site.register(NewUser)
# Register your models here.

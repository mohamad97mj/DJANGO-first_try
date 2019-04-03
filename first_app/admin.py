from django.contrib import admin
from .models import Question, Choice, Token, NewUser

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Token)
admin.site.register(NewUser)

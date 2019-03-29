from django.contrib import admin
from .models import Question, Choice, Token

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Token)
# Register your models here.

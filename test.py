import django
from first_app.models import Question, Choice


django.setup()
print(Question.objects.all())

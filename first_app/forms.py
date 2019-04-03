from django import forms
from django.core import validators
from .models import NewUser

#
# class MyForm(forms.Form):
#     name = forms.CharField(validators=[validators.MaxLengthValidator(8)])
#     email = forms.CharField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
#
#     def clean_botcatcher(self):
#         botcatcher = self.cleaned_data['botcatcher']
#         if len(botcatcher)>0:
#             raise forms.ValidationError("GOTCHA BOT")
#         return botcatcher


class UserForm(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = '__all__'

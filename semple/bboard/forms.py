from django import forms
from .models import SMS

class SMSForm(forms.ModelForm):
    class Meta:
        model = SMS
        fields = ('sender', 'receiver', 'message')

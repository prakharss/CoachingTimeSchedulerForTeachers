import re
from django import forms
from django.utils.translation import ugettext_lazy as _
 
class StudentDetails(forms.Form):
 
    name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Name"), error_messages={ 'invalid': _("name must contain only letters") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email"))
 

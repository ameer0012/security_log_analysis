from django import forms
from .models import LogParsingRule


class LogParsingRuleForm(forms.ModelForm):
    class Meta:
        model = LogParsingRule
        fields = ['log_source_type', 'required_fields', 'parsing_patterns']


class LogParsingRuleAddForm(forms.Form):
    log_source_type = forms.CharField(max_length=100)
    required_fields = forms.CharField(widget=forms.Textarea)
    parsing_patterns = forms.CharField(widget=forms.Textarea)
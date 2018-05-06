from django import forms
from .models import paras

class NewTopicForm(forms.ModelForm):
    #category = forms.CharField(widget=forms.Textarea(), max_length=400)
    class Meta:
        model = paras
        fields = ['name',]

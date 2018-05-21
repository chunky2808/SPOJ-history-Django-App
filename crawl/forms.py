from django import forms
from .models import ta,paras

class NewTopicForm(forms.ModelForm):
    #category = forms.CharField(widget=forms.Textarea(), max_length=400)
    class Meta:
        model = paras
        fields = ['Spoj_Handle',]

class NewTopicForm2(forms.ModelForm):
    #category = forms.CharField(widget=forms.Textarea(), max_length=400)
    class Meta:
        model = ta
        fields = ['name',]

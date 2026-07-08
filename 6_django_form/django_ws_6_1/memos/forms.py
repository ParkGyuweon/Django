from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = '__all__'
        widgets = {
            'summary': forms.TextInput(attrs={
                'placeholder': 'summary',
                'class': 'form-control',
            }),
            'memo': forms.Textarea(attrs={
                'placeholder': 'memo',
                'rows': 5,  
                'cols': 50, 
                'class': 'form-control',
            }),
        }
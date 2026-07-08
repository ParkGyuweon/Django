from django import forms
from .models import travels

class TravelForm(forms.ModelForm):
    class Meta:
        model = travels
        fields = '__all__'
        widgets = {
                'location': forms.TextInput(attrs={
                    'placeholder': '제주도',
                }),
                'start_date': forms.DateInput(attrs={
                    'placeholder': '2022-02-22',
                }),
                'end_date': forms.DateInput(attrs={
                    'placeholder': '2022-02-22',
                }),
            }
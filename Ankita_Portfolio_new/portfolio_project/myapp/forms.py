from django.forms import forms
from .models import Contact
class resumeform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['Your_Name','Your_Email','Your_Subject','Your_Message']

        # widgets={
        #     'Your_Name':forms.TextInput(attrs={'class':'form-control' }),
        #     'Your_Email ': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'Your_Subject': forms.TextInput(attrs={'class':'form-control' }),
        #     'Your_Message':forms.TextInput(attrs={'class':'form-control' }),
        # }
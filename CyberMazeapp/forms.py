from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'description']

        # Add widgets to customize the fields (e.g., placeholders)
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email', 
                'class': 'form-control', 
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter the subject', 
                'class': 'form-control', 
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter your message', 
                'class': 'form-control', 
                'rows': 5, 
                'required': True
            }),
        }



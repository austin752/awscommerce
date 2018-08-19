from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'form-full-name',
                'placeholder':'Your name'
            }))
    email    = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form-email',
                'placeholder': 'Your email'
            }))
    content  = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'form-content',
                'placeholder': 'Your message'
            }))

    def clean_email(self):
        """

        :return:
        """
        email = self.cleaned_data.get('email')
        if not 'gmail' in email:
            raise forms.ValidationError('emali not correct')
        return email





from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-username',
                'placeholder': 'Your name'
            }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-password',
                'placeholder': 'Your password'
            }))


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'form-username',
                'placeholder': 'Your name'
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'form-email',
                'placeholder': 'Your email'
            }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-password',
                'placeholder': 'Your password'
            }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'form-password2',
                'placeholder': 'Your password again'
            }))

    def clean_username(self):
        """

        :return:
        """
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username already taken.')
        return username

    def clean_email(self):
        """

        :return:
        """
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email already taken.')
        return email

    def clean_data(self):
        """

        :return:
        """
        data = self.clean_data
        password = self.clean_data.get('password')
        password2 = self.clean_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match')
        return data

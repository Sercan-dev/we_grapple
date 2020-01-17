import datetime

from django import forms
from django.contrib.auth.models import User

from .models import Post


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username eingeben')
    password = forms.CharField(min_length=6, max_length=35, label='Passwort eingeben', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email eingeben')


def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.filter(username__iexact=username).exists():
        raise forms.ValidationError('Diesen Usernamen gibt es schon')
    return username


def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email__iexact=email).exists():
        raise forms.ValidationError('Diese Email gibt es schon')
    return email


class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username eingeben')
    password = forms.CharField(min_length=6, max_length=35, label='Passwort eingeben', widget=forms.PasswordInput)



YEAR_CHOICES = tuple([2000+i for i in range(22)])

class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label = "",
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'id':'id_title',
            'placeholder': "article title",
            'label':''
            }))


    timestamp = forms.DateField(
        label='Select Publish Date',
        initial = datetime.datetime.now(),
        widget=forms.SelectDateWidget(
            attrs={
                'class':'form-control',
                },
            years=YEAR_CHOICES)
    )

    content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'id':'id_content',
                'rows':10,
                'placeholder': "article body",
                'label':''
                }))

    class Meta:
        model = Post
        fields = [
        'title',
        'content',
        'timestamp',
        ]
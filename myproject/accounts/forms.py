from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .models import UserProfile


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    class Meta:
        model = User


def create_userprofile(instance):
    # Salva slug
    fullname = '{} {}'.format(
        instance.first_name,
        instance.last_name
    )
    if fullname.strip():
        slug = slugify(fullname)
    else:
        slug = slugify(instance.email)
    # Cria UserProfile
    userprofile, _ = UserProfile.objects.get_or_create(
        user=instance,
        slug=slug
    )


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        # https://stackoverflow.com/a/3929671
        instance = super(RegisterForm, self).save(commit=False)
        # Salva username = email
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
            # Cria UserProfile
            create_userprofile(instance)
        return instance

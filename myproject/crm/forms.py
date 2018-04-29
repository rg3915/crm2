from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .models import Customer


# class UserAdminCreationForm(UserCreationForm):
# Sem senha definida
class UserAdminCreationForm(forms.ModelForm):
    ''' Cadastro geral de User '''
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        # username = email
        self.cleaned_data['username'] = email
        return email

    def save(self, commit=True):
        instance = super(UserAdminCreationForm, self).save(commit=False)
        # Salva username = email
        instance.username = self.cleaned_data['email']
        if commit:
            instance.save()
            # Cria Customer
            create_customer(instance)
        return instance


def create_customer(instance):
    # Salva slug
    fullname = '{} {}'.format(
        instance.first_name,
        instance.last_name
    )
    if fullname.strip():
        slug = slugify(fullname)
    else:
        slug = slugify(instance.email)
    # Cria Customer
    customer, _ = Customer.objects.get_or_create(
        user=instance,
        # slug=slug,
        person_type='c'
    )


class CustomerUpdateForm(forms.ModelForm):
    slug = forms.SlugField(disabled=True)

    class Meta:
        model = Customer
        fields = (
            'slug',
            'photo',
            'cpf',
            'rg',
            'cnpj',
            'ie',
            'birthday',
            'department',
            'info',
            'occupation',
            'address',
            'address_number',
            'complement',
            'district',
            'city',
            'uf',
            'cep',
        )

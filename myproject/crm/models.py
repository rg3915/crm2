from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, reverse_lazy
from myproject.core.models import TimeStampedModel, Address, Document, Active
from myproject.utils.lists import PHONE_TYPE, PERSON_TYPE, DEPARTMENT
from .managers import PersonManager, CustomerManager


class People(TimeStampedModel, Address, Document, Active):
    ''' Tabela base de pessoas '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    photo = models.ImageField('foto', null=True, blank=True)
    birthday = models.DateField('nascimento', null=True, blank=True)
    department = models.CharField(
        'departamento',
        max_length=3,
        choices=DEPARTMENT,
        null=True,
        blank=True
    )
    info = models.TextField('informações', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('user__first_name',)

    def __str__(self):
        return self.user.get_full_name()

    full_name = property(__str__)


class Person(People):
    person_type = models.CharField(
        'usuário, cliente ou fornecedor',
        max_length=1,
        choices=PERSON_TYPE,
        default='u'
    )
    occupation = models.ForeignKey(
        'Occupation',
        verbose_name='cargo',
        related_name='person_occupation',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    objects = PersonManager()

    def get_absolute_url(self):
        pass
        # return r('crm:person_detail', slug=self.slug)


class Phone(models.Model):
    phone = models.CharField('telefone', max_length=20, null=True, blank=True)
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        related_name='persons'
    )
    phone_type = models.CharField(
        'tipo',
        max_length=3,
        choices=PHONE_TYPE,
        default='pri'
    )


class Customer(Person):
    objects = CustomerManager()

    class Meta:
        proxy = True
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def get_absolute_url(self):
        return reverse_lazy('crm:customer_detail', kwargs={'pk': self.pk})

    @property
    def list_url(self):
        return reverse('crm:customer_list')

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:customer_update', kwargs=kw)
        return None

    @property
    def delete_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('crm:customer_delete', kwargs=kw)
        return None

    # def save(self, *args, **kwargs):
    #     # Update person_type
    #     self.person_type = 'c'
    #     super(Customer, self).save(*args, **kwargs)


class Occupation(models.Model):
    occupation = models.CharField('cargo', max_length=50, unique=True)

    class Meta:
        ordering = ('occupation',)
        verbose_name = 'cargo'
        verbose_name_plural = 'cargos'

    def __str__(self):
        return self.occupation

from django.db import models


class PersonManager(models.Manager):

    def get_queryset(self):
        return super(PersonManager, self).get_queryset().filter(person_type='u')


class CustomerManager(models.Manager):

    def get_queryset(self):
        return super(CustomerManager, self).get_queryset().filter(person_type='c')

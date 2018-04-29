from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from myproject.crm.models import Person, Occupation


class UserProfile(Person):
    pass

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ('user__first_name',)

    # def save(self):
    #     self.fullname = '{} {}'.format(
    #         self.user.first_name,
    #         self.user.last_name
    #     )
    #     if self.fullname.strip():
    #         self.slug = slugify(self.fullname)
    #     else:
    #         self.slug = slugify(self.user.username)
    #     super(UserProfile, self).save()

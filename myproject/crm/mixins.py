from django.urls import reverse_lazy


class SuccessUrlMixin(object):

    def get_success_url(self):
        obj, _ = self.model_name.objects.get_or_create(
            user=self.object,
        )
        kw = {'pk': obj.pk}
        return reverse_lazy(self.my_success_url, kwargs=kw)

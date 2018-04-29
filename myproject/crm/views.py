from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from myproject.core.actions import _delete
from myproject.core.mixins import ActiveMixin
from .models import Customer
from .forms import UserAdminCreationForm, CustomerUpdateForm
from .mixins import SuccessUrlMixin


def customer_delete(request, pk):
    _delete(Customer, pk)
    return HttpResponseRedirect(reverse_lazy('crm:customer_list'))


class CustomerList(ActiveMixin, ListView):
    model = Customer


class CustomerDetail(DetailView):
    model = Customer


class CustomerCreate(SuccessUrlMixin, CreateView):
    model = User
    form_class = UserAdminCreationForm
    template_name = 'crm/customer_form.html'
    model_name = Customer
    my_success_url = 'crm:customer_update'


class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerUpdateForm
    template_name = 'crm/customer_form.html'
    success_url = reverse_lazy('crm:customer_list')

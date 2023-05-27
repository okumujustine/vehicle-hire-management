from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from django.shortcuts import render
from common.models import Currency
from company.models import Company
from order.forms import OrderForm

from order.models import Order


def order_list(request):
    return render(request, "order/order_list.html", context={})


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(company=self.request.current_company).order_by('id')
        return queryset


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_create.html'
    success_url = reverse_lazy('order_app:order_list_url')

    def form_valid(self, form):
        company = Company.objects.get(id=self.request.company_id)
        form.instance.company = company

        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        currency = Currency.objects.get(code='UGX')
        form.instance.currency = currency
        messages.info(self.request, "Order created successfully")
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_update.html'
    success_url = reverse_lazy('order_app:order_list_url')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

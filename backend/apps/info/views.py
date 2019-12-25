from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from . import models, forms


@method_decorator(login_required, name='dispatch')
class OrganizationListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Organization.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OrganizationListView, self).get_context_data(**kwargs)
        context['fields'] = models.Organization._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class GoodsListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Goods.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data(**kwargs)
        context['fields'] = models.Goods._meta.get_fields()
        return context


@method_decorator(login_required, name='dispatch')
class TransportListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Transport.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TransportListView, self).get_context_data(**kwargs)
        context['fields'] = models.Transport._meta.get_fields()
        return context

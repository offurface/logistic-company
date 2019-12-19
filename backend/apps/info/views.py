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
    #template_name = "info/organization/organization_list.html"
    queryset = models.Organization.objects.all()
    paginate_by = 7


@method_decorator(login_required, name='dispatch')
class GoodsListView(ListView):
    #template_name = "info/goods/goods_list.html"
    queryset = models.Goods.objects.all()
    paginate_by = 7

@method_decorator(login_required, name='dispatch')
class TransportListView(ListView):
    #template_name = "info/transport/transport_list.html"
    queryset = models.Transport.objects.all()
    paginate_by = 7

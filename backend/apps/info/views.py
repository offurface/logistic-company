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
    View,
)
from . import models, forms
from docxtpl import DocxTemplate
from config.settings import TEMPLATES_DIR, PUBLIC_DIR

@method_decorator(login_required, name='dispatch')
class Test(View):
    template_name = "universal/docx-create.html"

    def get(self, request, *args, **kwargs):
        doc = DocxTemplate(TEMPLATES_DIR+"\docx\goods-list.docx")

        context = {
            'items': models.Goods.objects.all(),
        }
        doc.render(context)
        doc.save(PUBLIC_DIR+"\static\list-result.docx")

        return render(request, self.template_name, {
            'items': [],
            'title': 'Готово',
        })
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

@method_decorator(login_required, name='dispatch')
class DriverListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Driver.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DriverListView, self).get_context_data(**kwargs)
        context['fields'] = models.Driver._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class AdresListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Adres.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AdresListView, self).get_context_data(**kwargs)
        context['fields'] = models.Adres._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class ExecutorPersonListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ExecutorPerson.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExecutorPersonListView, self).get_context_data(**kwargs)
        context['fields'] = models.ExecutorPerson._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class ExecutorLegalListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ExecutorLegal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExecutorLegalListView, self).get_context_data(**kwargs)
        context['fields'] = models.ExecutorLegal._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class ClientPersonListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ClientPerson.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ClientPersonListView, self).get_context_data(**kwargs)
        context['fields'] = models.ClientPerson._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class ClientLegalListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ClientLegal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ClientLegalListView, self).get_context_data(**kwargs)
        context['fields'] = models.ClientLegal._meta.get_fields()
        return context

@method_decorator(login_required, name='dispatch')
class TariffListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Tariff.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TariffListView, self).get_context_data(**kwargs)
        context['fields'] = models.Tariff._meta.get_fields()
        return context



@method_decorator(login_required, name='dispatch')
class OrganizationDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Organization.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Organization, pk=pk_)

@method_decorator(login_required, name='dispatch')
class GoodsDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Goods.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Goods, pk=pk_)

@method_decorator(login_required, name='dispatch')
class TransportDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Transport.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Transport, pk=pk_)

@method_decorator(login_required, name='dispatch')
class DriverDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Driver.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Driver, pk=pk_)

@method_decorator(login_required, name='dispatch')
class AdresDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Adres.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Adres, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ExecutorPersonDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.ExecutorPerson.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ExecutorPerson, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ExecutorLegalDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.ExecutorLegal.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ExecutorLegal, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ClientPersonDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.ClientPerson.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ClientPerson, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ClientLegalDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.ClientLegal.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ClientLegal, pk=pk_)

@method_decorator(login_required, name='dispatch')
class TariffDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Tariff.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Tariff, pk=pk_)




@method_decorator(login_required, name='dispatch')
class OrganizationCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.OrganizationForm
    queryset = models.Organization.objects.all()
    success_url = "/info/organization/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class GoodsCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.GoodsForm
    queryset = models.Goods.objects.all()
    success_url = "/info/goods/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TransportCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.TransportForm
    queryset = models.Transport.objects.all()
    success_url = "/info/transport/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DriverCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.DriverForm
    queryset = models.Driver.objects.all()
    success_url = "/info/driver/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AdresCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.AdresForm
    queryset = models.Adres.objects.all()
    success_url = "/info/adres/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ExecutorPersonCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.ExecutorPersonForm
    queryset = models.ExecutorPerson.objects.all()
    success_url = "/info/executor-person/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ExecutorLegalCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.ExecutorLegalForm
    queryset = models.ExecutorLegal.objects.all()
    success_url = "/info/executor-legal/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ClientPersonCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.ClientPersonForm
    queryset = models.ClientPerson.objects.all()
    success_url = "/info/client-person/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ClientLegalCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.ClientLegalForm
    queryset = models.ClientLegal.objects.all()
    success_url = "/info/client-legal/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TariffCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.TariffForm
    queryset = models.Tariff.objects.all()
    success_url = "/info/tariff/"

    def form_valid(self, form):
        return super().form_valid(form)

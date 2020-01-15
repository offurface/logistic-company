from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
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

#API
from rest_framework import generics
from . import serializers

## TransportFull API ##
@method_decorator(login_required, name='dispatch')
class TransportFullCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TransportFullSerializer

@method_decorator(login_required, name='dispatch')
class TransportFullListAPIView(generics.ListAPIView):
    serializer_class = serializers.TransportFullSerializer
    queryset = models.TransportFull.objects.all()

@method_decorator(login_required, name='dispatch')
class TransportFullDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TransportFullSerializer
    queryset = models.TransportFull.objects.all()

## GoodsCount API ##
@method_decorator(login_required, name='dispatch')
class GoodsCountCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.GoodsCountSerializer

@method_decorator(login_required, name='dispatch')
class GoodsCountListAPIView(generics.ListAPIView):
    serializer_class = serializers.GoodsCountSerializer
    queryset = models.GoodsCount.objects.all()

@method_decorator(login_required, name='dispatch')
class GoodsCountDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GoodsCountSerializer
    queryset = models.GoodsCount.objects.all()

## Address API ##
@method_decorator(login_required, name='dispatch')
class AddressCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.AddressSerializer

@method_decorator(login_required, name='dispatch')
class AddressListAPIView(generics.ListAPIView):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()


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


## Заказы  клиентов ##
## OrderClient CRUD ##
@method_decorator(login_required, name='dispatch')
class OrderClientListView(ListView):
    #template_name = "info/order-client/order-client-list.html"
    template_name = "universal/list-view.html"
    queryset = models.OrderClient.objects.all()
    success_url = "/info/order-client/"

    def get_context_data(self, **kwargs):
        context = super(OrderClientListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.OrderClient._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)

        return context

@method_decorator(login_required, name='dispatch')
class OrderClientDetailView(DetailView):
    template_name = "info/order-client/order-client-detail.html"
    queryset = models.OrderClient.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OrderClientDetailView, self).get_context_data(**kwargs)
        context['transport_full'] =  models.TransportFull.objects.filter(order_client_id=self.object.pk)
        context['GoodsCountForm'] = forms.GoodsCountForm
        context['TransportFullForm'] = forms.TransportFullForm

        return context

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.OrderClient, pk=pk_)

@method_decorator(login_required, name='dispatch')
class OrderClientCreateView(CreateView):
    template_name = "info/order-client/order-client-create.html"
    form_class = forms.OrderClientForm
    queryset = models.OrderClient.objects.all()
    #success_url = "/info/organization/"

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class OrderClientUpdateView(UpdateView):
    template_name = "info/order-client/order-client-create.html"
    form_class = forms.OrderClientForm
    queryset = models.OrderClient.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.OrderClient, pk=pk_)

@method_decorator(login_required, name='dispatch')
class OrderClientDeleteView(DeleteView):
    template_name = "universal/delete-view.html"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.OrderClient, pk=pk_)

    def get_success_url(self):
        return reverse("info:order-client-list")

## Справочники ListView       ##
## "universal/list-view.html" ##
@method_decorator(login_required, name='dispatch')
class OrganizationListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Organization.objects.all()

    def get_context_data(self, **kwargs):
        context = super(OrganizationListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.Organization._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class GoodsListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Goods.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.Goods._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class TransportListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Transport.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TransportListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.Transport._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class DriverListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Driver.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DriverListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.Driver._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class AddressListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Address.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AddressListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.Address._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class AddressMapView(ListView):
    template_name = "info/address/address-map.html"
    queryset = models.Address.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AddressMapView, self).get_context_data(**kwargs)
        return context

@method_decorator(login_required, name='dispatch')
class ExecutorPersonListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ExecutorPerson.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExecutorPersonListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.ExecutorPerson._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class ExecutorLegalListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ExecutorLegal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExecutorLegalListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.ExecutorLegal._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class ClientPersonListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ClientPerson.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ClientPersonListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.ClientPerson._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class ClientLegalListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.ClientLegal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ClientLegalListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.ClientLegal._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context

@method_decorator(login_required, name='dispatch')
class TariffListView(ListView):
    template_name = "universal/list-view.html"
    queryset = models.Tariff.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TariffListView, self).get_context_data(**kwargs)
        context['fields'] = []
        for f in models.Tariff._meta.get_fields():
            if hasattr(f, 'verbose_name'):
                context['fields'].append(f.verbose_name)
        return context


## Справочники DetailView       ##
## "universal/detail-view.html" ##
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
class AddressDetailView(DetailView):
    template_name = "universal/detail-view.html"
    queryset = models.Address.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Address, pk=pk_)

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




## Справочники CreateView       ##
## "universal/detail-create.html" ##
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
class AddressCreateView(CreateView):
    template_name = "universal/create-view.html"
    form_class = forms.AddressForm
    queryset = models.Address.objects.all()
    success_url = "/info/address/"

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




## Справочники DeleteView       ##
## "universal/detail-create.html" ##
@method_decorator(login_required, name='dispatch')
class OrganizationDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Organization, pk=pk_)

@method_decorator(login_required, name='dispatch')
class GoodsDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Goods, pk=pk_)

@method_decorator(login_required, name='dispatch')
class TransportDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Transport, pk=pk_)

@method_decorator(login_required, name='dispatch')
class DriverDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Driver, pk=pk_)

@method_decorator(login_required, name='dispatch')
class AddressDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Address, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ExecutorPersonDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ExecutorPerson, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ExecutorLegalDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ExecutorLegal, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ClientPersonDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ClientPerson, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ClientLegalDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ClientLegal, pk=pk_)

@method_decorator(login_required, name='dispatch')
class TariffDeleteView(DeleteView):
    template_name = "universal/delete-view.html"
    success_url = "../../"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Tariff, pk=pk_)






@method_decorator(login_required, name='dispatch')
class OrganizationUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.OrganizationForm
    queryset = models.Organization.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Organization, pk=pk_)

@method_decorator(login_required, name='dispatch')
class GoodsUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.GoodsForm
    queryset = models.Goods.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Goods, pk=pk_)

@method_decorator(login_required, name='dispatch')
class TransportUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.TransportForm
    queryset = models.Transport.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Transport, pk=pk_)

@method_decorator(login_required, name='dispatch')
class DriverUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.DriverForm
    queryset = models.Driver.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Driver, pk=pk_)

@method_decorator(login_required, name='dispatch')
class AddressUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.AddressForm
    queryset = models.Address.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Address, pk=pk_)

@method_decorator(login_required, name='dispatch')
class DriverUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.DriverForm
    queryset = models.Driver.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Driver, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ExecutorLegalUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.ExecutorLegalForm
    queryset = models.ExecutorLegal.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ExecutorLegal, pk=pk_)

@method_decorator(login_required, name='dispatch')
class ClientLegalUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.ClientLegalForm
    queryset = models.ClientLegal.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.ClientLegal, pk=pk_)

@method_decorator(login_required, name='dispatch')
class TariffUpdateView(UpdateView):
    template_name = "universal/create-view.html"
    form_class = forms.TariffForm
    queryset = models.Tariff.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(models.Tariff, pk=pk_)

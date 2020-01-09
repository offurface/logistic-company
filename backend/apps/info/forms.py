from django import forms
from . import models

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ('__all__')

class GoodsForm(forms.ModelForm):
    class Meta:
        model = models.Goods
        fields = ('__all__')

class TransportForm(forms.ModelForm):
    class Meta:
        model = models.Transport
        fields = ('__all__')

class DriverForm(forms.ModelForm):
    class Meta:
        model = models.Driver
        fields = ('__all__')

class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = ('__all__')

class ExecutorPersonForm(forms.ModelForm):
    class Meta:
        model = models.ExecutorPerson
        fields = ('__all__')

class ExecutorLegalForm(forms.ModelForm):
    class Meta:
        model = models.ExecutorLegal
        fields = ('__all__')

class ClientPersonForm(forms.ModelForm):
    class Meta:
        model = models.ClientPerson
        fields = ('__all__')

class ClientLegalForm(forms.ModelForm):
    class Meta:
        model = models.ClientLegal
        fields = ('__all__')


class TariffForm(forms.ModelForm):
    class Meta:
        model = models.Tariff
        fields = ('__all__')




class TransportFullForm(forms.ModelForm):
    class Meta:
        model = models.TransportFull
        exclude = ['order_client',]

class GoodsCountForm(forms.ModelForm):
    class Meta:
        model = models.GoodsCount
        fields = ('__all__')

class OrderClientForm(forms.ModelForm):
    class Meta:
        model = models.OrderClient
        exclude = ['executor_person','client_person']

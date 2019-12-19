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
class AdresForm(forms.ModelForm):
    class Meta:
        model = models.Adres
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

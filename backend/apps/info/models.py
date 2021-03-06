from django.db import models
from django.urls import reverse


#  Организации
class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Organization._meta.fields]

    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:organization-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

#  Товары
class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    weight = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Вес (кг.)")
    x = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Ширина (м.)")
    y = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Длинна (м.)")
    z = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Высота (м.)")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Goods._meta.fields]

    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:goods-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

#  Транспорт
class Transport(models.Model):
    mark = models.CharField(max_length=100, verbose_name="Наименование")
    number = models.CharField(max_length=10, verbose_name="Номер", default="")
    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Transport._meta.fields]

    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:transport-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.mark

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспортные средства"

#  Водители
class Driver(models.Model):
    DRIVERS_LICENSE = [
        ('A','A'),
        ('A1','A1'),
        ('B','B'),
        ('B1','B1'),
        ('C','C'),
        ('C1','C1'),
        ('D','D'),
        ('D1','D1'),
        ('BE','BE'),
        ('CE','CE'),
        ('C1E','C1E'),
        ('DE','DE'),
        ('D1E','D1E'),
        ('M','M'),
        ('Tm','Tm'),
        ('Tb','Tb'),
    ]
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    category = models.CharField(max_length=4, choices=DRIVERS_LICENSE, null=True, blank=True, default=None, verbose_name="Категория")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Driver._meta.fields]

    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:driver-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

#  Населенные пункты
class Address(models.Model):
    label = models.CharField(max_length=255, verbose_name="Адрес", default="")
    street = models.CharField(max_length=255, verbose_name="Адрес", default="")
    lat = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True, verbose_name="Широта")
    lon = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True, verbose_name="Долгота")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Address._meta.fields]
    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:аdres-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.label
    class Meta:
        verbose_name = "Населенные пункт"
        verbose_name_plural = "Населенные пункты"

# Исполнители Base
class Executor(models.Model):
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    mail = models.CharField(max_length=100, verbose_name="Электронная почта", blank=True, null=True)

    def __str__(self):
        return self.name
# Слиенты Base
class Client(models.Model):
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    mail = models.CharField(max_length=100, verbose_name="Электронная почта", blank=True, null=True)

    def __str__(self):
        return self.name

#  Исполнители частные лица
class ExecutorPerson(Executor):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ExecutorPerson._meta.fields]

    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:executor-person-detail', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

#  Исполнители юридические лица
class ExecutorLegal(Executor):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ExecutorLegal._meta.fields]

    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:executor-legal-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

#  Клиенты (физ. лица)
class ClientPerson(Client):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.CharField(max_length=255, verbose_name="ИНН")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ClientPerson._meta.fields]
    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:client-person-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

#  Клиенты (юр лица)
class ClientLegal(Client):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.CharField(max_length=255, verbose_name="ИНН")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ClientLegal._meta.fields]
    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:client-legal-detail', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

#  Тарифы
class Tariff(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0, verbose_name="Цена")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Tariff._meta.fields]
    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:tariff-detail', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

#  Заказ клиента
class OrderClient(models.Model):
    STATE_ORDER = [
        (1, 'На согласовании'),
        (2, 'В работе'),
        (3, 'Выполнен'),
        (3, 'Отказ клиента'),
    ]

    date =  models.DateTimeField(
        verbose_name="Дата добавления"
        )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Организация"
        )

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Клиент")
    executor = models.ForeignKey(Executor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Исполнитель")

    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Тариф")

    date_start =  models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата погрузки"
    )
    date_end =  models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата разгрузки",
    )
    address_start = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='order_client_start',
        verbose_name="Адрес погрузки",
    )
    address_end = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='order_client_end',
        verbose_name="Адрес разгрузки"
    )
    state = models.IntegerField(choices=STATE_ORDER, default=1, verbose_name="Состояние заказа")
    def get_absolute_url(self,*args,**kwargs):
        return reverse('info:order-client-detail', kwargs={'pk': self.pk})
    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in OrderClient._meta.fields]

    class Meta:
        verbose_name = "Заказ клиента"
        verbose_name_plural = "Заказы клиентов"

# Загруженный транспорт
class TransportFull(models.Model):
    order_client = models.ForeignKey(OrderClient, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Заказ клиента")
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Транспортные средства")
    drivers = models.ManyToManyField(Driver, blank=True, verbose_name="Водители")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in TransportFull._meta.fields]

    class Meta:
        verbose_name = "Загружженый автомобиль"
        verbose_name_plural = "Загруженные автомобили"

#Колличество товара
class GoodsCount(models.Model):
    MEASURE = [
        (1, 'шт.'),
        (2, 'кг.'),
        (3, 'т.'),
    ]
    transport_full = models.ForeignKey(TransportFull, related_name='goods_count', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Загруженный транспорт")
    goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Товар")
    count = models.IntegerField(default=0, verbose_name="Количество")
    measure = models.IntegerField(choices=MEASURE, default=1, verbose_name="Еденица измерения")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in GoodsCount._meta.fields]

    class Meta:
        verbose_name = "Колличество товара"
        verbose_name_plural = "Колличество товаров"

#Путевой лист
class Waybill(models.Model):



    # def get_absolute_url(self,*args,**kwargs):
    #     return reverse('info:waybill-detail', kwargs={'pk': self.pk})

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Waybill._meta.fields]

    class Meta:
        verbose_name = "Путевой лист"
        verbose_name_plural = "Путевые листы"

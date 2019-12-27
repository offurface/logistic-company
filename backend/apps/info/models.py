from django.db import models

#  Организации
class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Organization._meta.fields]

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


#  Транспорт
class Transport(models.Model):
    mark = models.CharField(max_length=100, verbose_name="Наименование")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Transport._meta.fields]

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

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"


#  Населенные пункты
class Address(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица, № Дома")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Address._meta.fields]

    class Meta:
        verbose_name = "Населенные пункт"
        verbose_name_plural = "Населенные пункты"


#  Исполнители частные лица
class ExecutorPerson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ExecutorPerson._meta.fields]

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

#  Исполнители юридические лица
class ExecutorLegal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ExecutorLegal._meta.fields]

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

#  Клиенты (физ. лица)
class ClientPerson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.CharField(max_length=255, verbose_name="ИНН")
    phone = models.CharField(max_length=25, verbose_name="Телефон")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ClientPerson._meta.fields]

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"


#  Клиенты (юр лица)
class ClientLegal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.CharField(max_length=255, verbose_name="ИНН")
    phone = models.CharField(max_length=25, verbose_name="Телефон")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in ClientLegal._meta.fields]

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

#  Тарифы
class Tariff(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0, verbose_name="Цена")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Tariff._meta.fields]

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

    date =  models.DateTimeField(verbose_name="Дата добавления")
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Организация")

    client_legal = models.ForeignKey(ClientLegal, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Клиент")
    client_person = models.ForeignKey(ClientPerson, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Клиент")
    executor_legal = models.ForeignKey(ExecutorLegal, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Исполнитель")
    executor_person = models.ForeignKey(ExecutorPerson, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Исполнитель")

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
        related_name='OrderClientStart',
        verbose_name="Адрес погрузки",
    )
    address_end = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='OrderClientEnd',
        verbose_name="Адрес разгрузки"
    )

    state = models.IntegerField(choices=STATE_ORDER, default=1, verbose_name="Состояние заказа")

    transports = models.ManyToManyField(Transport, blank=True, verbose_name="Транспортные средства")
    goods = models.ManyToManyField(Goods, blank=True, verbose_name="Товары")
    drivers = models.ManyToManyField(Driver, blank=True, verbose_name="Водители")

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in OrderClient._meta.fields]

    class Meta:
        verbose_name = "Заказ клиента"
        verbose_name_plural = "Заказы клиентов"

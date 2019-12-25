from django.db import models

#  Организации
class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

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

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


#  Транспорт
class Transport(models.Model):
    mark = models.CharField(max_length=100, verbose_name="Наименование")

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

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"
#  Населенные пункты
class Adres(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица, № Дома")
    class Meta:
        verbose_name = "Населенные пункт"
        verbose_name_plural = "Населенные пункты"

#  Исполнители частные лица
class ExecutorPerson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

#  Исполнители юридические лица
class ExecutorLegal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

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

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

#  Тарифы
class Tariff(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0, verbose_name="Цена")

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

from django.db import models

#  Организации
class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

#  Клиенты
class Client(models.Model):
    address = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)


#  Товары
class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    weight = models.DecimalField(verbose_name="Вес")
    x = models.DecimalField(verbose_name="Ширина")
    y = models.DecimalField(verbose_name="Длинна")
    z = models.DecimalField(verbose_name="Высота")


#  Транспорт
class Transport(models.Model):
    mark = models.CharField(max_length=100, verbose_name="Наименование")

#  Водители
class Driver(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")

#  Населенные пункты
class Locality(models.Model):
    name = models.CharField(max_length=100)

#  Исполнители частные лица
class ExecutorPerson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")


#  Исполнители юридические лица
class ExecutorLegal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

#  Тарифы
class Tariff(models.Model):
    name = models.CharField(max_length=50)

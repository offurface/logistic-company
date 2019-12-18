from django.db import models

#  Организации 
class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")

    
#  Товары
class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    weight = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Вес (кг.)")
    x = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Ширина (м.)")
    y = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Длинна (м.)")
    z = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Высота (м.)")


#  Транспорт
class Transport(models.Model):
    mark = models.CharField(max_length=100, verbose_name="Наименование")

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
    category = models.CharField(max_length=4, choices=DRIVERS_LICENSE , verbose_name="Категория")

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

#  Клиенты (физ. лица)
class ClientPerson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.CharField(max_length=255, verbose_name="ИНН")
    phone = models.CharField(max_length=25, verbose_name="Телефон")

#  Клиенты (юр лица) 
class ClientLegal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сокращенное наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")    
    address = models.CharField(max_length=255, verbose_name="Адрес")
    inn = models.CharField(max_length=255, verbose_name="ИНН")
    phone = models.CharField(max_length=25, verbose_name="Телефон")    
    
#  Тарифы
class Tariff(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    price = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Цена")

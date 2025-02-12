from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField(
        'Нормализированный номер телефона',
        blank=True,
        null=True,
        region='RU'
    )
    new_building = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)
    likes = models.ManyToManyField(
        User,
        verbose_name='Кто лайкнул',
        related_name='liked_flats',
        blank=True
    )

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField(
        'Наличие балкона',
        null=True, blank=True,
        db_index=True
        )

    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'
    

class Owner(models.Model):
    full_name = models.CharField(
        "ФИО владельца",
        max_length=100,
        db_index=True
        )

    phone_number = models.CharField(
        "Номер владельца",
        max_length=20,
        db_index=True
        )

    normalized_phone = PhoneNumberField(
        "Нормализованный номер владельца",
        blank=True, null=True,
        region="RU"
        )

    flats = models.ManyToManyField(
        "Flat",
        related_name="owners",
        verbose_name="Квартиры в собственности",
        blank=True
        )

    def __str__(self):
        return self.full_name

class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Кто пожаловался",
        on_delete=models.CASCADE
    )
    flat = models.ForeignKey(
        'Flat',
        verbose_name='Квартира, на которую пожаловались',
        on_delete=models.CASCADE
    )
    text = models.TextField('Текст жалобы')
    
    def __str__(self):
        return f'{self.user}, {self.flat}'
    
    
    


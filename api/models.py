from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
        
PERCENTAGE_VALIDATOR = [MaxValueValidator(100)]


class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_name(self):
        return self.usernames
    

class Table(models.Model):
    year = models.IntegerField(default=2023)

    def __str__(self):
        return str(self.year)
    
    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'


class Month(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='months')
    order = models.IntegerField(default=1)
    period = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    rate_field = models.DecimalField(max_digits=3, decimal_places=2, validators=PERCENTAGE_VALIDATOR)

    def __str__(self):
        return self.period
    
    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'


class Estate(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='estates')
    date = models.DateTimeField('Created')
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    area = models.IntegerField(default=0)
    ceil = models.IntegerField()
    ceilings = models.IntegerField(default=5)
    description = models.TextField(max_length=1000)
    building_year = models.CharField(max_length=20, default='')
    type = models.CharField(max_length=50, default='')
    heating = models.CharField(max_length=50, default='')
    main_image = models.ImageField(upload_to = 'estate_images/', blank = True)

    def __str__(self):
        return self.title[:80]
    
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Report(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    file = models.FileField(upload_to='reports/', max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
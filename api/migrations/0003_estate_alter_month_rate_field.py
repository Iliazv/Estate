# Generated by Django 5.0.1 on 2024-05-05 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_table_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Created')),
                ('phone', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('area', models.IntegerField(default=0)),
                ('ceil', models.IntegerField()),
                ('ceilings', models.IntegerField(default=5)),
                ('description', models.TextField(max_length=1000)),
                ('building_year', models.CharField(default='', max_length=20)),
                ('type', models.CharField(default='', max_length=50)),
                ('heating', models.CharField(default='', max_length=50)),
                ('main_image', models.ImageField(blank=True, upload_to='estate_images/')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.AlterField(
            model_name='month',
            name='rate_field',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]

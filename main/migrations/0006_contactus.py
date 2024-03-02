# Generated by Django 5.0.1 on 2024-02-06 18:45

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Հասցե')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Հեռախոսահամար +374-ով սկսվող')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('linkedin', models.URLField(blank=True, verbose_name='LinkedIn')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Կոնտակտային տվյալներ',
                'verbose_name_plural': 'Կոնտակտային տվյալներ',
            },
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_pdfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video', verbose_name='Տեսանյութ')),
            ],
            options={
                'verbose_name': 'Տեսանյութ',
                'verbose_name_plural': 'Տեսանյութ',
            },
        ),
    ]

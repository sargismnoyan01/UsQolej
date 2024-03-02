# Generated by Django 5.0.1 on 2024-02-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English', '0009_enpdfiles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enpdfiles',
            options={'verbose_name': 'PDF Files', 'verbose_name_plural': 'PDF Files'},
        ),
        migrations.AlterField(
            model_name='enpdfiles',
            name='file',
            field=models.FileField(upload_to='pdf', verbose_name='pdf '),
        ),
        migrations.AlterField(
            model_name='enpdfiles',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Name'),
        ),
    ]

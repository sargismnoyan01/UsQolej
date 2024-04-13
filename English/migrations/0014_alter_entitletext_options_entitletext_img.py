# Generated by Django 5.0.1 on 2024-03-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English', '0013_entitletext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entitletext',
            options={'verbose_name': 'Main text and imagers', 'verbose_name_plural': 'Main text and imagers'},
        ),
        migrations.AddField(
            model_name='entitletext',
            name='img',
            field=models.ImageField(null=True, upload_to='main_imagers', verbose_name='main imagers'),
        ),
    ]

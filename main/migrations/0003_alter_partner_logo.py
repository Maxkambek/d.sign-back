# Generated by Django 5.0.6 on 2024-05-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_service_description_service_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]

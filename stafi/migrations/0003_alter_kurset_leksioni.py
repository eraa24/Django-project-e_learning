# Generated by Django 4.2.4 on 2023-09-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stafi', '0002_kurset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurset',
            name='leksioni',
            field=models.FileField(max_length=1000, upload_to=''),
        ),
    ]
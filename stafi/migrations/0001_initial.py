# Generated by Django 4.2.4 on 2023-08-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(max_length=255)),
                ('mbiemri', models.CharField(max_length=255)),
                ('cel', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
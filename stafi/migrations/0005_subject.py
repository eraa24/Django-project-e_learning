# Generated by Django 4.2.4 on 2023-09-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stafi', '0004_alter_kurset_kredite_alter_kurset_leksioni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
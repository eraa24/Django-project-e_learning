# Generated by Django 4.2.4 on 2023-09-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stafi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leksioni', models.FileField(max_length=2080, upload_to='')),
                ('petagogu', models.CharField(max_length=255)),
                ('kredite', models.IntegerField(max_length=10)),
            ],
        ),
    ]
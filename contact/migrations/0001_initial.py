# Generated by Django 3.2.4 on 2022-02-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_title', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('pox_title', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('tel_phone', models.IntegerField(blank=True)),
                ('mail', models.EmailField(blank=True, max_length=254)),
                ('map', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

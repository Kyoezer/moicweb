# Generated by Django 3.2.4 on 2022-02-01 06:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='select_annual_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('short_link', models.CharField(blank=True, max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='social_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SI_No', models.IntegerField(blank=True)),
                ('title', models.CharField(blank=True, max_length=400)),
                ('copy_link', models.CharField(blank=True, max_length=400)),
                ('facebook', models.CharField(blank=True, max_length=400)),
                ('whatsapp', models.CharField(blank=True, max_length=400)),
                ('email', models.CharField(blank=True, max_length=400)),
                ('telegram', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]

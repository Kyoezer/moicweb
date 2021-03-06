# Generated by Django 3.2.4 on 2022-02-01 02:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('press_title', models.CharField(max_length=100)),
                ('press_img', models.ImageField(blank=True, upload_to='pics')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('press_description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]

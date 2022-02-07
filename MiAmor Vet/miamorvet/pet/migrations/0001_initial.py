# Generated by Django 3.2.9 on 2022-02-06 11:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('genus', models.CharField(max_length=50, verbose_name='Cins')),
                ('type', models.CharField(max_length=50, verbose_name='Tür')),
                ('age', models.IntegerField(verbose_name='Yaş')),
                ('explanation', ckeditor.fields.RichTextField()),
                ('pet_image', models.FileField(blank=True, upload_to='', verbose_name='Resim Yükle')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
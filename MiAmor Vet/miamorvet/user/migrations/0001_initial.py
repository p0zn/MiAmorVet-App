# Generated by Django 3.2.9 on 2022-02-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='İsim')),
                ('last_name', models.CharField(max_length=50, verbose_name='Soyisim')),
                ('username', models.CharField(max_length=50, verbose_name='Kullanıcı Adı')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Şifre')),
                ('confirm', models.CharField(max_length=50, verbose_name='Şifreyi Onaylayın')),
            ],
        ),
    ]
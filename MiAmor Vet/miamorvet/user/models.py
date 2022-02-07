from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="İsim")
    last_name = models.CharField(max_length=50,verbose_name="Soyisim")
    username = models.CharField(max_length=50,verbose_name="Kullanıcı Adı")
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=50,verbose_name="Şifre")
    confirm = models.CharField(max_length=50,verbose_name="Şifreyi Onaylayın")


    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images')
    phone = models.CharField(max_length=11,verbose_name="Telefon")

    def __str__(self):
        return self.user.username

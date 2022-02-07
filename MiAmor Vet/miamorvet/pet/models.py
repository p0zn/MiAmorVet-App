from django.db import models
from ckeditor.fields import RichTextField


class Pet(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE, verbose_name='Yazar')
    name = models.CharField(max_length=50, verbose_name="İsim")
    type = models.CharField(max_length=50, verbose_name="Tür")
    genus = models.CharField(max_length=50, verbose_name="Cins")
    age = models.IntegerField(verbose_name="Yaş")
    explanation = RichTextField(verbose_name="Açıklama")
    pet_image = models.FileField(blank=True,null=True,verbose_name="Fotoğraf Yükle")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_date']


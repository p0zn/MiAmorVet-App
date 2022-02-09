# MiAmor Vet - Yeni Nesil Veteriner Sistemi
![](https://www.linkpicture.com/q/miamor-logo.png)



### Kurulum :
#### - Proje cmd üzerinden veya IDE üzerinden başlatılabilir.  
#### 1-CMD Üzerinden Başlatma :  
- cmd açılır.
- gerekli modüller yüklenir. (Aşağıda belirtilmiştir.)
- dosyanın olduğu dizine gidilir.
- python manage.py runserver komutu ile uygulama çalıştırılır.

![](https://www.linkpicture.com/q/cmd.png)

#### 2-IDE üzerinden başlatma :
- dosyanın olduğu dizine gidilir.
- python manage.py runserver komutu ile uygulama çalıştırılır.

## -------------------------------------------------------------------------------------------------------


### Özellikler : 

- Kullanıcı kayıt olma.
- Kullanıcı profili özelleştirme.
- Kullanıcı şifre sıfırlama.
- Kullanıcı hayvan ekleme.
- Eklenen hayvan bilgilerini güncelleme.
- Hayvan detaylarına erişebilme. 
- Hayvan silme.
- Admin özel detay sayfası (Kayıtlı tüm canlılara erişebilme).
- Yetkilendirme sistemi (Kullanıcılar kendi kayıtları üzerinde işlem yapabilir).
- Superuser tüm kayıtlara erişebilir ve değişiklik yapabilir.
- Admin paneli üzerinden değişiklik yapma.

## -------------------------------------------------------------------------------------------------------

### Gerekli Eklentiler / Komutlar
- django-ckeditor (pip install django-ckeditor)
- django-crispy-forms (pip install django-crispy-forms)
- Django (python -m pip install Django)
- Pillow (pip install Pillow)
- django-cleanup (pip install django-cleanup)

##### *modül eksikliğinde pip install [modül-adı] şeklinde yükleme yapılır.

## -------------------------------------------------------------------------------------------------------

## License


MIT

Copyright 2021 p0zn

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



from django.db import models

# Create your models here.
# My models

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Номер телефона'
    )
    img = models.ImageField(
        verbose_name='Фото',
        upload_to = 'media1'
    )
    
    img2 = models.ImageField(
        verbose_name='Фото',
        upload_to = 'media2'
    )
    video = models.URLField(
        verbose_name='Видео(YouTube)'
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "О нас"
        
class Uslugi(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
    verbose_name='Описание'        
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Услуги"
    
class Command(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    
   
    img = models.ImageField(
        verbose_name='Фото',
        upload_to = 'media3'
    )
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Команда"
    
class Contact(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    email = models.EmailField(
        verbose_name='Эл.почта'
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефонный номер'
    )
    adress = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Контакты'
        
class Commands(models.Model):
    img = models.ImageField(
        verbose_name='Фото',
        upload_to = 'media'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    job = models.CharField(
        max_length=100,
        verbose_name='Должность'
    )
    instagram = models.URLField(
        verbose_name='Инстаграм'
    )
    github = models.URLField(
        verbose_name='GitHub'
    )
    facebook = models.URLField(
        verbose_name='Фейсбук'
    )
    email = models.EmailField(
        verbose_name='Эл.почта'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Наша команда'
        
class Gallery(models.Model):
    img = models.ImageField(
        verbose_name='Фото',
        upload_to = 'media4'
    )
    
    def __str__(self):
        return f"Фото"    
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
    
class News_item(models.Model):
    img = models.ImageField(
        verbose_name='Фото',
        upload_to = 'media'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        
class Footer(models.Model):
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефонный номер'
    )
    
    about = models.TextField(
        verbose_name='Описание'
    )
    adress = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    email = models.EmailField(
        verbose_name='Эл.почта'
    )
    instagram = models.URLField(
        verbose_name='Instagram'
    )
    facebook = models.URLField(
        verbose_name='Facebook'
    )
    youtube = models.URLField(
        verbose_name='YouTube'
    )
    
    def __str__(self):
        return f"FooterAbout"
    class Meta:
        verbose_name_plural = 'Footer'
        
class Post(models.Model):
    fullname = models.CharField(
        max_length=255,
        verbose_name='Полное имя'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    date = models.CharField(
        max_length=255,
        verbose_name='Дата'
    )
    childs = models.IntegerField(
        verbose_name='Дети'
    )
    adults = models.IntegerField(
        verbose_name='Взрослые'
    )
    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name_plural = 'Заявки'

class Banner(models.Model):
    title = models.CharField(
    max_length=255,
    verbose_name='Заголовок'
    )
    id =  models.IntegerField(primary_key= True, 
    verbose_name= 'ID'
    )
    title_for_video = models.CharField(
    max_length=255, 
    verbose_name='Заголовок о видео')
    
    text = models.TextField(
    verbose_name='Текст')
    
    price = models.IntegerField(
    verbose_name='Цена')
    
    background = models.ImageField(
    upload_to='media6', 
    verbose_name='Фото')
    
    image = models.ImageField(
    upload_to='media7',
    verbose_name='Фото')
    
    image_1 = models.ImageField(
    upload_to='media7', 
    verbose_name='фото')
    
    description = models.TextField(
    verbose_name='Описание')

    def __str__(self) -> str:
        return "Баннер"
    
    class Meta:
        verbose_name_plural = 'Баннеры'

class Facilties(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Удобства'
        
class Services(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Сервисы'

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# "_API_URL" : "http://172.16.16.28/glpi/apirest.php/",
# "user_token": "aQdNykvkhbrYgZqHzbG60bKv4MIdvXox90ktcxX1",
# "app_token": "aQdNykvkhbrYgZqHzbG60bKv4MIdvXox90ktcxX1",

class PortalGlpiSettings(models.Model):
    glpi_srv_name = models.CharField(max_length=200, verbose_name="Имя", null=True)
    glpi_api_url = models.CharField(max_length=200, verbose_name="api url")
    glpi_user_token = models.CharField(max_length=200, verbose_name="user token")
    glpi_app_token = models.CharField(max_length=200, verbose_name="app token")

    def __str__(self):
        return self.glpi_srv_name

    class Meta:
        verbose_name = "Настройка"  
        verbose_name_plural = "Настройки GLPI API" 

class PortalSemaphoreSettings(models.Model):
    semaphore_srv_name = models.CharField(max_length=200, verbose_name="Имя", null=True)
    semaphore_api_url = models.CharField(max_length=200, verbose_name="api url")
    semaphore_user_login = models.CharField(max_length=200, verbose_name="user login")
    semaphore_user_password = models.CharField(max_length=200, verbose_name="user password")
    semaphore_user_token = models.CharField(max_length=200, verbose_name="user_token", null=True)

    def __str__(self):
        return self.semaphore_srv_name

    class Meta:
        verbose_name = "Настройка"  
        verbose_name_plural = "Настройки SEMAPHORE API" 



class PortalFrontSettings(models.Model):
    semaphore_srv_name = models.CharField(max_length=200, verbose_name="Имя")
    semaphore_srv_address = models.CharField(max_length=200, verbose_name="Адрес")
    semaphore_srv_user = models.CharField(max_length=200, verbose_name="Пользователь")
    semaphore_srv_priv_key_file = models.CharField(max_length=200, verbose_name="Приватный ключ")
    semaphore_srv_operator_dir = models.CharField(max_length=200, verbose_name="Папка c файлами")
    copy_files_program = models.CharField(max_length=200, verbose_name="ПО для копирования")

    def __str__(self):
        return self.semaphore_srv_name

    class Meta:
        verbose_name = "Настройка"  
        verbose_name_plural = "Настройки semaphore git" 




class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    name = models.CharField(max_length=200, verbose_name="Имя", null=True)
    body = models.TextField(verbose_name="Текст")  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заметка"  
        verbose_name_plural = "Заметки"     

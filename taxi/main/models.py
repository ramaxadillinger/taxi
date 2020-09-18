from django.db import models


class Trip(models.Model):
    phone = models.CharField('Номер телефона', max_length=13)
    destination = models.CharField('Пункт назначения', max_length=30)


    def __str__(self):
        return self.phone


    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'


class UserLogin(models.Model):
    username = models.CharField('Имя пользователя', max_length=15)
    password = models.CharField('Пароль', max_length=15)


    # def __str__(self):
    #     return self




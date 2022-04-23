from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField('名前',max_length=255)
    mail = models.EmailField('メール',max_length=255)
    male = models.BooleanField('性別')
    age = models.IntegerField('年齢',default=0)
    birthday = models.DateField('生年月日')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'おともだち'



        
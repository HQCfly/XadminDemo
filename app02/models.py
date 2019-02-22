from django.db import models

# Create your models here.


from django.db import models

# Create your models here.



class Transactions(models.Model):
    title=models.CharField(max_length=32)
    def __str__(self):
        return self.title


class Foodeat(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title
class UserInfo(models.Model):
    name=models.CharField(max_length=32,verbose_name="姓名")
    age=models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.name



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
    name=models.CharField(max_length=32)
    age=models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=32)

    def __str__(self):
        return self.title
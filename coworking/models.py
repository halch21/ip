from django.db import models

class TypeRooom(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    class Post(models.IntegerChoices):
        junior = 3, 'Младший менеджер'
        middle = 2, 'Менеджер'
        paid = 1, 'Старший менеджер'
    post = models.IntegerField(choices=Post.choices, default=Post.middle)

    
    def __str__(self):
        return self.surname

class Booking(models.Model):
    type_room = models.ForeignKey('TypeRooom', null=True, on_delete= models.PROTECT)
    date = models.DateTimeField()
    number = models.CharField(max_length=10)
    customer = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    class Periods(models.IntegerChoices):
        DAY = 1, 'День'
        THREE_DAYS = 3, 'Три дня'
        WEEK = 7, 'Неделя'
        MONTH = 30, 'Месяц'
        HALF_YEAR = 181, 'Полгода'
    period = models.IntegerField(choices=Periods.choices, default=Periods.DAY)

    def __str__(self):
        return self.number

class Order(models.Model):
    
    booking = models.ForeignKey('Booking', null=True, on_delete= models.PROTECT)
    manager = models.ForeignKey('Staff', null=True, on_delete= models.PROTECT)
    price = models.IntegerField()
    class Status(models.IntegerChoices):
        no_paid = 0, 'Не оплачен'
        paid = 1, 'Оплачен'
    status = models.IntegerField(choices=Status.choices, default=Status.no_paid)





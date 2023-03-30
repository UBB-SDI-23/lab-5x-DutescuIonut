from django.db import models


class CarBrand(models.Model):
    CarBrand = models.CharField(max_length=200)
    Founded = models.CharField(max_length=200)
    CEO = models.CharField(max_length=100)
    NumberOfEmployees = models.IntegerField(default=1)
    NetIncome = models.CharField(max_length=100)

    def __str__(self):
        return self.CarBrand


class Owner(models.Model):
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    CNP = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)

    def __str__(self):
        return self.CNP


class CarWorkshop(models.Model):
    Name = models.CharField(max_length=200)
    Owner = models.CharField(max_length=200)
    Founded = models.IntegerField(default=0)
    Location = models.CharField(max_length=200)
    NumberOfEmployees = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)


class Car(models.Model):
    CarBrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars')
    CarModel = models.CharField(max_length=200)
    ProductionYear = models.IntegerField(default=1)
    SeatsNumber = models.IntegerField(default=0)
    Color = models.CharField(max_length=50)
    OwnerCNP = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return str(self.id)


class CarTunedBy(models.Model):
    CarID = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='CarID')
    CarWorkshopID = models.ForeignKey(CarWorkshop, on_delete=models.CASCADE, related_name='WorkshopID')
    DateTuned = models.CharField(max_length=200,default="as")
    TuningPrice = models.IntegerField(default=50)

    def __str__(self):
        return str(self.CarID) + " " +str(self.CarWorkshopID)





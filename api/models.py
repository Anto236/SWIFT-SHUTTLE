from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    child_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='driver_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class BusRoute(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.driver.name} - {self.school.name}"
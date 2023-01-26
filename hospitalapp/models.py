from django.db import models

# Create your models here.
class Departments(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.name

class Doctors(models.Model):
    name=models.CharField(max_length=100)
    spec=models.CharField(max_length=100)
    dep=models.ForeignKey(Departments,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr' + self.name + '-('+ self.spec +')'

class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField()
    doc=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    date=models.DateField()
    booked_on=models.DateField(auto_now=True)
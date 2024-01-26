from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='employee_photo/', null=False, blank=True)
    interception = models.BooleanField(default=False, verbose_name='Перехват')

    class Meta:
        app_label = 'employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_datetime = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Controller(models.Model):
    power_on = models.BooleanField(default=False)
    offline = models.BooleanField(default=False)
    operation_mode = models.CharField(max_length=10, choices=[
        ('normal', 'Normal'),
        ('standby', 'Standby'),
        ('custom', 'Custom'),
    ], default='normal')
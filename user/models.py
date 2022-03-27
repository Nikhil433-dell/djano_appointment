from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):

    CHOICES = (
        ("Patient", "Patient"),
        ("Doctor", "Doctor"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to="media/")
    address = models.TextField( null=True)
    type = models.CharField(choices=CHOICES, max_length=100, default="none")

    def __str__(self):
        return str(self.user.username)


class Blog(models.Model):
    CHOICES = (
        ("Mental Health", "Mental Health"),
        ("Heart Disease", "Heart Disease"),
        ("Covid19", "Covid19"),
        ("Immunization", "Immunization"),
    )

    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    category = models.CharField(choices=CHOICES, max_length=100, default="none")
    draft = models.BooleanField(default=False)
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return str(self.title)



class Appointment(models.Model):
    doctor_name = models.CharField(max_length=500)
    speciality = models.CharField(max_length=300)
    appointment_date = models.DateField()
    appointment_start_time = models.CharField(max_length=500)
    appointment_end_time = models.CharField(max_length=500)

    def __str__(self):
        return self.doctor_name
    
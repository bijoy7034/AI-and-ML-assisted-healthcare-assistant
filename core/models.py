from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=200,null=True)
    
class Medical(models.Model):
    s1 = models.CharField(max_length=200)
    s2 = models.CharField(max_length=200)
    s3 = models.CharField(max_length=200)
    s4 = models.CharField(max_length=200)
    s5 = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    medicine = models.CharField(max_length=200)
    patient = models.ForeignKey(User, related_name="patient", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    appointment = models.BooleanField(default = False)

    def __str__(self):
        return self.disease
    
class Ment(models.Model):
    approved = models.BooleanField(default=False)
    time = models.CharField(max_length=200, null=True)
    patient = models.ForeignKey(User, related_name="pat", on_delete= models.CASCADE)
    doctor = models.ForeignKey(User, related_name="dor", on_delete= models.CASCADE, null=True)
    ment_day = models.DateTimeField(null=True)
    medical = models.ForeignKey(Medical, related_name="medical", on_delete= models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.approved

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = '', default = 'profile/avator.png', blank=True)
    birth_date = models.DateField(default='None')
    region = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=254, null=True)
    country = models.CharField(max_length=255, default='')
    height = models.DecimalField(max_digits=5, decimal_places=2, null = True) 
    weight = models.DecimalField(max_digits=5, decimal_places=2, null = True)  
    blood_type = models.CharField(max_length=3 , null = True) 
    allergies = models.CharField(max_length=255, blank=True, null = True) 
    past_medical = models.CharField(max_length=255, null = True)
    family_history = models.CharField(max_length=255, null = True)
    medical_profile = models.BooleanField(default= False)
    blood_low = models.IntegerField(null =True)
    blood_high = models.IntegerField(null =True)
    medications = models.CharField(max_length=255, null = True)

    def __str__(self):
        return self.country

class Hospitals(models.Model):
    Hospital_Name = models.CharField(max_length=255, default='')
    District = models.CharField(max_length=255, default='')
    CityTown = models.CharField(max_length=255, default='')
    Pincode = models.CharField(max_length=255, default='')
    Address = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return self.Hospital_Name
    
class WeightRecord(models.Model):
    user = models.IntegerField(null = False)
    date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99 kg
    note = models.CharField(max_length=255, blank=True)  # Optional note

    class Meta:
        ordering = ['-date']  # Order records by most recent first
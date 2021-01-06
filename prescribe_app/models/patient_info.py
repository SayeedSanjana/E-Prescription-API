from django.db import models



# PATIENT'S INFORMATION
class PatientInformation(models.Model):
    l_name = models.CharField(max_length = 100, verbose_name='Last Name')
    f_name = models.CharField(max_length = 100, verbose_name='First Name')
    age = models.PositiveIntegerField(verbose_name = "Age")
    bday = models.DateField(auto_now_add = False)
    contact = models.CharField(max_length = 100, verbose_name = "Contact No.")
    email = models.EmailField(verbose_name= "Email")
    active = models.BooleanField(default = True)
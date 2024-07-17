from django.db import models

# Create your models here.


class Item(models.Model):
    last_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    civil_status = models.CharField(max_length=200, blank=True, null=True)
    citizenship = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mother_last_name = models.CharField(max_length=200, blank=True, null=True)
    mother_first_name = models.CharField(max_length=200, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=200, blank=True, null=True)
    father_last_name = models.CharField(max_length=200, blank=True, null=True)
    father_first_name = models.CharField(max_length=200, blank=True, null=True)
    father_middle_name = models.CharField(max_length=200, blank=True, null=True)
    elementary_school = models.CharField(max_length=200, blank=True, null=True)
    junior_highschool = models.CharField(max_length=200, blank=True, null=True)
    senior_highschool = models.CharField(max_length=200, blank=True, null=True)
    college_school = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return f"{self.last_name} {self.first_name}"
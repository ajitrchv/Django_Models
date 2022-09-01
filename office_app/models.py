from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class patient(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)])
    heartrate = models.IntegerField(default=72)
    
    def __str__(self):
        return f"{self.fname} {self.lname} of age {self.age} has a heartrate of {self.heartrate}bpm"
    
# patient.objects.create(fname='peru',lname='inshal',age=30) //for all in one go

# patient1 = patient(fname='peru',lname='inshal',age=30) &&&& patient1.save()

# patient.objects.bulk_create("""a list of patients as in: patient_list=[patient(fname='peru',lname='inshal',age=30),patient(fname='peru',lname='inshal',age=30)]...""") // a lot of items in one go

# patient.objects.all()  //getting all the data available in tht db

# patient.objects.get(pk=5) //getting data from object with primary key/ pk=5


#------------- Filter samples-----------------

# patient.objects.filter(lname='smith') -- can get all the patients with lastname smith

# patient.objects.filter(lname='smith').filter(age=40)


#-------------> Field LookUps <-------------------

# To use more boolean operators such as <,>,<=,>= etc

# patient.objects.filter(name__startswith="s")  --> here two underscores "__" after field name is really important before lookup function.
#                                 |_________ here startswith is a function/fieldlookup thing to chk the corresponding

                                        # |____ There are a lot of those, check documntation -- " field-lookups "
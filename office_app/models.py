from django.db import models

class patient(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.fname} {self.lname} of age {self.age}"
    
# patient.objects.create(fname='peru',lname='inshal',age=30) //for all in one go

# patient1 = patient(fname='peru',lname='inshal',age=30) &&&& patient1.save()

# patient.objects.bulk_create("""a list of patients as in: patient_list=[patient(fname='peru',lname='inshal',age=30),patient(fname='peru',lname='inshal',age=30)]...""") // a lot of items in one go

# patient.objects.all()  //getting all the data available in tht db

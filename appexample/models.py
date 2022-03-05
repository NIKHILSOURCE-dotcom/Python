from django.db import models

# Create your models here.

from django.db import models






class User(models.Model):

    Gender_choices = (
    ('male', 'Male'),
    ('female','Female')
    )


    id = models.AutoField( primary_key=True)  # Field name made lowercase.
    name = models.CharField( max_length=35)  # Field name made lowercase.
    phonenumber = models.CharField(max_length=20)  # Field name made lowercase.
    gender = models.CharField(max_length=20,choices=Gender_choices)  # Field name made lowercase.
    email = models.EmailField(db_column='Population')  # Field name made lowercase.

    

    class Meta:
        db_table = 'user'
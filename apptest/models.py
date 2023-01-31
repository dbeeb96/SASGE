from django.db import models

class person(models.Model):
    prenom= models.CharField(max_length=30)
    nom1= models.CharField(max_length=30)

class Reporter(models.Model):
    full_name= models.CharField(max_length=70)

    def _str_(self):
        return self.full_name

from django.db import models

class person(models.model):
    prenom= models.charfield(max_length=30)
    nom= models.charfield(max_length=30)

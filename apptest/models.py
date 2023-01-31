from django.db import models

<<<<<<< HEAD
class Article(models.Model):
    pub_date = models.DateField()
    headtline = models.charField(max_length=200)
    content = models.TextField()
    Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __file__(self):
        return self.headtline
=======
class person(models.Model):
    prenom= models.CharField(max_length=30)
    nom1= models.CharField(max_length=30)

class Reporter(models.Model):
    full_name= models.CharField(max_length=70)

    def _str_(self):
        return self.full_name
>>>>>>> d986e63f81fe9f8f9f68ac9e4f0bc6aa6ae75efa

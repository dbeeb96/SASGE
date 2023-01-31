from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headtline = models.charField(max_length=200)
    content = models.TextField()
    Reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __file__(self):
        return self.headtline

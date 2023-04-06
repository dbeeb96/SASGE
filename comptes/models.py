from django.db import models
from django.contrib.auth.models import User
# Create your models here.


CHOICES = (
    ('CEO', 'CEO'),
    ('Assistance', 'Assistance'),
    ('DESE', 'DESE'),
    ('DEF', 'DEF'),
    ('DIT', 'DIT'),
    ('SAIN', 'SAIN'),
    ('DICM', 'DICM'),
    ('SLO', 'SLO'),
    ('DIP', 'DIP'),
)


class company(models.Model):  # [Table of companies ]
    company_name = models.CharField(max_length=100, default='', primary_key=True)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)  # or models.CASCADE
    Jobtitle = models.CharField(max_length=100, default='', choices=CHOICES)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    company_name = models.ForeignKey(company, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

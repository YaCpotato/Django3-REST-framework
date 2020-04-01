from django.db import models

# Create your models here.
class Player(models.Model):
    JOB = (
        (0, 'No job'),
        (1, 'Fighter'),
        (2, 'Magic Caster'),
        (3, 'Priest')
    )
    name = models.CharField(max_length=8)
    hp = models.IntegerField(null=False)
    mp = models.IntegerField(null=False)
    job = models.IntegerField(max_length=3,choices=JOB)
    weapon = models.CharField(max_length=8)
    pub_date = models.DateTimeField('date published')

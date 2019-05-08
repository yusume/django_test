from django.db import models
from django.utils import timezone

# Create your models here.

class board(models.Model):
    dbcon = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=400)
    # img_file = models.ImageField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    # hits = models.integerField(null=true)

    def __str__(self):
        return  "%s - %s" %(self.title, self.contents)
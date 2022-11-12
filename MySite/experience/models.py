from django.db import models
import datetime


# Create your models here.
class Experience(models.Model):
    date_start = models.DateField(default=datetime.date.today, verbose_name="Start date")
    date_end = models.DateField(default=datetime.date.today, verbose_name="End date")
    position = models.CharField(max_length=255, verbose_name="Position")
    responsibilities = models.CharField(max_length=255, verbose_name="Responsibilities")
    stack = models.CharField(max_length=255, verbose_name="Stack", default="Python")
    company = models.CharField(max_length=255, verbose_name="Company")

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

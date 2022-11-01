from django.db import models


# Create your models here.
class PersonalInformation(models.Model):
    info = models.CharField(verbose_name='Information', max_length=255)
    data = models.CharField(verbose_name='Data', max_length=255)

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Informations'

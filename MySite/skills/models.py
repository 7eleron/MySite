from django.db import models


# Create your models here.
class Skills(models.Model):
    skill = models.CharField(verbose_name='Skill', max_length=255)
    level = models.IntegerField(verbose_name='Level')

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

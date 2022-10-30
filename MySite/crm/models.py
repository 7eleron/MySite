from django.db import models


# Create your models here.
class ImageHead(models.Model):
    myimag = models.ImageField(upload_to='myimg/')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Мое фото'
        verbose_name_plural = 'Мои фото'



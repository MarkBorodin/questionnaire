from django.db import models


class BGImage(models.Model):
    name = models.TextField(max_length=256, null=False, blank=False)
    image = models.ImageField(verbose_name='background image site', null=True, blank=True)
    image_pdf = models.ImageField(verbose_name='background image pdf (size about: 700 x 800px)', null=True, blank=True)
    image_code = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "background image"
        verbose_name_plural = "background images"

    def __str__(self):
        return str(self.name)

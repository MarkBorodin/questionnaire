from django.db import models


class EmailText(models.Model):
    name = models.TextField(max_length=256, null=False, blank=False)
    subject = models.TextField(max_length=256, null=True, blank=True, default='survey results')
    body = models.TextField(max_length=256, null=True, blank=True, default='survey results')

    class Meta:
        verbose_name = "email text"
        verbose_name_plural = "email texts"

    def __str__(self):
        return str(self.name)

from django.db import models

# Create your models here.
class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Code(models.Model):
    search_text = models.CharField(max_length=500)
    meta_text = models.CharField(max_length=500)

    def __unicode__(self):
        return self.meta_text
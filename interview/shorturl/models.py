from django.db import models
import uuid

# Create your models here.
class urlShortModel(models.Model):
    uuid = models.UUIDField('uuid', primary_key=True, default=uuid.uuid4, editable=False)
    long_url = models.CharField('long_url', max_length=400, null=False, blank=False)

from datetime import timezone

from django.db import models

from blog.models import Client


class Report(models.Model):
    title = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    brend = models.CharField(max_length=255)
    name_item = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    time_create = models.DateTimeField(blank=True, auto_now_add=True)
    time_update = models.DateTimeField(blank=True, auto_now_add=True)
    is_published = models.BooleanField(default=True)
    defect_name = models.CharField(max_length=255)
    defect_text = models.TextField()
    remarks = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_tsp = models.ImageField(upload_to='photos-tsp/%Y/%m/%d/')
    spec_dok = models.TextField()
    spec_device = models.TextField(null=True)
    inference = models.TextField()
    inspector = models.CharField(max_length=255)


    def __str__(self):
        return self.title


from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    summary = models.CharField(max_length=200)
    category = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    #foto = models.ImageField(upload_to='pfotos/%Y/%m/%d/', blank=True)#TODO
    #slug = models.SlugField(...) # todo


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
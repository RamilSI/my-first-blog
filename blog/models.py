from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    summary = models.CharField(max_length=200)
    category = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    # foto = models.ImageField(upload_to='pfotos/%Y/%m/%d/', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Schema(models.Model):
    schema = models.CharField(max_length=200)
    name = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_shcem = models.CharField(max_length=200)
    first_layer = models.CharField(max_length=200)
    dry_residue_first_layer = models.PositiveSmallIntegerField(max_length=3)
    second_layer = models.CharField(max_length=200)
    thikness_first_layer = models.PositiveSmallIntegerField(max_length=5)
    dry_residue_second_layer = models.PositiveSmallIntegerField(max_length=3)
    thikness_second_layer = models.PositiveSmallIntegerField(max_length=3)
    all_thikness = models.IntegerField(max_length=5)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})

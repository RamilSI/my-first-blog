from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# class Cat(models.Model):
#     name = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    # client_object = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(blank=True)
    summary = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    #slug = models.SlugField(blank=True, null=True)
    # cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null=True, blank=True)
    # foto = models.ImageField(upload_to='pfotos/%Y/%m/%d/', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})


# class Schema(models.Model):
#     schema = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
#     name = models.ManyToManyField(Post)
#     category_shcem = models.CharField(max_length=200)
#     first_layer = models.CharField(max_length=200)
#     dry_residue_first_layer = models.PositiveSmallIntegerField()
#     second_layer = models.CharField(max_length=200)
#     thikness_first_layer = models.PositiveSmallIntegerField()
#     dry_residue_second_layer = models.PositiveSmallIntegerField()
#     thikness_second_layer = models.PositiveSmallIntegerField()
#     all_thikness = models.IntegerField()
#     slug = models.SlugField(blank=True, null=True)
#
#     def __str__(self):
#         return self.schema

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})


# class Client(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True, default='KVOiT')
#     address = models.CharField(max_length=200, default='Самара', null=True)
#     manager = models.CharField(max_length=200, default='Manager')
#     phone_manager = models.PositiveSmallIntegerField(blank=True, null=True)
#     object = models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return self.name

#todo model_latter-to-client-in письма для обоснования предложения
#todo model_latter-to-client-out




from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError


class SubService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    subs = models.ManyToManyField(SubService, blank=True)
    icon = models.CharField(max_length=255, help_text="themify-icons name eg: car, home, user, etc", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ""
        verbose_name = "Service"
        verbose_name_plural = "Services"


class NumberData(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            if NumberData.objects.all().count() < 3:
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    class Meta:
        db_table = ""
        verbose_name = "NumberData"
        verbose_name_plural = "NumberDatas"


class Director(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to="director/")
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    message = models.TextField(null=True)
    by_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.by_name


class Email(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
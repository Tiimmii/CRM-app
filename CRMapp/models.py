from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from datetime import datetime

class Auto(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class User(AbstractUser):
    pass
    # To categorize users either as an organisor or as an agent
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    organisation = models.ForeignKey("Auto", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
       return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    organisation = models.ForeignKey("Auto", on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=15)
    user = models.ForeignKey("User", on_delete=models.CASCADE)



    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        Auto.objects.create(user = instance)

post_save.connect(post_user_created_signal, sender=User)
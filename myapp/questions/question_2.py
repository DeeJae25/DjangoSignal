# question_2.py
#Do Django signals run in the same thread as the caller?
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")


# Testing in Django Shell
from myapp.models import MyModel
import threading

print(f"Caller thread: {threading.current_thread().name}")
MyModel.objects.create(name="Test")
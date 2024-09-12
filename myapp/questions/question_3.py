# question_3.py
# Do Django signals run in the same database transaction as the caller by default?
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler triggered")
    # Forcing a transaction rollback
    raise Exception("Simulating an error in the signal handler")
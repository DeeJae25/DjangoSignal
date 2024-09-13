
# Accuknox Interview

## Hi, I am Danish Jamal

### Question 1: Are Django signals executed synchronously or asynchronously by default?

Django signals are executed **synchronously** by default. This means that when a signal is sent, all the connected signal handlers are executed in the same thread, blocking the execution until the signal handlers finish.

#### Proof Code Snippet:

```python
# question_1.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a long-running task
    print("Signal handler finished")


# Testing in Django Shell
from myapp.questions.question_1 import MyModel
import time

start_time = time.time()
MyModel.objects.create(name="Test")
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
```

#### Expected Output:

```
Signal handler started
Signal handler finished
Time taken: 5.x seconds
```

This shows that the `create()` method waits until the signal handler finishes, demonstrating synchronous execution.

---

### Question 2: Do Django signals run in the same thread as the caller?

**Yes**, Django signals run in the **same thread** as the caller by default. You can check this by printing the thread information in both the caller and the signal handler.

#### Proof Code Snippet:

```python
# question_2.py
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
from myapp.questions.question_2 import MyModel
import threading

print(f"Caller thread: {threading.current_thread().name}")
MyModel.objects.create(name="Test")
```

#### Expected Output:

```
Caller thread: MainThread
Signal handler thread: MainThread
```

Both the caller and the signal handler run in the same thread, confirming that signals execute in the same thread as the caller.

---

### Question 3: Do Django signals run in the same database transaction as the caller by default?

Yes, Django signals run in the **same database transaction** as the caller. To prove this, we can use the `post_save` signal and force a database transaction failure within the signal handler, which will cause the transaction to roll back, preventing the model from being saved.

#### Proof Code Snippet:

```python
# question_3.py
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

# Testing in Django Shell
from myapp.questions.question_3 import MyModel

try:
    MyModel.objects.create(name="Test")
except Exception as e:
    print(f"Exception caught: {e}")

# Checking if the object was created
print(MyModel.objects.filter(name="Test").exists())
```

#### Expected Output:

```
Signal handler triggered
Exception caught: Simulating an error in the signal handler
False
```

The object does not get created because the signal handler raised an exception, causing the entire transaction to roll back. This confirms that signals run in the same transaction as the caller by default.


### You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the `Rectangle` class requires `length:int` and `width:int` to be initialized.
2. We can iterate over an instance of the `Rectangle` class.
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: `{'length': <VALUE_OF_LENGTH>}` followed by the width `{width: <VALUE_OF_WIDTH>}`


```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = int(length)
        self.width = int(width)

        # Check if length is greater than width
        if self.length <= self.width:
            raise ValueError("Length must be greater than width")

    # Define the __iter__ method to make the class iterable
    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

x, y = input("Enter two values (length width): ").split()
rect = Rectangle(x, y)

# Iterate over the Rectangle object
for item in rect:
    print(item)
```

### Test case:

#### Case 1:
```bash
Enter two values (length width): 10 5
{'length': 10}
{'width': 5}
```

#### Case 2:
```bash
Enter two values (length width): 5 11
ValueError: Length must be greater than width
```



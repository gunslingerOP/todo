from django.db import models

class OnlyActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)   
    
    
     
class Task(models.Model):
    title = models.TextField("Title")
    creationDate =  models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    active= OnlyActiveManager()
    objects = models.Manager()

    def __str__(self):
        return self.name
    class Meta:
         ordering = ['-creationDate']
    
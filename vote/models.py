from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    bio=models.TextField(default="no bio")       

    def __str__(self):
        return f'{self.bio} ' #show how we want it to be displayed 
    
class candidates(models.Model):
    candidate=models.OneToOneField(User,on_delete=models.CASCADE)   


    
class votes_candidate(models.Model):
    voter= models.OneToOneField(User, on_delete=models.CASCADE )
    candidate=models.ForeignKey(candidates,on_delete=models.CASCADE)
   

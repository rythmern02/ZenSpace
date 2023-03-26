from django.db import models
from django.contrib.auth.models import User


class ClubMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # club = models.ForeignKey('', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # return f"{self.user.username} - {self.club.name} - {self.timestamp}"

class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='clubs/', blank=True)
    members = models.ManyToManyField(User)
    messages = models.ManyToManyField(ClubMessage, related_name='clubs')


    def __str__(self):
        return self.name
    
    def des(self):
        return self.description

class ClubMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.club.name}"



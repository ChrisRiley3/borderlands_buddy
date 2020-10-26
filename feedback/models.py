from django.db import models
from profiles.models import UserProfile


class Feedback(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False,
                             on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    feedback = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.feedback

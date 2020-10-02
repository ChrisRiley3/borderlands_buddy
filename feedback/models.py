from django.db import models


class Feedback(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    feedback = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User


class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_created=True)


class Choice(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, blank=True)


class Vote(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    time = models.DateField(auto_created=True, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'title',)

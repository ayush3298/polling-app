from django.db import models


class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_created=True)


class Choice(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, blank=True)

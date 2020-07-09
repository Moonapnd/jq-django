from django.db import models

class Comment(models.Model):
    DOE1 = 'DOE1'
    DOE2 = 'DOE2'
    DOE3 = 'DOE3'
    PUBLISHER_CHOICES = ((DOE1, 'doe1'), (DOE2, 'doe2'), (DOE3, 'doe3'))

    POST1 = 'POST1'
    POST2 = 'POST2'
    POST3 = 'POST3'
    POST_CHOICES = ((POST1, 'post1'), (POST2, 'post2'), (POST3, 'post3'))

    post = models.CharField(choices=POST_CHOICES, max_length=20)
    publisher = models.CharField(choices=PUBLISHER_CHOICES, max_length=20)
    body = models.CharField(max_length=200)

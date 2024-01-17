from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo')
    about_user = models.TextField(max_length=300)

    # publication_set
    # following_set
    # followers_set

    def __str__(self):
        return f"{self.nickname}"


class Publication(models.Model):
    text_of_publication = models.TextField(max_length=1000)
    image_of_publication = models.ImageField(upload_to='images')
    owner_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publication_set")
    #like
    #comment_of_publication

    def __str__(self):
        return f"{self.text_of_publication}"
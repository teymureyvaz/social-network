from django.db import models

class Post(models.Model):
    user = models.ForeignKey()
    content = models.TextField()
    created_at =  models.DateField()
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def like_count(self):
        return self.likes.count()
from django.contrib import admin
from social.core.models import Post, LikeHistory

admin.site.register(Post)
admin.site.register(LikeHistory)

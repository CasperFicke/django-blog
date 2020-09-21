from django.contrib import admin

# Register your models here.
from .models import Post, Category, UserProfile, Comment

# registreer Post in de admin web-omgeving
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)
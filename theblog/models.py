from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date
from ckeditor.fields import RichTextField

# Category model
class Category(models.Model):
  name = models.CharField(max_length=255)

  # functie om in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.name
  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('home')
    # return reverse('post-view', args=(str(self.id)))

# Userprofile model
class UserProfile(models.Model):
  user         = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  bio          = models.TextField()
  profile_pic  = models.ImageField(null=True, blank=True, upload_to="images/profile/")
  website_url  = models.CharField(max_length=255, null=True, blank=True)
  twitter_url  = models.CharField(max_length=255, null=True, blank=True)
  facebook_url = models.CharField(max_length=255, null=True, blank=True)

  # functie om userprofile in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return str(self.user)
  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('home')


# Post model
class Post(models.Model):
  title  = models.CharField(max_length=255)
  header_image = models.ImageField(null=True, blank=True, upload_to="images/")
  # na uitbreding van model met extra veld als er al records zijn moet default worden meegegeven. kan later weer weg.
  # title_tag  = models.CharField(max_length=255, default="default tekst")
  title_tag = models.CharField(max_length=255)
  snippet   = models.CharField(max_length=255)
  author    = models.ForeignKey(User, on_delete=models.CASCADE)
  body      = RichTextField(blank=True, null=True)
  # body    = models.TextField()
  post_date = models.DateField(auto_now_add=True)
  category  = models.CharField(max_length=255, default='geen categorie')
  likes     = models.ManyToManyField(User, related_name='blog_posts')

  # functie om aantal likes te bepalen
  def total_likes(self):
    return self.likes.count()

  # functie om title en author in de admin web-pagina te kunnen presenteren
  def __str__(self):
    return self.title + ' | ' + str(self.author)

  # functie om redirect url te bepalen
  def get_absolute_url(self):
    return reverse('home')
    # return reverse('post-view', args=(str(self.id)))

# Comment model
class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  # 
  def __str__(self):
    return '%s - %s' % (self.post.title, self.name)


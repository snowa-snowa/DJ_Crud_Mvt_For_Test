from django.db import models

# One-to-One
class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    signup_date = models.DateField()

class ProfileExtra(models.Model):
    phone = models.CharField(max_length=20)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

# One-to-Many
class Blog(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField()

class Entry(models.Model):
    headline = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

# Many-to-Many
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)

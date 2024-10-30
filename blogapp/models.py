from django.core.files import File
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from PIL import Image as PilImage
from io import BytesIO
from users.models import Profile

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog-img/')
    content  = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=("authors"),on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def get_related_posts(self):
        return Blog.objects.filter(tags__in=self.tags.all()).exclude(id=self.id).distinct()
      
    def __str__(self):
        return self.title
    
    #check if blog new (created within the last day).
    def is_new(self):
        now = timezone.now().date()
        return (now - self.created_at) < timezone.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class  Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("comment_delete", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'Commented By {self.author} On Blog: {self.blog}'

class About(models.Model):
    title = models.CharField( max_length=50)
    content=  models.TextField()
    image = models.ImageField(upload_to='about/')
    background_content = models.TextField()
    teamwork_content = models.TextField()
    corevalue_content = models.TextField()
    team_members = models.ManyToManyField(Profile)
    def __str__(self):
        return "About Us" # Return a string representation of the model instance

    
class Contact(models.Model):
    map =  models.CharField(max_length=500)
    mobile = models.CharField(max_length=50)
    email =  models.EmailField()
    address = models.CharField(max_length=100)
    fblink = models.URLField(max_length=200)
    twlink = models.URLField(max_length=200)
    ytlink = models.URLField(max_length=200)
    instlink = models.URLField(max_length=200)
    
    def __str__(self):
        return "Contact Us" # Return a string representation of the model instance

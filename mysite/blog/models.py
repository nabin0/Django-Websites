from django.db import models


# Create your models here.
class Blogpost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default="")
    heading0 = models.CharField(max_length=500, default="")
    content_heading0 = models.CharField(max_length=5000, default="")
    heading1 = models.CharField(max_length=500, default="")
    content_heading1 = models.CharField(max_length=5000, default="")
    heading2 = models.CharField(max_length=500, default="")
    content_heading2 = models.CharField(max_length=5000, default="")
    thumbnail = models.ImageField(upload_to="blog/images")
    post_date = models.DateField()

    def __str__(self):
        return self.title

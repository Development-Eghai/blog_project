from django.db import models

# Create your models here.
class TeamsPost(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    content1 = models.TextField()
    content2 = models.TextField()

    def __str__(self):
        return self.name
    
class BlogDetails(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField()
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    seo_title = models.CharField(max_length=255)
    seo_description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.heading

class PostJobs(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.job_title} at {self.company}"


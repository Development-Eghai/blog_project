from django.db import models

# Create your models here.
class TeamsPost(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    position = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class BlogDetails(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    # feature_image = models.URLField()
    feature_image = models.ImageField(upload_to='uploads/')
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    seo_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    full_description = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.heading
    
class BlogComments(models.Model):
    blog_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    # feature_image = models.URLField()
    # blog_post = models.ForeignKey(BlogDetails, on_delete=models.CASCADE)
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


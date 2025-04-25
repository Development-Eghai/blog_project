from django.db import models

# Create your models here.
class TeamsPost(models.Model):
    name = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='uploads/')
    position = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class BlogPostCategory(models.Model):
    category_name = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.category
    
class BlogDetails(models.Model):
    heading = models.CharField(max_length=255,blank=True)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    # feature_image = models.URLField()
    feature_image = models.ImageField(upload_to='uploads/')
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    seo_title = models.CharField(max_length=255,blank=True)
    meta_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    meta_tag = models.CharField(max_length=255,blank=True)
    category = models.CharField(max_length=100,blank=True)
    slug_url = models.TextField(blank=True)

    def __str__(self):
        return self.heading
    
class BlogComments(models.Model):
    blog_id = models.IntegerField()
    name = models.CharField(max_length=255,blank=True)
    email_id = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    # feature_image = models.URLField()
    # blog_post = models.ForeignKey(BlogDetails, on_delete=models.CASCADE)
    def __str__(self):
        return self.heading
    


class PostJobs(models.Model):
    job_title = models.CharField(max_length=255,blank=True)
    company = models.CharField(max_length=255,blank=True)
    location = models.CharField(max_length=255,blank=True)
    job_description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    salary = models.CharField(max_length=25,blank=True)  #default='No Description'

    def __str__(self):
        return f"{self.job_title} at {self.company}"


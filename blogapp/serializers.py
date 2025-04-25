from rest_framework import serializers
from .models import TeamsPost,BlogDetails,BlogComments, PostJobs,BlogPostCategory


class TeamsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamsPost
        fields = '__all__'

class BlogPostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostCategory
        fields = '__all__'

class BlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogDetails
        fields = '__all__'

class BlogCommentsSerializer(serializers.ModelSerializer):

    # blog_post = BlogDetailsSerializer(read_only=True)
    # blog_post_id = serializers.PrimaryKeyRelatedField(queryset=BlogDetails.objects.all(), source='blog_post', write_only=True)

    class Meta:
        model = BlogComments
        fields = '__all__'

class PostJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJobs
        fields = '__all__'

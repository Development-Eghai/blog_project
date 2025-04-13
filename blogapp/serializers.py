from rest_framework import serializers
from .models import TeamsPost,BlogDetails, PostJobs


class TeamsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamsPost
        fields = '__all__'

class BlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogDetails
        fields = '__all__'

class PostJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJobs
        fields = '__all__'

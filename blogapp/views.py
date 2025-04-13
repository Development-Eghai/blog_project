from django.shortcuts import render
from rest_framework import generics
from .models import TeamsPost,BlogDetails, PostJobs
from .serializers import TeamsPostSerializer,BlogDetailsSerializer, PostJobsSerializer


class TeamsPostListCreate(generics.ListCreateAPIView):
    queryset = TeamsPost.objects.all()
    serializer_class = TeamsPostSerializer

class TeamsPostRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamsPost.objects.all()
    serializer_class = TeamsPostSerializer


class BlogDetailsListCreate(generics.ListCreateAPIView):
    queryset = BlogDetails.objects.all()
    serializer_class = BlogDetailsSerializer

class BlogDetailsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogDetails.objects.all()
    serializer_class = BlogDetailsSerializer

# CRUD for PostJobs
class PostJobsListCreate(generics.ListCreateAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobsSerializer

class PostJobsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobsSerializer


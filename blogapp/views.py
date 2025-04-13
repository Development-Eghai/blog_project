from django.shortcuts import render
from rest_framework import generics
from .models import TeamsPost,BlogDetails,BlogComments, PostJobs
from .serializers import TeamsPostSerializer,BlogDetailsSerializer,BlogCommentsSerializer, PostJobsSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status




class TeamsPostJsonUpdateDelete(APIView):
    def put(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = TeamsPost.objects.get(id=post_id)
        except TeamsPost.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamsPostSerializer(instance, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = TeamsPost.objects.get(id=post_id)
            instance.delete()
            return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        except TeamsPost.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        
class BlogPostJsonUpdateDelete(APIView):
    def put(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = BlogDetails.objects.get(id=post_id)
        except BlogDetails.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamsPostSerializer(instance, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = BlogDetails.objects.get(id=post_id)
            instance.delete()
            return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        except BlogDetails.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        
class JobPostJsonUpdateDelete(APIView):
    def put(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = PostJobs.objects.get(id=post_id)
        except PostJobs.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamsPostSerializer(instance, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = PostJobs.objects.get(id=post_id)
            instance.delete()
            return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        except PostJobs.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)


class TeamsPostListCreate(generics.ListCreateAPIView):
    queryset = TeamsPost.objects.all()
    serializer_class = TeamsPostSerializer

class TeamsPostRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamsPost.objects.all()
    serializer_class = TeamsPostSerializer


class BlogDetailsListCreate(generics.ListCreateAPIView):
    queryset = BlogDetails.objects.all()
    serializer_class = BlogDetailsSerializer

class BlogPostCommentsListCreate(generics.ListCreateAPIView):
    queryset = BlogComments.objects.all()
    serializer_class = BlogCommentsSerializer

class BlogDetailsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogDetails.objects.all()
    serializer_class = BlogDetailsSerializer

class BlogCommentsByBlog(ListAPIView):
    serializer_class = BlogCommentsSerializer

    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return BlogComments.objects.filter(blog_id=blog_id)  

# class BlogCommentsByBlog(ListAPIView):
#     serializer_class = BlogCommentsSerializer
#     def get_queryset(self):
#         blog_id = self.kwargs['blog_id']
#         return BlogComments.objects.filter(blog_id=blog_id)
    
# class BlogCommentsByBlog(ListAPIView):
#     serializer_class = BlogCommentsSerializer

#     def get_queryset(self):
#         blog_id = self.kwargs['blog_id']
#         return BlogComments.objects.filter(blog__id=blog_id)  


# class BlogCommentsRetrieveUpdateDelete(ListAPIView):
#     queryset = BlogComments.objects.all()
#     serializer_class = BlogCommentsSerializer
#     lookup_field = 'blog_id'  

# CRUD for PostJobs
class PostJobsListCreate(generics.ListCreateAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobsSerializer

class PostJobsRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobsSerializer


from django.urls import path
from .views import (TeamsPostListCreate, TeamsPostRetrieveUpdateDelete,
                    BlogDetailsListCreate, BlogDetailsRetrieveUpdateDelete,
                    PostJobsListCreate, PostJobsRetrieveUpdateDelete
                    )

urlpatterns = [
    path('teams/', TeamsPostListCreate.as_view(), name='teams-list-create'),
    path('teams/<int:pk>/', TeamsPostRetrieveUpdateDelete.as_view(), name='teams-detail'),
    path('blog_details/', BlogDetailsListCreate.as_view(), name='blog-list-create'),
    path('blog_details/<int:pk>/', BlogDetailsRetrieveUpdateDelete.as_view(), name='blog-detail'),
    path('post_jobs/', PostJobsListCreate.as_view(), name='post-jobs-list-create'),
    path('post_jobs/<int:pk>/', PostJobsRetrieveUpdateDelete.as_view(), name='post-jobs-detail'),
]

from django.urls import path
from .views import (TeamsPostListCreate, TeamsPostRetrieveUpdateDelete,TeamsPostJsonUpdateDelete,
                    BlogDetailsListCreate, BlogDetailsRetrieveUpdateDelete,BlogPostJsonUpdateDelete,
                    PostJobsListCreate, PostJobsRetrieveUpdateDelete,JobPostJsonUpdateDelete,BlogPostCommentsListCreate
                    )

urlpatterns = [
    path('teams/', TeamsPostListCreate.as_view(), name='teams-list-create'),
    path('teams/<int:pk>/', TeamsPostRetrieveUpdateDelete.as_view(), name='teams-detail'),
    path('teams_change/', TeamsPostJsonUpdateDelete.as_view(), name='teams_change'),
    path('blog_details/', BlogDetailsListCreate.as_view(), name='blog-list-create'),
    path('blog_details/<int:pk>/', BlogDetailsRetrieveUpdateDelete.as_view(), name='blog-detail'),
    path('blog_change/', BlogPostJsonUpdateDelete.as_view(), name='blog_change'),
    path('post_jobs/', PostJobsListCreate.as_view(), name='post-jobs-list-create'),
    path('post_jobs/<int:pk>/', PostJobsRetrieveUpdateDelete.as_view(), name='post-jobs-detail'),
    path('job_change/', JobPostJsonUpdateDelete.as_view(), name='post_change'),
    path('blog_comments/', BlogPostCommentsListCreate.as_view(), name='blog_post_comments'),
    # path('blog_comments/<int:blog_id>/', BlogDetailsRetrieveUpdateDelete.as_view(), name='blog_comment_rd'),
]

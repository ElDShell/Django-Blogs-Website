from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('blog/create/',BlogCreateView.as_view(),name='create_blog'),
    path('blog/<int:pk>/edit/',BlogUpdateView.as_view(),name='blog_edit'),
    path('blog/<int:pk>/delete/',BlogDeleteView.as_view(),name='blog_delete'),
    path('blog<int:pk>/update/image/',BlogImageUpdateView.as_view(),name='blog_image_update'),
    path('blog/<int:pk>/update/title/',BlogTitleUpdateView.as_view(),name='blog_title_update'),
    path('blog/<int:pk>/update/content/',BlogContentUpdateView.as_view(),name='blog_content_update'),
    path('blog/<int:pk>/update/tag/',BlogTagsUpdateView.as_view(),name='blog_tag_update'),
    path('blog/<int:pk>/detail/',BlogDetailView.as_view(),name='blog_detail'),
    path('tags/<slug:tag_slug>/',TagsView.as_view(),name='tags'),
    
    #Comments
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(),name='comment_delete'),

    #Extra
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
]

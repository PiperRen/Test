from django.urls import path
from blogging.views import BlogListView, BlogDetailView
# from blogging.views import stub_view, list_view, detail_view

# urlpatterns = [
#     path('', list_view, name="blog_index"),
#     path('posts/<int:post_id>/', detail_view, name="blog_detail"),
# ]

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/",BlogDetailView.as_view(), name="blog_detail"),
]

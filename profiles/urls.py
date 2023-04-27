from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('talents/', views.PostList.as_view(), name="talents"),
    path('add-post/', views.AddPost.as_view(), name="add_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('profile', views.UserProfile.as_view(), name='user_profile'),
    path('my-posts', views.MyPosts.as_view(), name='my_posts'),
    path('publish', views.publish, name='publish'),
    path('edit/<post_id>', views.edit_post, name='edit'),
    path('delete/<post_id>', views.delete_post, name='delete'),

]

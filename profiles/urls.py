from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('talents/', views.PostList.as_view(), name="talents"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

]
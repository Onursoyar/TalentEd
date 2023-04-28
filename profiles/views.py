from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages


class PostList(generic.ListView):
    """ View for Talents page"""
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "talents.html"
    paginate_by = 6


class IndexView(View):
    """View for home page"""

    def get(self, request):
        return render(request, 'index.html')


class PostDetail(View):
    """View for post details"""

    def get(self, request, slug, *args, **kwargs):
        """ get post meta data """
        queryset = Post.objects.filter(slug=slug)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Add comments against specific post"""
        queryset = Post.objects.filter(slug=slug)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class AddPost(View):
    """View for adding new post"""

    def get(self, request):
        return render(
            request,
<<<<<<< Updated upstream
            "publish.html", {'post_form': PostForm}
=======
            "add_post.html", {'add_post_form': PostForm}
            
>>>>>>> Stashed changes
        )

    def post(self, request):
        add_post_form = PostForm(request.POST, request.FILES)

        if add_post_form.is_valid():
            form = add_post_form.save(commit=False)
            form.author = User.objects.get(username=request.user.username)
            form.slug = form.title.replace(" ", "-")
            messages.success(request, 'Post has been created successfully')
            form.save()
            return redirect('talents')


class PostLike(View):
    """Add like on specific post"""

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class MyPosts(View):
<<<<<<< Updated upstream
    """Get user own posts only"""

    def get(self, request):
        return render(request, 'my_posts.html', {'posts': Post.objects.filter(author=request.user)})


class EditPost(View):
    """Edit user own posts"""

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
=======
    """Authenticated user views their own posts"""
    def get(self, request):
        return render(request, 'my_posts.html', {'posts': Post.objects.filter(author=request.user)})

class EditPost(View):

    def post(request, post_id):
        """Authenticated user views and edit their own posts"""
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post)
            if post_form.is_valid():
                form = post_form.save(commit=False)
                messages.success(
                    request, 'Post updated successfully'
                    )
                form.save()
                return redirect('talents')
>>>>>>> Stashed changes
        post_form = PostForm(instance=post)
        context = {'post_form': post_form}
        return render(request, 'edit_post.html', context)

<<<<<<< Updated upstream
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            form = post_form.save(commit=False)
            form.approved = False
            messages.success(request, 'Post has been updated successfully')
            form.save()
            return redirect('my_posts')


class DeletePost(View):
    """Delete user own poems"""

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect('my_posts')
=======

def delete_post(request, post_id):
    """Authenticated user views and edits their own posts"""
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect('talents')
>>>>>>> Stashed changes

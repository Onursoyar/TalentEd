from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
<<<<<<< Updated upstream
        fields = ('title',  'featured_image', 'content')
        
=======
        fields = ('title', 'featured_image', 'excerpt', 'content')
>>>>>>> Stashed changes

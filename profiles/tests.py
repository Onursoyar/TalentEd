"""Unit Testing for Forms, Models, Views"""
from django.test import TestCase
from .forms import PostForm, CommentForm
from .models import Post


class TestPostForm(TestCase):
    """Unit Test for Post Form"""

    def test_post_title_is_required(self):
        form = PostForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = PostForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PostForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'featured_image', 'content')
        )


class TestCommentForm(TestCase):
    """Unit Test for Comments Form"""

    def test_post_title_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestModels(TestCase):
    """Unit Testing models has featured image"""

    def test_post_has_featured_image(self):
        self.assertTrue(Post.featured_image)


class TestIndexViews(TestCase):
    """Unit Test Index Page View"""

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestPostListViews(TestCase):
    """Unit Test Post List Page View"""

    def test_get_talents_list_page(self):
        response = self.client.get('/talents/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talents.html')


class TestProfileViews(TestCase):
    """Unit Test Profile Page View"""

    def test_profile_page(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class TestPublishPoemViews(TestCase):
    """Unit Test Publish Page View"""

    def test_can_publish_poem(self):
        response = self.client.get('/publish')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish.html')

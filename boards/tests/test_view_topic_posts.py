from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from boards.views import PostListView
from ..models import Board, Topic, Post


class TopicPostsTest(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Quiz1', description='Quiz board.')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        topic = Topic.objects.create(subject='시스템보안2', board=board, starter=user)
        Post.objects.create(message='정보시스템 운영체계 보안', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEqual(view.func.view_class, PostListView)


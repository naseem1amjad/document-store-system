from django.test import TestCase
from .models import Topic


class TopicTests(TestCase):
    def setUp(self):
        Topic.objects.create(topic_name='SpekitLove!')
        Topic.objects.create(topic_name='Testing Topic')

    def test_topic(self):
        """  Test module for Topic model  """

        topic_spekit = Topic.objects.get(topic_name='SpekitLove!')
        topic_testing = Topic.objects.get(topic_name='Testing Topic')
        self.assertEqual(
            topic_spekit.topic_name, "SpekitLove!")
        self.assertEqual(
            topic_testing.topic_name, "Testing Topic")

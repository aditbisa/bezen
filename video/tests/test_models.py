import uuid
from datetime import datetime

from django.test import TestCase
from moto import mock_dynamodb

from ..models import KeywordModel, VideoModel


class VideoModelTests(TestCase):
    @mock_dynamodb
    def test_create_and_get(self):
        VideoModel.create_table(wait=True)

        video1 = VideoModel(
            uuid.uuid4().hex,
            created_at=datetime.now(),
            file_key=uuid.uuid4().hex,
            keywords=["game", "fun"],
        )
        video1.save()
        self.assertEqual(VideoModel.count(), 1)

        video2 = VideoModel(
            uuid.uuid4().hex,
            created_at=datetime.now(),
            file_key=uuid.uuid4().hex,
            keywords=["training", "serious"],
            details={"type": "mp4"},
        )
        video2.save()
        self.assertEqual(VideoModel.count(), 2)

        video3 = VideoModel.get(video1.uuid)
        self.assertEqual(video3.uuid, video1.uuid)
        self.assertEqual(video3.file_key, video1.file_key)

    @mock_dynamodb
    def test_create_and_update(self):
        VideoModel.create_table(wait=True)

        video1 = VideoModel(
            uuid.uuid4().hex,
            created_at=datetime.now(),
            file_key=uuid.uuid4().hex,
            keywords=["game", "fun"],
        )
        video1.save()
        self.assertEqual(VideoModel.count(), 1)

        video1.update(
            actions=[
                VideoModel.keywords.add(["challenging"]),
            ]
        )
        video3 = VideoModel.get(video1.uuid)
        self.assertEqual(video3.keywords, set(["game", "fun", "challenging"]))

        video1.update(
            actions=[
                VideoModel.details.set({"type": "avi", "size": "1k"}),
            ]
        )
        video3.refresh()
        self.assertEqual(video3.details.as_dict(), {"type": "avi", "size": "1k"})


class KeywordModelTests(TestCase):
    @mock_dynamodb
    def test_create_and_query(self):
        KeywordModel.create_table(wait=True)

        word1 = KeywordModel(
            "ga",
            "me",
            uuids={uuid.uuid4().hex},
        )
        word1.save()
        self.assertEqual(KeywordModel.count(), 1)

        word2 = KeywordModel(
            "fu",
            "n",
            uuids={uuid.uuid4().hex},
        )
        word2.save()
        self.assertEqual(KeywordModel.count(), 2)

        words = KeywordModel.query("ga", KeywordModel.last.startswith("m"))
        self.assertEqual(words.next().uuids, word1.uuids)
        self.assertEqual(words.total_count, 1)  # total_count populated after iter(obj)

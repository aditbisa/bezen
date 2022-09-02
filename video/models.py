from pynamodb.attributes import (
    MapAttribute,
    UnicodeAttribute,
    UnicodeSetAttribute,
    UTCDateTimeAttribute,
)
from pynamodb.models import Model


class VideoModel(Model):
    """
    A DynamoDB Video

    Attributes
    ----------
    uuid
        Also used for a filename in s3 (without extension/file type).
    file_key
        S3 key object.
    keywords
        [Future] To be used for Lamda-CloudSearch for keywords searching.
    """

    class Meta:
        table_name = "videos"

    uuid = UnicodeAttribute(hash_key=True)
    created_at = UTCDateTimeAttribute()
    file_key = UnicodeAttribute()
    keywords = UnicodeSetAttribute()
    details = MapAttribute(default={})


class KeywordModel(Model):
    """
    A DynamoDB Keyword

    A keyword will be lowered and split the first 3 digit as hash key and the remainder as range
      key.

    Attributes
    ----------
    first
        First 2 char of the keyword.
    last
        Remaining substring of the keyword.
    uuids
        A set of uuid whose related to the keyword.
    """

    class Meta:
        table_name = "keywords"

    first = UnicodeAttribute(hash_key=True)
    last = UnicodeAttribute(range_key=True)
    uuids = UnicodeSetAttribute()

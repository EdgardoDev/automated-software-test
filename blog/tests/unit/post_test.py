from unittest import TestCase


from unittest import TestCase
from post import Post

# On this test we create an object making sure that the properties match.
class PostTest(TestCase):
    # When a new post is created the title and content should match to what it has been defined.
    def test_create_post(self):
        newPost = Post("First Post Title", "First Post Content")

        self.assertEqual("First Post Title", newPost.title)
        self.assertEqual("First Post Content", newPost.content)

    # When a new post is created it checks that the keys and values are the same.
    def test_json(self):
        newPost = Post("First Post Title", "First Post Content")
        expected = {"title": "First Post Title", "content": "First Post Content"}

        self.assertDictEqual(expected, newPost.json())


# First let's create a class with the title and content properties.
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Here we convert the post to a json format.
    def json(self):
        # We return a dictionary that represent the post.
        return {
            "title" : self.title,
            "content" : self.content
        }





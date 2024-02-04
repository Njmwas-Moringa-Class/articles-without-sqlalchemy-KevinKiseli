

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.article_title = title
        Article.all_articles.append(self)

    def get_title(self):
        return self.article_title

    def get_author(self):
        return self.author

    def get_magazine(self):
        return self.magazine

    @classmethod
    def get_all(cls):
        return cls.all_articles



class Author:
    all_authors = []

    def __init__(self, name):
        self.author_name = name
        self.articles_written = []
        Author.all_authors.append(self)

    def get_name(self):
        return self.author_name

    def get_articles(self):
        return self.articles_written

    def get_magazines(self):
        return list(set(article.get_magazine() for article in self.articles_written))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self.articles_written.append(new_article)
        return new_article

    def topic_areas(self):
        return list(set(magazine.get_category() for magazine in self.get_magazines()))





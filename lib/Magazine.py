

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.magazine_name = name
        self.category_name = category
        Magazine.all_magazines.append(self)

    def get_name(self):
        return self.magazine_name

    def get_category(self):
        return self.category_name

    @classmethod
    def get_all(cls):
        return cls.all_magazines

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.get_name() == name:
                return magazine
        return None

    @classmethod
    def article_titles(cls, magazine):
        return [article.get_title() for article in Article.get_all() if article.get_magazine() == magazine]

    @classmethod
    def contributing_authors(cls, magazine):
        authors_dict = {}
        for article in Article.get_all():
            if article.get_magazine() == magazine:
                author = article.get_author()
                authors_dict[author] = authors_dict.get(author, 0) + 1
        return [author for author, count in authors_dict.items() if count > 2]
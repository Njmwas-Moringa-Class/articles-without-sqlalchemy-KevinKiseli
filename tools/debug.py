#!/usr/bin/env python3

# debug.py

import sys
sys.path.append('lib')  # Assuming 'lib' is one level above 'tools'

import ipdb

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    #  WRITE YOUR TEST CODE HERE ###
    

    author1 = Author("Kevin Kiseli")
    author2 = Author("Clinton Captain")
    
    ipdb.set_trace()
    
    magazine1 = Magazine("Forbes", "Machine Learning")
    magazine2 = Magazine("Time", "National Geographic")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "Top 10 richest Kenyan")
    article2 = author2.add_article(magazine1, "Best places to visit in the world")
    article3 = author1.add_article(magazine2, "Most expensive")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()

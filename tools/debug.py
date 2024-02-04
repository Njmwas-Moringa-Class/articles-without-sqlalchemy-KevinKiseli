
#!/usr/bin/env python3
import ipdb
from Article import Article
from Author import Author
from Magazine import Magazine

if __name__ == '__main__':
    
    author1 = Author("Kevin James")
    author2 = Author("Jack Wilson")
    
    magazine1 = Magazine("TechMag", "Technology")
    magazine2 = Magazine("SciMag", "Science")
    
    print(author1.get_name())  
    print(magazine1.get_name())  
   
    article1 = author1.add_article(magazine1, "Python Basics")
    article2 = author1.add_article(magazine2, "Quantum Computing")
    
    print(author1.get_articles())  

    print(author1.get_magazines())  
    
    print(author1.topic_areas())  
    
    found_magazine = Magazine.find_by_name("TechMag")
    print(Magazine.article_titles(found_magazine))  
   
    print(Magazine.contributing_authors(magazine1))  

    # DO NOT REMOVE THIS
    ipdb.set_trace()

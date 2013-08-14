from django.db.models.sql import Date
from elements.document import Document
from elements.article import Article
from elements.document_description import DocumentDescription
from elements.item import Item
from elements.revision import Revision
from elements.sections import Section


def main():
    revision = Revision(Date(),"Tashkent", "#19281928")
    description = DocumentDescription("Закон", revision)
    document = Document(1, description)

    section = Section("part", "Особенная часть", "part:1")
    section.articles.append(Article("text10", "article:10"))
    document.sections.append(section)

    article = Article("text", "article:1")
    article.items.append(Item())
    document.articles.append(article)
    document.articles.append(Article("text1", "article:2"))
    document.articles.append(Article("text2", "article:3"))
    document.articles.append(Article("text3", "article:4"))


if  __name__ =='__main__':
    main()
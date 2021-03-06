from unittest import TestCase
from common.dom.elements.comment import Comment
from common.dom.elements.header import Header
from common.dom.elements.document import *
from common.dom.elements.section import Section
from common.dom.elements.text_section import TextSection


class ElementTests(TestCase):
    def test_document_to_xml(self):
        document = Document()
        self.assertEqual('<document/>', document.to_xml())

    def test_description_to_xml(self):
        description = Header("name", "place")
        self.assertEqual('<header><name>name</name><place>place</place></header>', description.to_xml())

    def test_description_with_revisions_to_xml(self):
        description = Header("name", "place", "(from 1995 year);(from 1997 year)")
        xml = '<header>' \
              '<name>name</name>' \
              '<place>place</place>' \
              '<revisions>(from 1995 year);(from 1997 year)</revisions>' \
              '</header>'
        self.assertEqual(xml, description.to_xml())

    def test_document_with_description(self):
        description = Header("name", "place")
        document = Document(description)
        xml = '<document>' \
              '<header><name>name</name><place>place</place></header>' \
              '</document>'
        self.assertEqual(xml, document.to_xml())

    def test_empty_section(self):
        section = Section("part", "name", "1")
        xml = '<section id="part_1" level="part" name="name" number="1"/>'
        self.assertEqual(xml, section.to_xml())

    def test_section_with_subsections(self):
        part = Section("part", "name", "1")
        part.sections.append(Section("chapter", "name", "1"))
        part.sections.append(Section("chapter", "name", "2"))
        xml = '<section id="part_1" level="part" name="name" number="1">' \
              '<section id="chapter_1" level="chapter" name="name" number="1"/>' \
              '<section id="chapter_2" level="chapter" name="name" number="2"/>' \
              '</section>'
        self.assertEqual(xml, part.to_xml())

    def test_section_with_article(self):
        part = Section("part", "name", "1")
        chapter = Section("chapter", "name", "1")
        chapter.sections.append(TextSection("article", "1", "name"))
        part.sections.append(chapter)
        part.sections.append(Section("chapter", "name", "2"))
        xml = '<section id="part_1" level="part" name="name" number="1">' \
              '<section id="chapter_1" level="chapter" name="name" number="1">' \
              '<article id="article_1" level="article" name="name" number="1"/>' \
              '</section>' \
              '<section id="chapter_2" level="chapter" name="name" number="2"/>' \
              '</section>'
        self.assertEqual(xml, part.to_xml())

    def test_section_with_article_with_text(self):
        part = Section("part", "name", "1")
        chapter = Section("chapter", "name", "1")
        article_with_text = TextSection("article", "1", "name")
        article_with_text.text = "Hello world!"
        chapter.sections.append(article_with_text)
        part.sections.append(chapter)
        part.sections.append(Section("chapter", "name", "2"))
        xml = '<section id="part_1" level="part" name="name" number="1">' \
              '<section id="chapter_1" level="chapter" name="name" number="1">' \
              '<article id="article_1" level="article" name="name" number="1">' \
              'Hello world!' \
              '</article>' \
              '</section>' \
              '<section id="chapter_2" level="chapter" name="name" number="2"/>' \
              '</section>'
        self.assertEqual(xml, part.to_xml())

    def test_section_with_item(self):
        part = Section("part", "name", "1")
        chapter = Section("chapter", "name", "1")
        article = TextSection("article", "1", "name")
        item = TextSection("item", "1")
        article.sections.append(item)
        chapter.sections.append(article)
        # part.sections.append(Item("item", "name", "1"))
        part.sections.append(chapter)
        part.sections.append(Section("chapter", "name", "2"))
        xml = '<section id="part_1" level="part" name="name" number="1">' \
              '<section id="chapter_1" level="chapter" name="name" number="1">' \
              '<article id="article_1" level="article" name="name" number="1">' \
              '<item id="item_1" level="item" number="1"/>' \
              '</article>' \
              '</section>' \
              '<section id="chapter_2" level="chapter" name="name" number="2"/>' \
              '</section>'
        self.assertEqual(xml, part.to_xml())

    def test_section_with_item_with_text(self):
        part = Section("part", "name", "1")
        chapter = Section("chapter", "name", "1")
        article = TextSection("article", "1", "name")
        item = TextSection("item", "1")
        item.text = "djkshkaskjdsaj"
        article.sections.append(item)
        chapter.sections.append(article)
        part.sections.append(chapter)
        part.sections.append(Section("chapter", "name", "2"))
        item_text = TextSection
        item_text.text = "test test test"
        xml = '<section id="part_1" level="part" name="name" number="1">' \
              '<section id="chapter_1" level="chapter" name="name" number="1">' \
              '<article id="article_1" level="article" name="name" number="1">' \
              '<item id="item_1" level="item" number="1">djkshkaskjdsaj</item>' \
              '</article></section><section id="chapter_2" level="chapter" name="name" number="2"/>' \
              '</section>'
        self.assertEqual(xml, part.to_xml())


    def test_document_with_sections(self):
        description = Header("name", "place")
        document = Document(description)
        section = Section("part", "name", "1")
        document.add_section(section)
        xml = '<document>' \
              '<header><name>name</name><place>place</place></header>' \
              '<section id="part_1" level="part" name="name" number="1"/>' \
              '</document>'
        self.assertEqual(xml, document.to_xml())

    def test_article_with_item(self):
        article = TextSection("article", "1", "Article")
        item = TextSection("item", "1")
        item.text = "dslkdsaldsads"

        article.sections.append(item)
        xml = '<article id="article_1" level="article" ' \
              'name="Article" number="1"><item id="item_1" level="item"' \
              ' number="1">dslkdsaldsads</item></article>'
        self.assertEqual(xml, article.to_xml())

    def test_article_with_comment(self):
        article = TextSection("article", "1", "Article", comment=Comment("(asdhsjkl)"))

        xml = '<article id="article_1" level="article" ' \
              'name="Article" number="1"><comment>(asdhsjkl)</comment></article>'
        self.assertEqual(xml, article.to_xml())

    def test_comments_in_chapter(self):
        section = Section("chapter", 'chapter1', "1", comment=Comment(u"(qwerty)"))
        xml = '<section id="chapter_1" level="chapter" name="chapter1" number="1"><comment>(qwerty)</comment></section>'
        self.assertEqual(xml, section.to_xml())

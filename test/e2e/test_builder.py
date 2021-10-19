import unittest

from hamcrest import contains_string, assert_that

from markdown_builder.document import MarkdownDocument


class BuilderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.document = MarkdownDocument()

    def test_can_append_text(self):
        self.document.append_text('Foo')
        assert_that(self.document.contents(), contains_string('Foo'))

    def test_can_append_top_level_heading(self):
        self.document.append_heading('This is a top-level heading')
        assert_that(self.document.contents(), contains_string('# This is a top-level heading'))

    def test_can_append_lower_level_heading(self):
        self.document.append_heading('This is a level two heading', 2)
        assert_that(self.document.contents(), contains_string('## This is a level two heading'))

    def test_can_indent_text(self):
        self.document.append_text_indented('Foo', 0)
        self.document.append_text_indented('Bar', 1)
        contents = self.document.contents()
        assert_that(contents, contains_string('Foo'))
        assert_that(contents, contains_string('    Bar'))

    def test_can_change_indentation(self):
        self.document = MarkdownDocument('    ')
        self.document.append_text_indented('Bar', 1)
        assert_that(self.document.contents(), contains_string('    Bar'))

    def test_can_add_bullet(self):
        self.document.append_bullet('baz')
        assert_that(self.document.contents(), contains_string('- baz'))

    def test_can_add_link(self):
        self.document.append_link('BBC', 'https://www.bbc.co.uk/')
        assert_that(self.document.contents(), contains_string('[BBC](https://www.bbc.co.uk/)'))

    def test_can_add_bulleted_link(self):
        self.document.append_bulleted_link('BBC', 'https://www.bbc.co.uk/')
        assert_that(self.document.contents(), contains_string('- [BBC](https://www.bbc.co.uk/)'))


if __name__ == '__main__':
    unittest.main()

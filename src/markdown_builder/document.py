from io import StringIO


def bullet(text):
    return '- ' + text


def make_link(text, link):
    return '[%s](%s)' % (text, link)


class MarkdownDocument:
    def __init__(self, indentation=None):
        self._contents = StringIO()
        self.indentation = indentation if indentation else '    '

    def append_text(self, text: str):
        self._contents.write(text)
        self._contents.write('\n')

    def append_text_indented(self, text, depth: int):
        text = (depth*self.indentation)+text
        self.append_text(text)

    def append_link(self, text, link, depth: int=0):
        self.append_text_indented(make_link(text, link), depth)

    def append_bulleted_link(self, text, link, depth: int=0):
        self.append_text_indented(bullet(make_link(text, link)), depth)

    def append_bullet(self, text, depth=0):
        self.append_text_indented(bullet(text), depth)

    def contents(self):
        result = self._contents.getvalue()
        self._contents.close()
        return result

    def append_heading(self, text, level=1):
        self.append_text(level*'#' +' ' + text)

# markdown-builder

`markdown-builder` is a minimalist package for creating [MarkDown](https://en.wikipedia.org/wiki/Markdown)
documents in a Python program.

It requires Python 3.

It grew out of a number of Python applications that needed similar functionality.
At present, it only supports the features required by those applications,
but I'm open to suggestions for additions.

The [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) 
led me to separate out the code into a separate package.

With `markdown-builder` you can build a Markdown document in a few lines
of Python code.

## Installation

`pip3 install markdown-builder.`

## Quickstart

The following Python program will generate [SAMPLE.md](SAMPLE.md)

```python
from markdown_builder.document import MarkdownDocument

md = MarkdownDocument()
md.append_heading('Welcome to MarkDown')
md.append_text('markdown-builder is really easy to use')
md.append_heading('This is a level2 heading', 2)
md.append_text_indented('This is inset', depth=1)
md.append_bullet('This is a top-level bullet point')
md.append_bullet('This is a lower level bullet point', depth=1)
```



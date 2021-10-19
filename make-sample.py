from markdown_builder.document import MarkdownDocument

md = MarkdownDocument()
md.append_heading('Welcome to MarkDown')
md.append_text('markdown-builder is really to use')
md.append_heading('This is a level2 heading', 2)
md.append_text_indented('This is inset', depth=1)
md.append_bullet('This is a top-level bullet point')
md.append_bullet('This is a lower level bullet point', depth=1)

with open('SAMPLE.md', 'w') as mdf:
    mdf.write(md.contents())
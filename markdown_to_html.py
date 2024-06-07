import re
import sys

def validate_markdown(markdown_text):
    if re.search(r'\*\*.*`.*_.*`.*\*\*', markdown_text) or \
       re.search(r'`.*\*\*.*_.*\*\*.*`', markdown_text) or \
       re.search(r'_.*\*\*.*`.*\*\*.*_', markdown_text):
        return False

    if markdown_text.count('**') % 2 != 0 or \
       markdown_text.count('_') % 2 != 0 or \
       markdown_text.count('`') % 2 != 0 or \
       markdown_text.count('```') % 2 != 0:
        return False

    return True

def markdown_to_html(markdown_text):
    if not validate_markdown(markdown_text):
        print("Error: invalid markdown", file=sys.stderr)
        sys.exit(1)

    preformatted_blocks = re.findall(r'```(.*?)```', markdown_text, re.DOTALL)
    for block in preformatted_blocks:
        html_block = f'<pre>{block}</pre>'
        markdown_text = markdown_text.replace(f'```{block}```', html_block)

    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_text)

    markdown_text = re.sub(r'_(.*?)_', r'<i>\1</i>', markdown_text)

    markdown_text = re.sub(r'`(.*?)`', r'<tt>\1</tt>', markdown_text)

    paragraphs = markdown_text.split('\n\n')
    html_paragraphs = ['<p>{}</p>'.format(p.replace('\n', ' ')) for p in paragraphs]
    html_text = ''.join(html_paragraphs)

    return html_text

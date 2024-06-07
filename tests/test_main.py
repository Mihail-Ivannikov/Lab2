# tests/test_main.py
import subprocess
import os

def test_markdown_to_html(tmp_path):
    sample_markdown = "**bold text**\n\n_italic text_\n\n`monospace text`\n\n```preformatted block```"
    markdown_file = tmp_path / "sample.md"
    html_file = tmp_path / "output.html"

    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(sample_markdown)

    result = subprocess.run(['python', 'main.py', str(markdown_file), '--out', str(html_file), '--format', 'html'],
                            capture_output=True, text=True)

    assert result.returncode == 0

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    assert '<b>bold text</b>' in html_content
    assert '<i>italic text</i>' in html_content
    assert '<tt>monospace text</tt>' in html_content
    assert '<pre>preformatted block</pre>' in html_content

def test_markdown_to_ansi(tmp_path):
    # Create a sample markdown file
    sample_markdown = "**bold text**\n\n_italic text_\n\n`monospace text`\n\n```preformatted block```"
    markdown_file = tmp_path / "sample.md"

    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(sample_markdown)

    # Run the script
    result = subprocess.run(['python', 'main.py', str(markdown_file), '--format', 'ansi'],
                            capture_output=True, text=True)

    assert result.returncode == 0
    ansi_content = result.stdout

    assert '\033[1mbold text\033[0m' in ansi_content
    assert '\033[3mitalic text\033[0m' in ansi_content
    assert '\033[7mmonospace text\033[0m' in ansi_content
    assert '\033[7mpreformatted block\033[0m' in ansi_content
import sys
from markdown_to_html import markdown_to_html

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='utf-16') as file:
                return file.read()
        except UnicodeDecodeError:
            print("Error: Unable to decode the file. Please make sure it is in UTF-16 encoding.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print("Error:", e, file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_markdown_file> [--out <output_html_file>]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    markdown_content = read_markdown_file(input_file)
    html_content = markdown_to_html(markdown_content)

    if len(sys.argv) > 2 and sys.argv[2] == '--out':
        if len(sys.argv) < 4:
            print("Error: Please specify the output file path.", file=sys.stderr)
            sys.exit(1)
        output_file = sys.argv[3]
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(html_content)
            print("HTML output written to", output_file)
        except Exception as e:
            print("Error:", e, file=sys.stderr)
            sys.exit(1)
    else:
        print(html_content)

if __name__ == "__main__":
    main()

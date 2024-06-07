import sys
from markdown_to_html import markdown_to_html, markdown_to_ansi

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
        print("Usage: python main.py <input_markdown_file> [--out <output_file>] [--format <html|ansi>]", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    markdown_content = read_markdown_file(input_file)
    
    output_file = None
    output_format = 'ansi'
    
    if '--out' in sys.argv:
        output_file_index = sys.argv.index('--out') + 1
        if output_file_index >= len(sys.argv):
            print("Error: Please specify the output file path.", file=sys.stderr)
            sys.exit(1)
        output_file = sys.argv[output_file_index]
        output_format = 'html'

    if '--format' in sys.argv:
        format_index = sys.argv.index('--format') + 1
        if format_index >= len(sys.argv):
            print("Error: Please specify the format (html or ansi).", file=sys.stderr)
            sys.exit(1)
        output_format = sys.argv[format_index]

    if output_format == 'html':
        formatted_content = markdown_to_html(markdown_content)
    elif output_format == 'ansi':
        formatted_content = markdown_to_ansi(markdown_content)
    else:
        print("Error: Unsupported format. Please use 'html' or 'ansi'.", file=sys.stderr)
        sys.exit(1)

    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(formatted_content)
            print("Output written to", output_file)
        except Exception as e:
            print("Error:", e, file=sys.stderr)
            sys.exit(1)
    else:
        print(formatted_content)

if __name__ == "__main__":
    main()

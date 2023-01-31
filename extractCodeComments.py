# usage: python script.py source_file.ext


import sys
import re
import json

def extract_comments(code, language):
        comment_patterns = {
        'C++': re.compile(r'(?://|/\*|\*/).*'),
        'C': re.compile(r'(?://|/\*|\*/).*'),
        'C#': re.compile(r'(?://|/\*|\*/).*'),
        'Python': re.compile(r'#.*'),
        'javascript': re.compile(r'(?://|/\*|\*/).*'),
        'Go': re.compile(r'(?://).*'),
        'PHP': re.compile(r'(?://|#).*'),
        'Java': re.compile(r'(?://|/\*|\*/).*'),
    }
    comment_pattern = comment_patterns.get(language, None)
    if not comment_pattern:
        return []
    comments = comment_pattern.findall(code)
    return comments


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        with open(file_path) as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: permission denied: {file_path}")
        sys.exit(1)
    # Determine the language from the file extension
    ext = file_path.rsplit('.', 1)[-1]
    if ext not in ['cpp', 'c', 'cs', 'py', 'js', 'go', 'php', 'java']:
        print(f"Error: unsupported file type: {ext}")
        sys.exit(1)
    language = {
        'cpp': 'C++',
        'c': 'C',
        'cs': 'C#',
        'py': 'Python',
        'js': 'javascript',
        'go': 'Go',
        'php': 'PHP',
        'java': 'Java',
    }[ext]
    comments = extract_comments(code, language)
    with open('comments.json', 'w') as f:
        json.dump(comments, f, indent=4)

if __name__ == '__main__':
    main()


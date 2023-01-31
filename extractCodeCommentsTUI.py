# required: pip install urwid
# This script uses urwid to create a main loop that displays the result of the comment extraction process. 
# The result is displayed as a text widget in the terminal. If there was an error, an error message is displayed instead.

import re
import json
import urwid

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
    # Get the code from the file
    try:
        with open(sys.argv[1]) as f:
            code = f.read()
    except FileNotFoundError:
        return urwid.Text(("error", "Error: file not found"))
    except PermissionError:
        return urwid.Text(("error", "Error: permission denied"))
    # Determine the language from the file extension
    ext = sys.argv[1].rsplit('.', 1)[-1]
    if ext not in ['cpp', 'c', 'cs', 'py', 'js', 'go', 'php', 'java']:
        return urwid.Text(("error", f"Error: unsupported file type: {ext}"))
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
    # Write the comments to a JSON file
    with open('comments.json', 'w') as f:
        json.dump(comments, f, indent=4)
    # Display the result in the terminal
    return urwid.Text(f"{len(comments)} comments extracted and saved to comments.json")

if __name__ == '__main__':
    # Create a main loop and run it
    loop = urwid.MainLoop(main(), unhandled_input=lambda key: key)
    loop.run()

# Code Comment Extractor
This script defines a function extract_comments that takes in a code string and a language string and returns a list of comments. It uses regular expressions to match different comment styles for different languages. The main function uses the codes dictionary to test the extract_comments function for different languages and write the result to a comments.json file.


## Requirements & Dependencies

The script requires the following dependencies:

Python 3
The built-in json library in Python, which is used to convert the extracted comments into a JSON file.

If you want to use a terminal UI library to make the script more intuitive and beautiful, you can use a library such as curses or urwid. These libraries provide a way to create user interfaces within a terminal window and display the extracted comments in a more visually appealing way.

To use either of these libraries, you would need to install them using pip (the Python package manager). Here's an example of how you could install the urwid library:

```pip install urwid```

Once you have installed the library, you can import it into your script and use it to create the UI. You may need to make modifications to the script to incorporate the library and display the extracted comments in the desired way.

## Usage
For standard Python code, use this command:

```python extract_comments.py test.py```

For CPP code, use this command:

```python extract_comments.py test.cpp```



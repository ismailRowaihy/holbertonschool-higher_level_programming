#!/usr/bin/python3
"""
this module use the function text_indentation
to prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """print string with 2lines after ., ? and :"""
    n_line_char = [".", "?", ":"]
    has_space = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if has_space:
            if text[i] == " ":
                continue
            else:
                has_space = False
        if text[i] in n_line_char:
            print(f"{text[i]}", end="\n\n")
            if i+1 < len(text):
                if text[i + 1].isspace():
                    has_space = True
        else:
            print(f"{text[i]}", end="")

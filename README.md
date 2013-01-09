LaTeXAccents
============

Decode and encode letters with accents in LaTeX


Installation
------------

I hope soon it will be possible tu use Package Control to install "LaTeXAccents"

For the moment:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo

How to use
----------
To transform all letters with accents (like é,à,î, ...) to LaTeX accents (\'e, \`a, \^\i, ...) :

1. Open Command Pannel (Ctrl+Shift+P by default)
2. Select "LaTeXAccents: Encode accents" (_hint_ : you can type something shorter like "ltxenc")

To transform all letters with LaTeX accents (\'e, \`a, \^\i, ...) to letters with accents (like é,à,î, ...):

1. Open Command Pannel (Ctrl+Shift+P by default)
2. Select "LaTeXAccents: Decode accents" (_hint_ : you can type something shorter like "ltxdec")

_Hint_ : If your file contain accents you should use : \usepackage[...]{inputenc}

Commands
--------

* `encode_latex_accents`: Encode all letters with accents to latex accents.
* `decode_latex_accents`: Decode all letters with latex accents to 'normal' letters with accents.
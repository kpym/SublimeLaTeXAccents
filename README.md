LaTeXAccents for Sublime Text 2
===============================
This is a plugin for [Sublime Text 2](http://www.sublimetext.com/2).
It decode and encode letters with accents in LaTeX files.


Installation
------------

Using [Package Control](http://wbond.net/sublime_packages/package_control), install "LaTeX Accents".

Or manualy:

1. open the Sublime Text 2 Packages folder

        - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
        - Windows: %APPDATA%/Sublime Text 2/Packages/
        - Linux: ~/.Sublime Text 2/Packages/
    
2. clone this repo.

How to use
----------
To transform all letters with accents (like é,à,î, ...) to LaTeX accents (\'e, \\\`a, \\\^\i, ... ) :

1. open Command Pannel (`Ctrl+Shift+P` by default);
2. select "LaTeXAccents: Encode accents" ( _hint_ : you can type something shorter like "ltxenc").

To transform all letters with LaTeX accents (\'e, \\\`a, \\\^\i, ...) to letters with accents (like é,à,î, ...):

1. open Command Pannel (`Ctrl+Shift+P` by default);
2. select "LaTeXAccents: Decode accents" ( _hint_ : you can type something shorter like "ltxdec" )

_Hint_ : If your file contains accents you should :

1. save the file using appropriate encoding (for example `ISO 8859-1` or `UTF-8`);
2. use : `\usepackage[...]{inputenc}` with the corresponding encoding (for example `latin` or `utf8`}.

Commands
--------

* `encode_latex_accents`: Encode all letters with accents to latex accents.
* `decode_latex_accents`: Decode all letters with latex accents to 'normal' letters with accents.

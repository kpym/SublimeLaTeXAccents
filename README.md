LaTeXAccents for Sublime Text 2 and 3
=====================================
This is a plugin for [Sublime Text 2](http://www.sublimetext.com/2) and [Sublime Text 3](http://www.sublimetext.com/3).
It decode and encode letters with accents in LaTeX files.


Installation
------------

Using [Package Control](http://wbond.net/sublime_packages/package_control), install "LaTeX Accents".

Or manualy:

1a. open the Sublime Text Packages folder

  - for ST2
    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/
  - for ST3
    - OS X: ~/Library/Application Support/Sublime Text 3/Data/Packages/
    - Windows: %programfiles%/Sublime Text 3/Data/Packages/
    - Linux: ~/.Sublime Text 3/Data/Packages/

2. clone this repo (`git clone git://github.com/kpym/SublimeLaTeXAccents LaTeXAccents`).

How to use
----------
To transform all letters with accents (like é,à,î, ...) to LaTeX accents (\'e, \\\`a, \\\^\i, ... ) :

1. open Command Pannel (`Ctrl+Shift+P` by default);
2. select "LaTeXAccents: Encode accents" ( _hint_ : you can type something shorter like "ltxenc").

To transform all letters with LaTeX accents (\'e, \\\`a, \\\^\i, ...) to letters with accents (like é,à,î, ...):

1. open Command Pannel (`Ctrl+Shift+P` by default);
2. select "LaTeXAccents: Decode accents" ( _hint_ : you can type something shorter like "ltxdec" )

To remove accents from all letters (letters é,à,î,... became e,a,i,... ) :

1. open Command Pannel (`Ctrl+Shift+P` by default);
2. select "LaTeXAccents: Remove accents" ( _hint_ : you can type something shorter like "ltxrmv").

_Hint_ : If your file contains accents you should :

1. save the file using appropriate encoding (for example `ISO 8859-1` or `UTF-8`);
2. use : `\usepackage[...]{inputenc}` with the corresponding encoding (for example `latin` or `utf8`}.

Commands
--------

* `encode_latex_accents`: Encode all letters with accents to latex accents.
* `decode_latex_accents`: Decode all letters with latex accents to 'normal' letters with accents.
* `remove_accents`: Remove all accents from 'normal' letters with accents.

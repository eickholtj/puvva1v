#!/bin/bash

BASEPATH="$( cd "$(dirname "$0")" ; pwd -P )"

python $BASEPATH/annotations.py
python $BASEPATH/book_chapters.py
python $BASEPATH/book_chapters_sections.py
python $BASEPATH/books.py


#!/bin/bash

BASEPATH="$( cd "$(dirname "$0")" ; pwd -P )"

python $BASEPATH/annotations.py
python $BASEPATH/book_chap.py
python $BASEPATH/book_chap_sec.py
python $BASEPATH/books.py


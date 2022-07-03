#! /bin/sh
set -e

python -m spacy download de_core_news_md

python ./app/main.py
#! /bin/sh
set -e

python -m spacy download de_core_news_md
# python -m spacy download en_core_web_sm

# tail -f /dev/null
python ./app/main.py
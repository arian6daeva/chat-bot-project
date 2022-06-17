#! /bin/sh
set -e

python -m spacy download de_dep_news_trf
# python -m spacy download en_core_web_sm

# tail -f /dev/null
python ./app/main.py
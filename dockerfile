FROM python:3.7.13-slim-buster

RUN apt-get -y update
# RUN apt-get -y install git
RUN python3 -m pip install --upgrade pip setuptools wheel
WORKDIR /usr/src

COPY . /usr/src/

RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install git+https://github.com/gunthercox/chatterbot-corpus.git#egg=chatterbot-corpus
# RUN pip install spacy==2.3.5
# RUN pip install spacy en_core_web_sm --force
 
# CMD [ "python", "-m spacy download de_dep_news_trf"]

COPY chatterbot /usr/local/lib/python3.7/site-packages/chatterbot/
RUN mkdir -p /usr/local/lib/python3.7/site-packages/chatterbot_corpus/data/dhbw
COPY trainingsdaten /usr/local/lib/python3.7/site-packages/chatterbot_corpus/data/dhbw/
# COPY comparisons.py /usr/local/lib/python3.7/site-packages/chatterbot/
# COPY tagging.py /usr/local/lib/python3.7/site-packages/chatterbot/
# COPY languages.py /usr/local/lib/python3.7/site-packages/chatterbot/


CMD [ "sh","./entrypoint.sh" ]
# CMD [ "python", "./app/main.py" ]
# ENTRYPOINT ["tail", "/dev/null"]
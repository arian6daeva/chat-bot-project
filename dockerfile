FROM python:3

RUN apt-get -y update
WORKDIR /usr/src

COPY . /usr/src/

RUN pip install --no-cache-dir -r ./app/requirements.txt

CMD [ "python", "./app/main.py.py" ]

ENTRYPOINT ["tail", "-f", "/dev/null"]
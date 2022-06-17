import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.languages import GER
from chatterbot.response_selection import get_random_response
from chatterbot.comparisons import SpacySimilarity, LevenshteinDistance, JaccardSimilarity

import logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot(
    'DHBW-Chatbot',
    language=GER,
    tagger_language=GER,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///./datenbank/database.sqlite3',
    logic_adapters=[
        {
        'import_path': 'chatterbot.logic.BestMatch',
        "statement_comparison_function": SpacySimilarity,
        "response_selection_method": get_random_response,
        'default_response': 'Leider konnte ich dich nicht verstehen. Wende dich bitte an einen Ansprechpartner der DHBW Stuttgart.'
        },
        {
        'import_path': 'chatterbot.logic.BestMatch',
        "statement_comparison_function": LevenshteinDistance,
        "response_selection_method": get_random_response,
        'default_response': 'Leider konnte ich dich nicht verstehen. Wende dich bitte an einen Ansprechpartner der DHBW Stuttgart.'
        },
        {
        'import_path': 'chatterbot.logic.BestMatch',
        "statement_comparison_function": JaccardSimilarity,
        "response_selection_method": get_random_response,
        'default_response': 'Leider konnte ich dich nicht verstehen. Wende dich bitte an einen Ansprechpartner der DHBW Stuttgart.'
        }
    ]
) 

trainer = ListTrainer(chatbot)
training_data = open('training_data/konversationen.txt').read().splitlines()
trainer.train(training_data) 

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
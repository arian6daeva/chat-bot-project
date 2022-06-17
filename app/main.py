import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_most_frequent_response

class GER:
    ISO_639_1 = 'de'
    ISO_639 = 'ger'
    ENGLISH_NAME = 'German'

chatbot = ChatBot(
    'Chatty',
    language=GER,
    tagger_language=GER,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///./datenbank/database.sqlite3',
    logic_adapters=[
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'Leider konnte ich dich nicht verstehen. Wende dich bitte an einen Ansprechpartner der DHBW Stuttgart.',
        'maximum_similarity_threshold': 0.90,
        # "statement_comparison_function": LevenshteinDistance,
        # "response_selection_method": get_most_frequent_response
        }
    ],

    # logic_adapters=[
    #     {
    #         "import_path": "chatterbot.logic.BestMatch",
    #         "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
    #         "response_selection_method": chatterbot.response_selection.get_first_response
    #     }
    # ],
) 

# Training with Personal Ques & Ans 
# training_data_quesans = open('training_data/crime.txt').read().splitlines()
# training_data_personal = open('training_data/simple.txt').read().splitlines()
# training_data_conv = open('training_data/more.txt').read().splitlines()

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
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
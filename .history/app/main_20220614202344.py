from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Chatty',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'Leider konnte ich dich nicht verstehen. Wende dich bitte an einen Ansprechpartner der DHBW Stuttgart.',
        'maximum_similarity_threshold': 0.95
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 

 # Training with Personal Ques & Ans 
# training_data_quesans = open('training_data/crime.txt').read().splitlines()
# training_data_personal = open('training_data/simple.txt').read().splitlines()
# training_data_conv = open('training_data/more.txt').read().splitlines()

training_data = open('training_data/konversationen.txt').read().splitlines()

trainer = ListTrainer(chatbot)
trainer.train(training_data) 

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)

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
    app.run(host="0.0.0.0", debug=True)
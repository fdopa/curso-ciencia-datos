from flask import Flask

app = Flask(__name__)
# se crearan dos ruta
@app.route('/')
def home():
    return 'Hello World'

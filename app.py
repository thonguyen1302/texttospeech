from flask import Flask, render_template, request
from gtts import gTTS
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # The text that you want to convert to audio
    text = request.form.get('text')

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    name = str(datetime.now())
    myobj.save("static/file.mp3")

    return render_template('index.html', content="static/file.mp3")

if __name__ == '__main__':
    app.run(port=3000, debug=True)




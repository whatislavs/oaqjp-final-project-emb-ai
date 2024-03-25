''' Routes and server initialization'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' Return the main page '''
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    ''' Receive the text and return detected emotions '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = str(response['anger'])
    disgust = str(response['disgust'])
    fear = str(response['fear'])
    joy = str(response['joy'])
    sadness = str(response['sadness'])
    dominant_emotion = response['dominant_emotion']
    return "For the given statement, the system response is " \
    "'anger': "+anger+", 'disgust': "+disgust+", 'fear': "+fear+", " \
    "'joy': "+joy+" and 'sadness': "+sadness+". " \
    "The dominant emotion is "+dominant_emotion+"." \

if __name__ == "__main__":
    app.run(host="localhost", port=5000)

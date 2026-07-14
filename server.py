"""
This module implements a Flask-based web application for detecting
emotions in text using the Watson NLP Emotion Predict library.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotion of the text provided via the 'textToAnalyze'
    query parameter and return a formatted response.

    Returns:
        str: A formatted string describing the detected emotions and
        the dominant emotion, or an error message if the input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

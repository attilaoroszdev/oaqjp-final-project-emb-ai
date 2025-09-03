"""
This module implements a Flask web application for emotion detection in text.
It provides endpoints for analyzing emotional content in text using an emotion detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")


@app.route('/')
def home():
    """
    Render the home page of the emotion detection application.

    Returns:
        str: Rendered HTML template for the home page
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the emotional content of provided text using the emotion detector.

    The function extracts text from the URL parameters and processes it through
    the emotion detection service to identify emotional components and the
    dominant emotion.

    Returns:
        str: A formatted string containing the emotion analysis results,
             including scores for anger, disgust, fear, joy, sadness,
             and the dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    formatted_result = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}. "
    )
    return formatted_result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

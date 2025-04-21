"""Flask application for emotion detection from text input."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotions_detector():
    """
    Handle emotion detection requests.

    Retrieves 'textToAnalyze' from query parameters, processes it with
    emotion_detector, and returns a JSON response with emotion scores or an error.

    Returns:
        flask.Response: JSON response with emotion scores or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid input! Try again!'
    message = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return message

@app.route('/')
def render_index_page():
    """
    Render the index page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

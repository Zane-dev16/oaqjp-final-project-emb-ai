"""emotion detection server"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """render project web page"""
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """return emotions of textToAnalyze"""
    text = request.args.get("textToAnalyze")
    emotions = emotion_detector(text)
    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again"
    response = f"For the given statement, \
                the system response is 'anger': {emotions['anger']}, \
                'disgust': {emotions['disgust']}, \
                'fear': {emotions['fear']}, \
                'joy': {emotions['joy']} \
                and 'sadness': {emotions['sadness']}. \
                The dominant emotion is <b>{emotions['dominant_emotion']}</b>."
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

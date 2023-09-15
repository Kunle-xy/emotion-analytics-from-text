# Import libraries
from flask import Flask, redirect, request, render_template, url_for
from EmotionDetection import emotion_detection as ed

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/")
def get_transactions():
    return render_template("index.html")

# Create operation: Display add transaction form
@app.route("/emotionDetector")
def emotion_detector():
    text = request.args.get('textToAnalyze')
    response, _ = ed.emotion_detector(text)
    response_text = f"For the given statement, the system response is \
                'anger': {response['anger']}, 'disgust': {response['disgust']}, \
                'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. \
                The dominant emotion is {response['dominant_emotion']}."
    
    # Render the form template to display the add transaction form
    return response_text



# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
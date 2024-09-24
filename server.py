''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the emotion_detector function from the package created: TODO
from flask import Flask, request, send_from_directory
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    """Get text from FE and sent to BE

    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None, indicating an error or invalid input
    dominant_emotion = response.pop('dominant_emotion', None)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response = ', '.join(f"'{key}': {value}" for key, value in response.items())
    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is \
    {response}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """Render index page of app
    """
    return send_from_directory('templates', 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

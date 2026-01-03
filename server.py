"""Module for deployement using flask"""
# import required libraries
from flask import Flask,request,render_template
# import emotion_detector
from EmotionDetection.emotion_detection import emotion_detector
# Initiate app
app = Flask("Emotion Detector")
# create funtion
@app.route("/emotionDetector")
def emtn_detector():
    """ function to get text and display the result"""
    text_to_analyze = request.args.get("textToAnalyze")
    emtn_dict = emotion_detector(text_to_analyze)
    if emtn_dict["dominant_emotion"] is None:
        return "Invalid text! Please try again!."
    return (f"For the given statement, the system response is 'anger': {emtn_dict['anger']},"
    f" 'disgust': {emtn_dict['disgust']}, 'fear': {emtn_dict['fear']}, 'joy': {emtn_dict['joy']} an" 
    f"d 'sadness': {emtn_dict['sadness']}. The dominant emotion is {emtn_dict['dominant_emotion']}."
    )
#render index
@app.route("/")
def render_index_page():
    """ Function to render main page. """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to send a post request and recieve the output.
    """
    # URL of the library
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # variable for which the request is to be made
    myobj = { "raw_document": { "text": text_to_analyze } }
    # PUT request
    response = requests.post(URL, json = myobj, headers = Headers)
    # load formatted response
    formatted_response = json.loads(response.text)
    # extract the emotions dict from the response
    emotions_dict = formatted_response["emotionPredictions"][0]["emotion"]
    # find the dominant_emotion
    score = -1
    dominant_emotion = ''
    for emtn in emotions_dict:
        if emotions_dict[emtn]>score:
            score = emotions_dict[emtn]
            dominant_emotion = emtn
    # create the entry for dominant_emotion
    emotions_dict["dominant_emotion"] = dominant_emotion

    # return the updated dict
    return emotions_dict 
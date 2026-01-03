import requests

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
    # returning the output as a text attribute
    return response.text
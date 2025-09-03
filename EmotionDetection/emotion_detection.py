import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze the emotional content of a given text using the IBM Watson Emotion
    Analysis API. This function takes a text string input and sends a request to
    the IBM Watson Emotion API, returning the result in a textual format.

    :param text_to_analyze: The input text string to be analyzed for emotion
                            content.
    :type text_to_analyze: str
    :return: The API response containing the emotional analysis results of the
             input text.
    :rtype: str
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_obj, headers=header)

    # Error check, in case the input is empty
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Convert the returned JSON response to a Python dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotion scores from the response
    parsed_response = formatted_response['emotionPredictions'][0]['emotion']
    # Extract the dominant emotion from the emotion scores
    dominant_emotion = max(parsed_response, key=parsed_response.get)
    # Add dominant_emotion to the dictionary
    parsed_response['dominant_emotion'] = dominant_emotion

    # Return the new dictionary
    return parsed_response



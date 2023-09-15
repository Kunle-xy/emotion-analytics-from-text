import requests
from typing import Dict
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'


def emotion_detector(text_to_analyse: str):
    data_json= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = URL, json = data_json, headers = HEADERS)
    output = response.json()["emotionPredictions"][0]["emotion"]
    code = response.status_code
    dominant = _helper(output)
    output['dominant_emotion'] = f"{dominant} is the dominant emotion"
    return output, code

def _helper( data: Dict):
    """
    gets the max value from a dictionary
    """
    return max(data, key=data.get)


if __name__ == "__main__":
    TEST = "she lost her best friend "
    output, _ = emotion_detector(TEST)
    print(output)
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 400:
        return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }

    
    formatted_res = json.loads(response.text)
    emotion_scores = formatted_res["emotionPredictions"][0]["emotion"]

    max_score = emotion_scores["anger"]
    for emotion, score in emotion_scores.items():
        if score >= max_score:
            max_score = score
            dominant_emotion = emotion
    emotion_scores["dominant_emotion"] = dominant_emotion
    return emotion_scores

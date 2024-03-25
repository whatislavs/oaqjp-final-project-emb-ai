''' Emotion detection module '''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' Emotion detection function '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    elif response.status_code == 200:
        json_text = json.loads(response.text)
        emotion_scores = json_text['emotionPredictions'][0]['emotion']
        emotion_max = max(zip(emotion_scores.values(), emotion_scores.keys()))[1]
        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': emotion_max
        }
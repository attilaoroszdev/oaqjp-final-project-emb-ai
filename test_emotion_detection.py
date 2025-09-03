from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        test_case_1 = {'text': 'I am glad this happened', 'result': 'joy'}
        test_case_2 = {'text': 'I am really mad about this', 'result': 'anger'}
        test_case_3 = {'text': 'I feel disgusted just hearing about this', 'result': 'disgust'}
        test_case_4 = {'text': 'I am so sad about this', 'result': 'sadness'}
        test_case_5 = {'text': 'I am really afraid that this will happen', 'result': 'fear'}

        result_1 = emotion_detector(test_case_1['text'])
        self.assertEqual(result_1['dominant_emotion'], test_case_1['result'])
        result_2 = emotion_detector(test_case_2['text'])
        self.assertEqual(result_2['dominant_emotion'], test_case_2['result'])
        result_3 = emotion_detector(test_case_3['text'])
        self.assertEqual(result_3['dominant_emotion'], test_case_3['result'])
        result_4 = emotion_detector(test_case_4['text'])
        self.assertEqual(result_4['dominant_emotion'], test_case_4['result'])
        result_5 = emotion_detector(test_case_5['text'])
        self.assertEqual(result_5['dominant_emotion'], test_case_5['result'])
    

unittest.main()

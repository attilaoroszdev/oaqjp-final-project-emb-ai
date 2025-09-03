from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):

        test_case_1 = {'text': 'I am glad this happened', 'result': 'joy'}
        test_case_2 = {'text': 'I am really mad about this', 'result': 'anger'}
        test_case_3 = {'text': 'I feel disgusted just hearing about this', 'result': 'disgust'}
        test_case_4 = {'text': 'I am so sad about this', 'result': 'sadness'}
        test_case_5 = {'text': 'I am really afraid that this will happen', 'result': 'fear'}

        self.assertEqual(emotion_detector(test_case_1['text']), test_case_1['result'])
        self.assertEqual(emotion_detector(test_case_2['text']), test_case_2['result'])
        self.assertEqual(emotion_detector(test_case_3['text']), test_case_3['result'])
        self.assertEqual(emotion_detector(test_case_4['text']), test_case_4['result'])
        self.assertEqual(emotion_detector(test_case_5['text']), test_case_5['result'])

unittest.main()
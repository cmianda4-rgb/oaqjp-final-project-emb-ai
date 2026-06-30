import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector("I am so happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am so angry that I want to break things!")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("I am very disgusted at the smell of this food")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am so sad about the loss of my friend")
        self.assertEqual(result['dominant_emotion'], 'sadness')

        result = emotion_detector("I am very afraid that I might fail this exam")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
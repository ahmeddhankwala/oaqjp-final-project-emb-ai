from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Testcase 1
        self.assertEqual(emotion_detector('I am glad this happened')['dominant_emotion'],'joy')
        # Testcase 2
        self.assertEqual(emotion_detector('I am really mad about this')['dominant_emotion'],'anger')
        # Testcase 3
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'],'disgust')
        # Testcase 4
        self.assertEqual(emotion_detector('I am so sad about this')['dominant_emotion'],'sadness')
        # Testcase 5
        self.assertEqual(emotion_detector('I am really afraid that this will happen')['dominant_emotion'],'fear')

unittest.main()
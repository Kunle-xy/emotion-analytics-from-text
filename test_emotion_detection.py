from EmotionDetection import *
import unittest

response, code = emotion_detection.emotion_detector("this text is used for testing")
class Testresponse_code(unittest.TestCase):
    """
    tests response attributes
    """
    
    def test_response_code(self):
        self.assertEqual(code, 200)
    
    def test_response_attribute(self):
        self.assertIn("dominant_emotion", response)
        
if __name__ == '__main__':
    unittest.main()
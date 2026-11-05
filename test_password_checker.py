import unittest
from password_checker import check_password

class TestPasswordChecker(unittest.TestCase):
    def test_weak_password(self):
        result = check_password("hello")
        self.assertEqual(result["strength"], "Weak")
    
    def test_medium_password(self):
        result = check_password("hello123")
        self.assertEqual(result["strength"], "Medium")
    
    def test_strong_password(self):
        result = check_password("Hello123!")
        self.assertEqual(result["strength"], 'Strong')
        
    def test_score(self):
        result = check_password("Hello123!")
        self.assertEqual(result["score"], 5)
    
    def test_feedback(self):
        result = check_password("Hello123!")
        self.assertEqual(result["feedback"], [])

if __name__ == "__main__":
    unittest.main()
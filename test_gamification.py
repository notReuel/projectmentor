import unittest
from utils.gamification import award_badges

class TestGamification(unittest.TestCase):
    def test_award_badges_reading(self):
        # When reading_level is high (>= 2), we expect a "Reading Prodigy" badge.
        results = {"reading_level": 3, "math_level": 1, "writing_assessment_completed": False}
        badges = award_badges(results)
        self.assertIn("Reading Prodigy", badges)
    
    def test_award_badges_math(self):
        # When math_level is high (>= 2), we expect a "Math Whiz" badge.
        results = {"reading_level": 1, "math_level": 3, "writing_assessment_completed": False}
        badges = award_badges(results)
        self.assertIn("Math Whiz", badges)
    
    def test_award_badges_writing(self):
        # When writing assessment is completed, we expect a "Writing Star" badge.
        results = {"reading_level": 1, "math_level": 1, "writing_assessment_completed": True}
        badges = award_badges(results)
        self.assertIn("Writing Star", badges)

if __name__ == '__main__':
    unittest.main()

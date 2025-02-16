import unittest
from utils.learner_profiles import generate_learner_profile

class TestLearnerProfile(unittest.TestCase):
    def test_generate_profile_beginner(self):
        # Beginner learner with low levels
        results = {"reading_level": 1, "math_level": 1, "writing_assessment_completed": False}
        profile = generate_learner_profile(results)
        
        self.assertEqual(profile["category"], "Beginner")
        self.assertIn("You are starting your learning journey!", profile["message"])
    
    def test_generate_profile_advanced(self):
        # Advanced learner with high levels
        results = {"reading_level": 3, "math_level": 3, "writing_assessment_completed": True}
        profile = generate_learner_profile(results)

        self.assertEqual(profile["category"], "Advanced")
        self.assertIn("You are doing great!", profile["message"])

if __name__ == '__main__':
    unittest.main()

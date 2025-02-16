import unittest
from utils.analytics import calculate_progress  # Ensure this import works

class TestAnalytics(unittest.TestCase):

    def test_progress_calculation_improvement(self):
        previous = {"reading_level": 50, "math_level": 60}
        current = {"reading_level": 70, "math_level": 80}
        progress = calculate_progress(previous, current)

        print("DEBUG - Test improvement:", progress)  # Debugging line

        self.assertGreater(progress["reading_level_improvement"], 0)  # ✅ Corrected key
        self.assertGreater(progress["math_level_improvement"], 0)  # ✅ Corrected key

    def test_progress_no_change(self):
        previous = {"reading_level": 50, "math_level": 60}
        current = {"reading_level": 50, "math_level": 60}
        progress = calculate_progress(previous, current)

        print("DEBUG - Test no change:", progress)  # Debugging line

        self.assertEqual(progress["reading_level_improvement"], 0)  # ✅ Corrected key
        self.assertEqual(progress["math_level_improvement"], 0)  # ✅ Corrected key

if __name__ == "__main__":
    unittest.main()

import unittest
import os
import json
from utils.progress_tracker import save_progress, load_progress

class TestProgressTracker(unittest.TestCase):
    def setUp(self):
        # Use a test file to avoid affecting production data.
        self.test_file = "test_progress_data.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def tearDown(self):
        # Clean up test file after each test.
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_save_and_load_progress(self):
        # Define test data
        test_data = {
            "reading_level": 2,
            "math_level": 3,
            "writing_assessment_completed": True
        }
        # Save the progress data to our test file.
        save_progress(test_data, filename=self.test_file)
        # Load the progress data from the file.
        loaded_data = load_progress(filename=self.test_file)
        # Ensure at least one entry exists.
        self.assertTrue(len(loaded_data) > 0)
        # Check that the last entry matches our test data.
        self.assertEqual(loaded_data[-1], test_data)

if __name__ == '__main__':
    unittest.main()

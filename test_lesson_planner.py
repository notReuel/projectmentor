import unittest
from utils.lesson_planner import generate_lesson_plan

class TestLessonPlanner(unittest.TestCase):
    def test_lesson_plan_for_beginners(self):
        # For beginners, extra hours should be allocated.
        results = {"reading_level": 1, "math_level": 1, "writing_assessment_completed": False}
        plan = generate_lesson_plan(results)
        # Expect additional hours beyond the base values.
        self.assertGreater(plan["reading_hours"], 40)
        self.assertGreater(plan["math_hours"], 30)
        self.assertGreater(plan["writing_hours"], 30)
    
    def test_lesson_plan_for_advanced(self):
        # For advanced learners, use the base allocation.
        results = {"reading_level": 3, "math_level": 3, "writing_assessment_completed": True}
        plan = generate_lesson_plan(results)
        # Base reading = 40, writing = 30, math = 30.
        self.assertEqual(plan["reading_hours"], 40)
        self.assertEqual(plan["writing_hours"], 30)
        self.assertEqual(plan["math_hours"], 30)

if __name__ == '__main__':
    unittest.main()

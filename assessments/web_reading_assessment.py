# assessments/web_reading_assessment.py

from difflib import SequenceMatcher

def calculate_accuracy(expected, transcript):
    """
    Calculate the similarity ratio between the expected word and the transcribed text.
    
    Args:
        expected (str): The word the learner was supposed to say.
        transcript (str): The transcribed text from the learner.
        
    Returns:
        float: Accuracy as a value between 0 and 1.
    """
    if not transcript:
        return 0.0
    return SequenceMatcher(None, expected.lower(), transcript.lower()).ratio()

def process_reading_assessment(transcript, expected_word):
    """
    Process the reading assessment by comparing the transcribed text with the expected word.
    
    Args:
        transcript (str): The transcribed text from the learner.
        expected_word (str): The expected word.
        
    Returns:
        dict: A dictionary containing the accuracy score.
    """
    accuracy = calculate_accuracy(expected_word, transcript)
    return {"accuracy": accuracy}

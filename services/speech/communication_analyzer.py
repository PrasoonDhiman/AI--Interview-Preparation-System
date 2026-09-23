import re

# Common filler words
FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "basically",
    "actually",
    "you know",
    "sort of",
    "kind of",
    "hmm",
]


def calculate_wpm(transcript, duration):
    """
    Calculate Words Per Minute.
    """

    if duration <= 0:
        return 0

    word_count = len(transcript.split())
    wpm = (word_count / duration) * 60

    return round(wpm, 2)


def speaking_speed_feedback(wpm):
    """
    Give feedback based on speaking speed.
    """

    if wpm < 80:
        return "Too Slow"

    elif wpm <= 140:
        return "Good"

    elif wpm <= 180:
        return "Fast"

    else:
        return "Too Fast"


def count_filler_words(transcript):
    """
    Count the number of filler words.
    """

    text = transcript.lower()
    count = 0

    for word in FILLER_WORDS:
        count += text.count(word)

    return count


def vocabulary_score(transcript):
    """
    Calculate vocabulary richness percentage.
    """

    words = transcript.lower().split()

    if len(words) == 0:
        return 0

    unique_words = len(set(words))

    score = (unique_words / len(words)) * 100

    return round(score, 2)


def vocabulary_feedback(score):
    """
    Provide feedback for vocabulary usage.
    """

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Poor"


def analyze_communication(transcript, duration):
    """
    Complete communication analysis.
    """

    wpm = calculate_wpm(transcript, duration)

    filler_count = count_filler_words(transcript)

    vocab_score = vocabulary_score(transcript)

    report = {

        "wpm": wpm,

        "speaking_speed":
            speaking_speed_feedback(wpm),

        "filler_words":
            filler_count,

        "vocabulary_score":
            vocab_score,

        "vocabulary_feedback":
            vocabulary_feedback(vocab_score)

    }

    return report
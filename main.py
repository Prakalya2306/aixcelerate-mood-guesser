train_data = [
("I got full marks in the test today!", "Happy"),
("We won the college cricket match", "Happy"),
("My friends planned a surprise party for me", "Happy"),
("The food in the canteen was really tasty", "Happy"),
("I am so excited for the weekend trip", "Happy"),
("Our project got selected for the exhibition", "Happy"),
("I finally learned how to ride a bicycle", "Happy"),
("Mom made my favourite sweets today", "Happy"),
("I lost my phone on the bus", "Sad"),
("I failed in the mathematics exam", "Sad"),
("My best friend is moving to another city", "Sad"),
("It rained and our picnic was cancelled", "Sad"),
("I missed the last bus and felt very upset", "Sad"),
("My laptop stopped working before the submission", "Sad"),
("I felt lonely during the long holidays", "Sad"),
]

practice_data = [
("I won a medal in the sports meet", "Happy"),
("I lost my notebook before the exam", "Sad"),
("My friends gave me a lovely surprise", "Happy"),
("The train was late and I felt upset", "Sad"),
("Today was a great day", "Happy"),
]

# ---------- Helper: ignore capitals and punctuation ----------
def clean_words(sentence):
    sentence = sentence.lower()
    cleaned = ""
    for ch in sentence:
        cleaned += ch if ch.isalpha() else " "   # punctuation becomes a space
    return cleaned.split()

# ---------- Level 1 ----------
def count_moods(data):
    happy = 0
    sad = 0
    for sentence, mood in data:
        if mood == "Happy":
            happy += 1
        elif mood == "Sad":
            sad += 1
    return happy, sad

# ---------- Level 2 ----------
# N = last digit of roll number (use 10 if the last digit is 0).
# Roll number ends in 0, so N = 10.
N = 10

# Words ranked from most to least useful (strong mood words that are
# not everyday words). Only the first N of each are used.
_happy_ranked = ["won", "surprise", "excited", "favourite", "tasty",
                 "finally", "great", "party", "selected", "learned"]
_sad_ranked = ["lost", "failed", "upset", "lonely", "cancelled",
               "missed", "felt", "stopped", "moving", "rained"]

happy_words = _happy_ranked[:N]
sad_words = _sad_ranked[:N]
assert len(happy_words) == N and len(sad_words) == N

def guess_mood(sentence):
    words = clean_words(sentence)
    h = sum(1 for w in words if w in happy_words)
    s = sum(1 for w in words if w in sad_words)
    if h > s:
        return "Happy"
    if s > h:
        return "Sad"
    # Tie: choose Happy, because train_data has slightly more Happy (8) than Sad (7).
    return "Happy"

# ---------- Level 3 ----------
def accuracy(predict, data):
    right = 0
    for sentence, mood in data:
        guess = predict(sentence)
        print(f"  {sentence!r} -> {guess} (actual {mood})")
        if guess == mood:
            right += 1
    return 100 * right / len(data)

# ---------- Learning part ----------
def learn_scores(data):
    scores = {}
    for sentence, mood in data:
        for w in clean_words(sentence):
            scores[w] = scores.get(w, 0) + (1 if mood == "Happy" else -1)
    return scores

learned = learn_scores(train_data)

def guess_mood_learned(sentence):
    total = sum(learned.get(w, 0) for w in clean_words(sentence))  # unseen word = 0
    return "Happy" if total > 0 else "Sad"

if __name__ == "__main__":
    print("Level 1:", count_moods(train_data))
    print("\nLevel 2/3 (clue words, N =", N, ")")
    print("  happy_words:", happy_words)
    print("  sad_words:  ", sad_words)
    print(f"  Accuracy: {accuracy(guess_mood, practice_data):.0f}%")
    print("\nLearned scores method")
    print(f"  Accuracy: {accuracy(guess_mood_learned, practice_data):.0f}%")
    demo = learn_scores([("good party","Happy"),("good exam","Happy"),
                         ("bad exam","Sad"),("bad day","Sad")])
    print("\nNote example scores:", demo)
    for s in ["good party today", "bad exam day", "not good"]:
        print(" ", s, sum(demo.get(w, 0) for w in s.split()))

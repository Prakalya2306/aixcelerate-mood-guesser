# aixcelerate-mood-guesse

# Mood Guesser

## Level 3: Testing
Accuracy on the 5 practice sentences: 100 %

1. Which sentence went wrong (or was closest to going wrong), and why?
None went wrong. "My friends gave me a lovely surprise" was closest, because it is Happy only through the single word "surprise" ("lovely" is not in my list). Also, "felt" is in my Sad list, so a sentence like "I felt happy" would be marked Sad.

2. One change that would make my program better:
Handle negation words like "not" (so "not happy" is Sad), or add more clue words.

## Learning questions
1. Total score of "good party today" and its mood: 2 + 1 + 0 = 3, so Happy ("today" is unseen, so it scores 0).
2. Total score of "bad exam day" and its mood: -2 + 0 + (-1) = -3, so Sad.
3. Why did "exam" get a score of 0, and is that good or bad? "exam" appears once in a Happy sentence and once in a Sad sentence, so +1 and -1 cancel out. This is good because "exam" is not a mood word, so it should not push the answer. It is bad because with so little data the program cannot tell if a word is really neutral.
4. Why is "not good" labelled Happy by this method, and how could it be fixed? "not" is unseen (score 0) and "good" is +2, so the total is +2 and it says Happy. The method adds up single words and ignores word order. It could be fixed by flipping the score of the word after "not", or by scoring pairs of words like "not good".

## AI declaration
I used an AI tool: yes
If yes, what I asked it: I asked Claude to help me write the Python program (count_moods, guess_mood, learn_scores and guess_mood_learned), to check it against the task requirements, and to help draft my README answers. I set N = 10 for my roll number and checked the output myself.

## Reflection
What was hardest, and what I learned that I did not know before: The hardest part was choosing only 10 words for each list, because every word matters. I learned that a program can find clue words by itself by counting words in examples, and that it can still be fooled by words like "not" because it ignores word order.

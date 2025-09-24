# Member D(ingmar): Word-level statistics Part 2
import string
from collections import defaultdict

'''
#sample
sentiment_lexicon = {
    'love': 10, 'loved': 10, 'amazing': 9, 'great': 8, 'good': 7, 'excellent': 10, 'fantastic': 10,
    'bad': -7, 'boring': -8, 'terrible': -10, 'awful': -10, 'worst': -10, 'disappointing': -8,
    'mediocre': -4, 'okay': 1, 'enjoyable': 6, 'predictable': -5, 'fun': 6, 'slow': -5,
    'recommend': 8, 'not': -5, 'poor': -6, 'weak': -6, 'strong': 6, 'beautiful': 9,
    'ugly': -8, 'flat': -6, 'brilliant': 9, 'stunning': 9, 'dull': -7
}

positive_reviews = [
    "I loved the movie. It was amazing and fun to watch.",
    "The acting was brilliant and the visuals were stunning.",
    "A fantastic story with great characters and beautiful direction.",
    "Highly recommend to anyone who enjoys good cinema."
]

negative_reviews = [
    "The movie was boring and predictable. A disappointing experience.",
    "Terrible pacing and flat characters. Very dull.",
    "I did not enjoy the film. It was bad and the dialogue was awful.",
    "One of the worst and most mediocre movies I've seen."
]
'''

# Tokenization: lowercase, remove punctuation, split on whitespace
def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split()

# Count words in each review set
def build_word_set(reviews):
    word_set = set()
    for review in reviews:
        words = tokenize(review)
        word_set.update(words)
    return word_set


def highlight_interesting_words(positive_reviews,negative_reviews,sentiment_lexicon,n):
    #Computes and outputs data for interesting words
    
    
    # Get sets of words from both review types
    positive_words = build_word_set(positive_reviews)
    negative_words = build_word_set(negative_reviews)


    #print(positive_words,negative_words)

    # Find overlapping words
    common_words = set(positive_words).intersection(set(negative_words))

    # Calculate average sentiment per common word
    combined_reviews = positive_reviews + negative_reviews

    # Track sentiment per word
    sentiment_map = defaultdict(list)
    for review in combined_reviews:
        words = tokenize(review)
        review_score = sum(sentiment_lexicon.get(w, 0) for w in words)
        for w in words:
            sentiment_map[w].append(review_score)

    #print(sentiment_map)

    interesting_words = []

    for word in common_words:
        scores = sentiment_map[word]
        if len(scores) >= 2:
            avg = sum(scores) / len(scores)
            polarity = max(scores) - min(scores)  # how "polarizing" the word is
            interesting_words.append((word, avg, polarity, len(scores)))

    #print(interesting_words)

    # Sort by polarity (difference between max and min score) - most "interesting" words
    for i in range(len(interesting_words)):
        for j in range(i + 1, len(interesting_words)):
            if (interesting_words[i][2] < interesting_words[j][2]):
                interesting_words[i], interesting_words[j] = interesting_words[j], interesting_words[i]
            elif interesting_words[i][2] == interesting_words[j][2]:
                if interesting_words[i][0] > interesting_words[j][0]:
                    interesting_words[i], interesting_words[j] = interesting_words[j], interesting_words[i]
    return interesting_words[:n]
'''
# Display results
results = highlight_interesting_words(positive_reviews,negative_reviews,sentiment_lexicon,10)
print(results)
print("Interesting words used in both positive & negative reviews:")
print(f"{'Word':12} | {'Avg Sentiment':>14} | {'Polarity':>8} | {'Count':>5}")
print("-" * 45)
for word, avg, diff, count in results:
    print(f"{word:12} | {avg:14.2f} | {diff:8.2f} | {count:5}")
    '''
    
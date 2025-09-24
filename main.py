# Main pipeline to connect all modules

from lexicon_setup import load_afinn
from review_sentiment import review_sentiment, classify_review
from word_insights import top_sentiment_words
from word_stats import average_word_sentiment, top_n_words
from word_stats_part_2 import highlight_interesting_words
from valid_segmentation import word_break
from sliding_window import sliding_window

# Example: load lexicon
afinn = load_afinn()

# Example: fake sample reviews (replace with real preprocessed data)
sample_reviews = [
    ["the", "movie", "was", "fantastic", "and", "inspiring"],
    ["boring", "plot", "and", "terrible", "acting"]
]
sample_labels = ["positive", "negative"]

# Review sentiment
for r, label in zip(sample_reviews, sample_labels):
    score = review_sentiment(r, afinn)
    prediction = classify_review(score)
    print(r, "=>", prediction, "(true:", label, ")")

# Word insights
pos_words, neg_words = top_sentiment_words(sample_reviews, afinn)
print("Top pos words:", pos_words)
print("Top neg words:", neg_words)

# Word stats
per_word_scores = average_word_sentiment(sample_reviews, afinn)
for key, value in per_word_scores.items():
    print(f"{key}: {value}")
word_scores = average_word_sentiment(sample_reviews, afinn)
print("Top 5 positive words:", top_n_words(word_scores, n=5, positive=True))
print("Top 5 negative words:", top_n_words(word_scores, n=5, positive=False))

# Word stats Part 2
results = highlight_interesting_words(positive_reviews,negative_reviews,afinn,10)
print(results)
print("Interesting words used in both positive & negative reviews:")
print(f"{'Word':12} | {'Avg Sentiment':>14} | {'Polarity':>8} | {'Count':>5}")
print("-" * 45)
for word, avg, diff, count in results:
    print(f"{word:12} | {avg:14.2f} | {diff:8.2f} | {count:5}")
    
# Valid Segmentation
valid_segmentations = word_break(string, word_dict)
print("A valid segmentation would be: "valid_segmentations[0])

# Sliding window
sw = sliding_window(sample_reviews[0], afinn, window_size=3)
print("Sliding window scores for review 1:", sw)

        
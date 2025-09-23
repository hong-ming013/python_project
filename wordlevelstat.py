from collections import Counter

def word_frequencies(reviews: list[list[str]]) -> Counter:
    """
    Counts all word frequencies across reviews.
    """
    counter = Counter()
    for r in reviews:
        counter.update(r)
    return counter

positive_words = {"great", "good", "excellent", "amazing", "awesome", "love", "like", "fantastic"}
negative_words = {"bad", "terrible", "awful", "poor", "hate", "dislike", "worst", "not"}

def count_sentiment_words(reviews: list[list[str]]) -> dict:
    """
    Counts positive and negative words across all reviews.
    Returns a dictionary with counts.
    """
    sentiment_counts = {"positive": 0, "negative": 0}

    for review in reviews:
        for word in review:
            word = word.lower()  # Normalize to lowercase
            if word in positive_words:
                print(word)
                sentiment_counts["positive"] += 1
            elif word in negative_words:
                print(word)
                sentiment_counts["negative"] += 1

    return sentiment_counts


def top_sentiment_words(reviews: list[list[str]], lexicon: dict, n=20):
    """
    Finds the most frequent positive and negative words.
    """
    freq = word_frequencies(reviews)
    pos_words = [(w, freq[w]) for w in freq if lexicon.get(w, 0) > 0]
    neg_words = [(w, freq[w]) for w in freq if lexicon.get(w, 0) < 0]

    pos_sorted = sorted(pos_words, key=lambda x: x[1], reverse=True)[:n]
    neg_sorted = sorted(neg_words, key=lambda x: x[1], reverse=True)[:n]

    return pos_sorted, neg_sorted


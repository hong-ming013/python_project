# Member D(ingmar): Word-level statistics (average scores)
from collections import defaultdict
def average_per_word_sentiment(reviews, lexicon):
    
    #Computes average sentiment score per word.
    #Returns dict {"ave sentiment score per word": avg_score}.
    
    word_totals = 0
    word_counts = 0

    for r in reviews:
        for w in r:
            word_counts = word_counts + 1
            if w in lexicon:
                word_totals = word_totals + lexicon[w]

    return {"average sentiment score per word": word_totals / word_counts}

def average_word_sentiment(reviews, lexicon):
    
    #Computes average sentiment score for each word across all reviews.
    #Returns dict {word: avg_score}.
    
    word_totals = {}
    word_counts = {}

    for r in reviews:
        for w in r:
            if w in lexicon:
                word_totals[w] = word_totals.get(w, 0) + lexicon[w]
                word_counts[w] = word_counts.get(w, 0) + 1

    return {w: word_totals[w] / word_counts[w] for w in word_totals}

def top_n_words(word_scores: dict, n, positive):
    #Returns the top N positive or negative words by average sentiment.
    #print(word_scores.items(),"ab",list(word_scores.items()))
    #items = list(word_scores.items())
    #print({word: score for word, score in word_scores.items() if score > 0},"abc")
    if positive:
        items = [(word, score) for word, score in word_scores.items() if score > 0]
    else:
        items = [(word, score) for word, score in word_scores.items() if score < 0]
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if positive:
                if (items[i][1] < items[j][1]):
                    items[i], items[j] = items[j], items[i]
                elif items[i][1] == items[j][1]:
                    if items[i][0] > items[j][0]:
                        items[i], items[j] = items[j], items[i]
            else:
                if (items[i][1] > items[j][1]):
                    items[i], items[j] = items[j], items[i]
                elif items[i][1] == items[j][1]:
                    if items[i][0] > items[j][0]:
                        items[i], items[j] = items[j], items[i]
                            
    return items[:n]

"""
lexicon = {
    'good': 7,
    'great': 8,
    'amazing': 9,
    'bad': -7,
    'terrible': -10,
    'boring': -8,
    'fun': 6,
    'okay': 1
}

reviews = [
    ['the', 'movie', 'was', 'good'],
    ['the', 'acting', 'was', 'amazing'],
    ['it', 'was', 'boring', 'and', 'bad'],
    ['fun', 'but', 'not', 'great'],
    ['okay', 'film']
]
result = average_word_sentiment(reviews, lexicon)
per_result = average_per_word_sentiment(reviews, lexicon)
for key, value in per_result.items():
    print(f"{key}: {value}")

print(result)
print(top_n_words(result,10,True))

# --- Display results ---
print("Top Positive Words:")
for word, score in top_n_words(result,10,True):
    print(f"{word:20} : {score:.3f}")

print("\nTop Negative Words:")
for word, score in top_n_words(result,10,False):
    print(f"{word:20} : {score:.3f}")
'''

import os
#memberA Hafi

def load_afinn(filepath="AFINN-en-165.txt") -> dict:
    lexicon = {}
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            word, score = line.strip().split("\t")
            lexicon[word] = int(score)
    return lexicon


def score_tokens(tokens: list[str], lexicon: dict) -> int:
    return sum(lexicon.get(w, 0) for w in tokens)


def sliding_window(tokens: list[str], lexicon: dict, window_size=20) -> list[int]:
    scores = []
    for i in range(0, len(tokens) - window_size + 1):
        window = tokens[i:i+window_size]
        scores.append(score_tokens(window, lexicon))
    return scores


# ---- NEW: handle a dataset of reviews ----
def load_reviews_from_folder(folder: str) -> list[list[str]]:
    """
    Loads reviews from a folder. Assumes each review is in a text file.
    Returns a list of token lists (each review already preprocessed).
    """
    reviews = []
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        with open(path, encoding="utf-8") as f:
            tokens = f.read().split()   # since preprocessed, split by space
            reviews.append(tokens)
    return reviews


def dataset_sentiments(pos_folder: str, neg_folder: str, lexicon: dict):
    """
    Computes sentiment scores for all positive and negative reviews.
    """
    pos_reviews = load_reviews_from_folder(pos_folder)
    neg_reviews = load_reviews_from_folder(neg_folder)

    pos_scores = [score_tokens(r, lexicon) for r in pos_reviews]
    neg_scores = [score_tokens(r, lexicon) for r in neg_reviews]

    print("Processed", len(pos_scores), "positive reviews")
    print("Processed", len(neg_scores), "negative reviews")
    print("Average score (positive reviews):", sum(pos_scores)/len(pos_scores))
    print("Average score (negative reviews):", sum(neg_scores)/len(neg_scores))

    return pos_scores, neg_scores


# ---------------- DEMO ----------------
if __name__ == "__main__":
    afinn = load_afinn("AFINN-en-165.txt")

    # Example: analyze dataset
    pos_scores, neg_scores = dataset_sentiments(
        "/Users/hafimeow/Desktop/python/progfundsproj/lexicon_demo/aclImdb/train/pos",  
        "/Users/hafimeow/Desktop/python/progfundsproj/lexicon_demo/aclImdb/train/neg",
        afinn
    )

    # Show first 5 results
    print("\nFirst 5 positive review scores:", pos_scores[:5])
    print("First 5 negative review scores:", neg_scores[:5])

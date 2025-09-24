#memberA Hafi
import os
import csv
from lexicon_demo import load_afinn, score_tokens  # <-- from your module

def load_reviews_from_folder(folder: str) -> list[list[str]]:
    """
    Loads reviews from a folder (pos/ or neg/).
    Returns a list of token lists.
    """
    reviews = []
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        with open(path, encoding="utf-8") as f:
            text = f.read()
            tokens = text.split()   # assumes preprocessed (space-separated)
            reviews.append(tokens)
    return reviews


def sliding_window(tokens: list[str], lexicon: dict, window_size=20) -> list[int]:
    """
    Computes sentiment scores over a sliding window of tokens.
    """
    scores = []
    for i in range(0, len(tokens) - window_size + 1):
        window = tokens[i:i+window_size]
        scores.append(score_tokens(window, lexicon))
    return scores


if __name__ == "__main__":
    # Paths to dataset
    pos_folder = "/Users/hafimeow/Desktop/python/progfundsproj/lexicon_demo/aclImdb/train/pos"
    neg_folder = "/Users/hafimeow/Desktop/python/progfundsproj/lexicon_demo/aclImdb/train/neg"

    # Load reviews
    pos_reviews = load_reviews_from_folder(pos_folder)
    neg_reviews = load_reviews_from_folder(neg_folder)
    print("Loaded", len(pos_reviews), "positive reviews")
    print("Loaded", len(neg_reviews), "negative reviews")

    # Load lexicon
    afinn = load_afinn("AFINN-en-165.txt")

    # Score all reviews
    pos_scores = [score_tokens(r, afinn) for r in pos_reviews]
    neg_scores = [score_tokens(r, afinn) for r in neg_reviews]

    print("Average sentiment of positive reviews:", sum(pos_scores)/len(pos_scores))
    print("Average sentiment of negative reviews:", sum(neg_scores)/len(neg_scores))

    # --- SAVE RESULTS TO CSV ---
    with open("review_scores.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["review_id", "label", "score"])
        for i, s in enumerate(pos_scores):
            writer.writerow([f"pos_{i}", "positive", s])
        for i, s in enumerate(neg_scores):
            writer.writerow([f"neg_{i}", "negative", s])
    print("Saved review scores to review_scores.csv")

    # --- SLIDING WINDOW DEMO (1 review) ---
    demo_review = pos_reviews[0]  # pick the first positive review
    sw_scores = sliding_window(demo_review, afinn, window_size=20)
    print("\nSliding window scores for first positive review:", sw_scores[:10], "...")

import random
from collections import defaultdict

class MarkovText:
    def __init__(self, corpus):
        self.corpus = corpus.split()
        self.term_dict = self.get_term_dict()

    def get_term_dict(self):
        term_dict = defaultdict(list)
        for i in range(len(self.corpus) - 1):
            key = self.corpus[i]
            next_word = self.corpus[i + 1]
            term_dict[key].append(next_word)
        return dict(term_dict)

    def generate(self, term_count=15, seed_term=None):
        # Choose starting word
        if seed_term:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current_word = seed_term
        else:
            current_word = random.choice(list(self.term_dict.keys()))

        generated = [current_word]

        # Generate the sequence
        for _ in range(term_count - 1):
            if current_word not in self.term_dict or not self.term_dict[current_word]:
                break
            next_word = random.choice(self.term_dict[current_word])
            generated.append(next_word)
            current_word = next_word

        # ✅ Make sure you RETURN the result
        return " ".join(generated)

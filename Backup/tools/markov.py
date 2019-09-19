import nltk

def generate_markov_text(context, max):
    tokens = nltk.word_tokenize(context)
    seed = random.randint(0, len(tokens) -3)
    seed_word, next_word = tokens[seed], tokens[seed+1]
    w1, w2 = seed_word, next_word
    gen_words = []
    for i in range(max):
        gen_words.append(w1)
        w1, w2 = w2, random.choice([w1, w2])
    gen_words.append(w2)
    return ' '.join(gen_words)

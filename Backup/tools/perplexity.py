perplexity = 1
N = 0

for word in testset:
    if word in unigram:
        N += 1
        perplexity = perplexity * (1/unigram[word])
perplexity = pow(perplexity, 1/float(N))

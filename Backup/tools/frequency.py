def get_word_counts(input_str, limit = 100):
        input_str = PreprocessManager.remove_non_ascii(input_str)
        wordnet_lemmatizer = WordNetLemmatizer()
        snowball_stemmer = EnglishStemmer()
        tokenized_text = CountVectorizer().build_tokenizer()(input_str.lower())
        tokenized_text = [word for word in tokenized_text if len(word) > 1]  # Filter some small words
        #tokenized_text = [word for word in tokenized_text if not word.isnumeric()]
        filtered_words = [word for word in tokenized_text if word not in stopwords.words('english')]
        stemmed_list = [wordnet_lemmatizer.lemmatize(w) for w in filtered_words]
        # Calculate frequency distribution
        frequency_dist = nltk.FreqDist(stemmed_list)

        # Output top 50 words
        result = dict()
        for word, frequency in frequency_dist.most_common(limit):
            # print(u'{};{}'.format(word, frequency))
            result[word] = frequency
        return result

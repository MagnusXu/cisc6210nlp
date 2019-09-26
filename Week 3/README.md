# Homework No. 3
### CISC 6210 Natural Language Processing Due Date: 10/2/2019
### Fall 2019 Points: 20
### Goal
- Practice Naïve Bayes and Logistic Regression Classifiers
- Perform sentiment analysis on review datasets
- Get familiar with Sklearn package
## Data Set
The dataset folder: http://storm.cis.fordham.edu/~yli/data/electronics

Data courtesy: https://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html
## Tasks
1. Study the review datasets.
- a. Preprocess its text content. Open datasets for positive review and
negative reviews, only consider the contents stored in <review_text>
tags. Perform tokenization, stemming (PorterStemmer in NLTK), you
could try remove/keep words from stop word list - NLTK English Stop
Word List and see the difference. Keep only letters and numbers in the
cleaned text.
- b. Find 20,50,100 most frequent words in the dataset of each class and
show them in WordCloud. Investigate how many words show in both
classes.
- c. For each shared word between two classes in two scenarios
(remove/keep stop words), compare their frequencies. Think about
what you would like to do with these common words, and whether you
would like to remove stop words in the following sentimental analysis
task.

2. Labeled datasets of each class are divided to two parts, training and test, you
could try different ratio such as 70/30 or 80/20.

3. Use NaiveBayes Classifier in Sklearn package to perform Sentiment Analysis
on the given training dataset.
Perform the task with word counts and word occurrence
(Sklearn.feature_extraction.text.CountVectorizer) in document representation,
compare their performance in terms of the precision, recall, and f-score on the
test set.

4. Perform Logistic Regression on the same split of labeled datasets and also
vector document representation of word counts and word occurrence.
Compare its performance vs. Naïve Bayes classifier.
5. With the help of the trained Logistic Regression model, find out the most
important words for both positive and negative classes. Show these words in
wordCloud.

import nltk
from textblob import TextBlob

# Need a pre-processing step to pick up names of players, teams, countries that aren't
# properly capitalised

print nltk.pos_tag(nltk.word_tokenize("games Gareth Bale scored in in 2012/2013"))
print nltk.pos_tag(nltk.word_tokenize("games in which Gareth Bale scored"))

from nltk.corpus import brown

brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)

word_tag_pairs = nltk.bigrams(brown_news_tagged)

wsj = nltk.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)

idx1 = wsj.index(('kicked', 'VD'))

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
	print tag, tagdict[tag]

brown_learned_text = brown.words(categories='learned')
sorted(set(b for (a, b) in nltk.ibigrams(brown_learned_text) if a == 'often'))

brown_lrnd_tagged = brown.tagged_words(categories='learned', simplify_tags=True)
tags = [b[1] for (a, b) in nltk.ibigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()

def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print w1, w2, w3

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)


from nltk.corpus import names
import random
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])    

import random
random.shuffle(names)

def gender_features(word):
    return {'last_letter': word[-1]}

    
def gender_features2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features

def create_classifier(fn):
    featuresets = [(fn(n), g) for (n,g) in names]
    train_set, test_set = featuresets[500:], featuresets[:500]
    return nltk.NaiveBayesClassifier.train(train_set)

classifier = create_classifier(gender_features2)

print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(5)

train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]

train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)
    
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

def gender_features(word):
    return {'suffix1': word[-1:], 'suffix2': word[-2:]}


    
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)

# movies    
from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category)
                for category in movie_reviews.categories()
                for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
    
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set) 

print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(5)

from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    suffix_fdist.inc(word[-1:])
    suffix_fdist.inc(word[-2:])
    suffix_fdist.inc(word[-3:])

common_suffixes = suffix_fdist.keys()[:100]
print common_suffixes 
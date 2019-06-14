from nltk.stem.snowball import SnowballStemmer
from scipy import *


class LSI(object):
    def __init__(self, stopwords, articles):
        self.articles = []
        self.wdict = []

        self.dictionary = []
        self.stopwords = stopwords
        self.wordsNumber = 0

        self.i = 0

        for article in articles:
            self.addArticleDic(article, self.i)

            self.i += 1

    def dictionaryArticle(self, word, i):

        word = self.processingIgnoreChars(word)
        stemmer = SnowballStemmer("russian")
        word = stemmer.stem(word)
        print(word)
        if not word in self.dictionary[i]:
            self.dictionary[i].append(word)
        else:
            self.dictionary[i].append(word)

    def addArticleDic(self, article, i):
        self.dictionary.append([])
        self.wdict.append({})
        saveProblemWord = ""
        for word in article.split():

            if str(word).endswith('-'):
                saveProblemWord = word
                continue
            word = saveProblemWord + word
            saveProblemWord = ""

            self.dictionaryArticle(word, i)

        for word in self.dictionary[i]:
            if word in self.stopwords:
                self.dictionary[i].remove(word)

        for word in self.dictionary[i]:
            if word in self.wdict[i]:
                self.wdict[i][word] += 1

            else:
                self.wdict[i][word] = 1

    def hyphenProcessing(self, article):

        print(article.split('-'))

    def processingIgnoreChars(self, word):

        ignorechars = ''',\n:.;-'!'''

        if type(ignorechars) == unicode:
            ignorechars = ignorechars.encode('utf-8')

        if type(word) == unicode:
            word = word.encode('utf-8')

        word = word.lower().translate(None, ignorechars)
        word = word.decode('utf-8')

        return word

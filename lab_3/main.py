"""
Labour work #3
 Building an own N-gram model
"""

import math
from random import randint

REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()


class WordStorage:
    def __init__(self):
        self.storage = {}

    def put(self, word: str) -> int:
        if word != str(word) or word in self.storage:
            return None
        count = randint(1,1000000)
        while count in self.storage.values() and count is None:
             count += 1
        self.storage[word] = count
        return count




    def get_id_of(self, word: str) -> int:
        if word in self.storage:
            return self.storage.get(word)
        return - 1



    def get_original_by(self, id: int) -> str:
        if id in self.storage.values() and isinstance(id, int):
            id = list(self.storage.values()).index(id)
            return list(self.storage.keys())[id]
        return 'UNK'


    def from_corpus(self, corpus: tuple):
        if isinstance(corpus, tuple):
            for word in corpus:
                self.put(word)
        return corpus


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        if sentence is None or sentence != tuple(sentence) or sentence == ():
            return 'ERROR'
        combinations = []
        start = 0
        while start != len(sentence) - 1:
            possible_variants = sentence[start:start + self.size]
            possible_variants = tuple(possible_variants)
            combinations.append(possible_variants)
            start += 1
        for element in combinations:
            if len(element) == self.size:
                freq = combinations.count(element)
                self.gram_frequencies[element] = freq
        return 'OK'


    def calculate_log_probabilities(self):
        variants = []
        for key in self.gram_frequencies.keys():
            variants.append(key)
        count = 0
        while count != len(variants):
            for gram in variants:
                all_gram = []
                gram_count = self.gram_frequencies[gram]
                for extra_gram in variants:
                    if gram[:-1] == extra_gram[:-1]:
                        all_gram.append(self.gram_frequencies[extra_gram])
                count_all_gram = sum(all_gram)
                e_log = math.log(gram_count / count_all_gram)
                self.gram_log_probabilities[gram] = e_log
                count += 1

    def predict_next_sentence(self, prefix: tuple) -> list:
        if self.gram_log_probabilities is None or self.gram_log_probabilities == {}:
            return []
        prefix = list(prefix)
        count = 0
        values = []
        variants = []
        for key in self.gram_log_probabilities.keys():
            variants.append(key)
        while count != len(variants):
            for n_gram in variants:
                if list(n_gram[:-1]) == prefix[1 - self.size:]:
                    values.append(self.gram_log_probabilities[n_gram])
            if values == []:
                return prefix
            max_val = max(values)
            for key, value in self.gram_log_probabilities.items():
                if value == max_val:
                    prefix.append(key[-1])
            values = []
            count += 1
        return prefix


def encode(storage_instance, corpus) -> list:
    new_corpus = []
    new_sentence = []
    for sentence in corpus:
        for word in sentence:
            new_word = storage_instance.put(word)
            new_sentence.append(new_word)
        new_corpus.append(new_sentence)
    return new_corpus


def split_by_sentence(text: str) -> list:
    marks = [',', ':', '"', '`', '[', ']', '@', '&', "'", '-',
        '$', '^', '*', '(', ')','_', 'вЂњ', 'вЂќ', 'вЂ™', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n' ]
    if text == '' or text is None:
        return []
    if not isinstance(text, str):
        text = str(text)
    text1 = ''
    for element in text:
        if element not in marks:
            text1 += element
    points = ['!','?','...']
    for element in points:
            text1 = text1.replace(element, '.')
    text1 = text1.lower()
    text2 = text1.split('.')
    text2.remove(text2[-1])
    if text2 == ['']:
        return []
    final = []
    for sentence in text2:
        new_list = ['<s>']
        list_sent = sentence.split(' ')
        for element in list_sent:
            if element is not '':
                new_list.append(element)
        new_list.append('</s>')
        final.append(new_list)
    return final



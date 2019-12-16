import math


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    if not texts or not isinstance(texts, list):
        return []
    clean_token_corpus = []
    for one_text in texts:
        if one_text and isinstance(one_text, str):
            while '<br />' in one_text:
                one_text = one_text.replace("<br />", " ")
            clean_token_text = []
            words = one_text.split(" ")
            for word in words:
                new_word = ""
                if not word.isalpha():
                    for i in word.lower():
                        if i.isalpha():
                            new_word += i
                    if new_word:
                        clean_token_text.append(new_word.lower())
                else:
                    clean_token_text.append(word.lower())
            clean_token_corpus += [clean_token_text]
    return clean_token_corpus

class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if self.corpus:
            for part in self.corpus:
                tf_values = {}
                if part:
                    len_text = len(part)
                    for word in part:
                        if not isinstance(word, str):
                            len_text -= 1
                    for word in part:
                        if isinstance(word, str) and word not in tf_values:
                            count_word = part.count(word)
                            tf_values[word] = count_word / len_text
                    self.tf_values += [tf_values]
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            for part in self.corpus:
                if not part:
                    continue
                new_corpus = []
                for word in part:
                    if word not in new_corpus and isinstance(word, str):
                        new_corpus += [word]
                count_words = {}
                for word in new_corpus:
                    count_word = 0
                    for text_again in self.corpus:
                        if not text_again or word in text_again:
                            count_word += 1
                    count_words[word] = count_word
                    if count_words.get(word) != 0:
                        len_c = len(self.corpus)
                        self.idf_values[word] = math.log(len_c / count_words.get(word))
            return self.idf_values

    def calculate(self):
        if self.idf_values and self.tf_values:
            for part in self.tf_values:
                tf_idf_values = {}
                for word, tf_value in part.items():
                    tf_idf_values[word] = tf_value * self.idf_values.get(word)
                self.tf_idf_values += [tf_idf_values]
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_dict = self.tf_idf_values[document_index]
        if not word in tf_idf_dict:
            return ()
        list_tf_idf = sorted(tf_idf_dict, key=tf_idf_dict.__getitem__, reverse=True)
        return tf_idf_dict.get(word.lower()), list_tf_idf.index(word.lower())


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))

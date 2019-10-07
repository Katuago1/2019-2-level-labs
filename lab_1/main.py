"""
Labour work #1
Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) :
    super_dict = {}
    if text == "" or text is None:
        return super_dict
    text = str(text)
    text_lower = text.lower()
    for s in text_lower:
        if not s.isalpha():
            text_lower = text_lower.replace(s, ' ')
    split = text_lower.split()
    for word in split:
        word = word.lower()
        if word in super_dict:
            value = super_dict[word]
            super_dict[word] = value + 1
        else:
            super_dict[word] = 1
    return super_dict

def filter_stop_words(super_dict: dict, stop_words: tuple) -> dict:
    dict_filter = {}
    if super_dict is not None and stop_words is not None:
        for k, v in super_dict.items():
            if k == str(k):
                if k not in stop_words:
                    dict_filter.update({k: v})
    return dict_filter

def get_top_n(super_dict: dict, top_n: int):
    if not isinstance(top_n, int):
        super_dict = ()
        return super_dict
    if top_n < 0:
        top_n = 0
    elif top_n > len(super_dict):
        top_n = len(super_dict)
    words_top = sorted(super_dict, key=lambda x: int(super_dict[x]), reverse=True)
    top_of_the_top = tuple(words_top[:top_n])
    return top_of_the_top


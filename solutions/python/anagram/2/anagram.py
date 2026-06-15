"""
To find anagrams
"""  
from collections import Counter

def find_anagrams(word, candidates):  
    """  
    :param word:str -Given the target word  
    :param candidates:list -the candidate words list  
    :return :list -To given the target word the candidate words list  
    """  
    word_freq = Counter(word.lower())  
    anagrams = []  
    for candidate in candidates:  
        if len(candidate) != len(word):  
            continue  
        candidate_freq = Counter(candidate.lower())  
        if word_freq == candidate_freq and word.lower() != candidate.lower():  
            anagrams.append(candidate)  

    return anagrams

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:18:39 2022

@author: jense
"""

text = ('i have to write some words that repeat in some way for homework '
        'i hope this example is enough of words repeating for my homework')

word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
print (f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words:', len(word_counts))
    
    
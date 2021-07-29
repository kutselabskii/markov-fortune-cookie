# Adapted and modified code from https://github.com/StrikingLoo/ASOIAF-Markov/blob/master/ASOIAF.ipynb

from random import random

from scipy.sparse import dok_matrix
import numpy as np

class Chain:
    def __init__(self, data, size):
        self.size = size
    
        self.distinct_words = list(set(data))
        word_idx_dict = {word: i for i, word in enumerate(self.distinct_words)}
        
        sets = [' '.join(data[i: i + self.size]) for i, _ in enumerate(data[:-self.size])]

        sets_count = len(list(set(sets)))
        self.dmatrix = dok_matrix((sets_count, len(self.distinct_words)))

        distinct_sets = list(set(sets))
        self.word_ids = {word: i for i, word in enumerate(distinct_sets)}

        for i, word in enumerate(sets[:-self.size]):
            word_sequence_idx = self.word_ids[word]
            next_word_idx = word_idx_dict[data[i + self.size]]
            self.dmatrix[word_sequence_idx, next_word_idx] += 1


    def sample_next_word_after_sequence(self, word_sequence, alpha = 0):
        next_word_vector = self.dmatrix[self.word_ids[word_sequence]] + alpha
        likelihoods = next_word_vector / next_word_vector.sum()
        return self.weighted_choice(self.distinct_words, likelihoods.toarray())

    def weighted_choice(self, objects, weights):
        weights = np.array(weights, dtype=np.float64)
        sum_of_weights = weights.sum()
        np.multiply(weights, 1 / sum_of_weights, weights)
        weights = weights.cumsum()
        x = random()
        for i in range(len(weights)):
            if x < weights[i]:
                return objects[i]
    
    def generate(self, seed, chain_length=15, seed_length=2):
        current_words = seed.split(' ')
        if len(current_words) != seed_length:
            raise ValueError(f'wrong number of words, expected {seed_length}')
        sentence = seed

        for _ in range(chain_length):
            sentence += ' '
            next_word = self.sample_next_word_after_sequence(' '.join(current_words))
            sentence += next_word
            current_words = current_words[1:]+[next_word]
        return sentence
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:40:15 2020

@author: andresparrado
"""
#Importing relevant modules
from linked_list import Nil, LinkedList


#This part is given 
def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)
    return list_of_sentences



#Part of the homeworks
def longest_sentence():
    list_of_sentences = get_list_of_sentences()
    
    #Function to be used to compare sentences
    def biggest(a,b):
        return a if a > b else b
    
    #Counts the number of words in each sentence
    counted_list = list_of_sentences.for_each(len)
    
    #Goes through all sentences and compares them
    longest = counted_list.reduce_right(biggest)
    
    #Prints the longest sentence
    print('The longest sentence contains {:d} words'.format(longest))
    
    #Returns longest sentence
    return longest


#Testing that the code works
test = longest_sentence()
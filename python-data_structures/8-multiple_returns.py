#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    sentence = sentence[0] if sentence else None
    
    return (length,sentence)

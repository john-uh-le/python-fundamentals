"""
Problem

Return frequency of characters.
Input: string
Output: dictionary of char with the total freuency count

"""

def character_frequence(word):
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) +1
    return freq

print (character_frequence("google"))
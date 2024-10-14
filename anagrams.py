# Write your solution here
def anagrams(word1,word2):
    word1 = sorted(word1)
    word2 = sorted(word2)

    return (word1 == word2)

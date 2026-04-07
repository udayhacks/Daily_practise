# Last updated: 07/04/2026, 11:38:20
class Solution:
    def replaceWords(self, dictionary, sentence):
        # Store dictionary words in a set for O(1) lookup
        dict_set = set(dictionary)
        
        # Function to find the root for a given word
        def find_root(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in dict_set:
                    return prefix
            return word

        # Split the sentence into words
        words = sentence.split()
        
        # Transform each word
        transformed_words = [find_root(word) for word in words]
        
        # Reassemble the sentence
        return ' '.join(transformed_words)
# Approach:
# 1. Create a mapping of each character in the given alien order to its index.
# 2. Compare each pair of adjacent words to check if they are in the correct lexicographical order.
# 3. If a word comes after another but should be before it according to the alien dictionary, return False.
# 4. If all words are correctly ordered, return True.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Step 1: Create a mapping of each character to its index in the given order
        order_map = {char: index for index, char in enumerate(order)}

        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # Step 3: Compare characters in both words
            for j in range(min_length):
                if word1[j] != word2[j]:  # Found first differing character
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False  # Incorrect order
                    break  # If correct order, stop comparison
            else:
                # If all characters are the same but word1 is longer than word2, it's incorrect order
                if len(word1) > len(word2):
                    return False

        # Step 4: If no incorrect order found, return True
        return True

# Time Complexity: O(N * M), where N is the number of words and M is the max length of a word.
# - We iterate through each word and compare characters, leading to O(N * M).

# Space Complexity: O(1), since we use only a fixed-size dictionary of 26 characters.
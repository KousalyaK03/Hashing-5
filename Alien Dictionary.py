# Approach:
# 1. Build a graph where each node is a character, and a directed edge (u -> v) means u comes before v.
# 2. Determine character precedence by comparing adjacent words.
# 3. Use topological sorting (Kahn’s Algorithm or DFS) to determine the correct order.
# 4. If there is a cycle (invalid order), return an empty string.
# 5. Otherwise, return the characters in the determined order.

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Initialize graph structures
        graph = defaultdict(set)  # Adjacency list for precedence relations
        in_degree = {char: 0 for word in words for char in word}  # Track in-degrees of each character

        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # Check for invalid ordering (prefix issue)
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            # Compare characters and determine precedence
            for j in range(min_length):
                if word1[j] != word2[j]:  
                    if word2[j] not in graph[word1[j]]:  # Avoid duplicate edges
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1  # Increase in-degree of dependent character
                    break  # Stop at first difference

        # Step 3: Perform Topological Sorting using Kahn's Algorithm (BFS)
        queue = deque([char for char in in_degree if in_degree[char] == 0])  # Enqueue characters with 0 in-degree
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            # Reduce in-degree of neighbors and add to queue if they reach 0 in-degree
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if valid ordering exists (cycle detection)
        if len(order) != len(in_degree):
            return ""  # Cycle detected, invalid order

        return "".join(order)  # Return the valid order

# Time Complexity: O(C), where C is the total number of characters across all words.
# - Building the graph takes O(C).
# - Topological sorting takes O(C).

# Space Complexity: O(1), since the total number of unique characters is limited to 26.
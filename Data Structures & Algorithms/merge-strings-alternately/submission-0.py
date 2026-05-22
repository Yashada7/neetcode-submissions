class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        output = []
        for i in range(min_len):
            output.append(word1[i])
            output.append(word2[i])
        output.append(word1[min_len:])
        output.append(word2[min_len:])
        return ''.join(output)
        
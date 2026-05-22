class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        while True:
            first = strs[0]
            for words in strs:
                try:
                    if words[i] == first[i]:
                        first = words
                    else:
                        return prefix
                except IndexError:
                    return prefix
            prefix += first[i]
            i += 1
        return prefix
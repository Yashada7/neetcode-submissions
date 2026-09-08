class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dictionary_for_mapping ={')':'(','}':'{',']':'['}
        for char in s:
            if char in dictionary_for_mapping:
                if stack and stack[-1]==dictionary_for_mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answers = [0] * n
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                previous_index = stack.pop()
                answers[previous_index] = index - previous_index
            stack.append(index)
        return answers
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result
        
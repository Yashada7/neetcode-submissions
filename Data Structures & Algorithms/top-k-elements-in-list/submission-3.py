class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1
        output=[]
        for key,value in sorted(count.items(), key = lambda x:x[1], reverse = True):
            output.append(key)
        return output[:k]
        
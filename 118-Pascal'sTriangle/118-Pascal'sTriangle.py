# Last updated: 7/17/2025, 1:18:48 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        cur = [1]
        res = [cur]
        for k in range(numRows-1):
            temp1 = cur + [0]
            temp2 = [0] + cur
            cur = [sum(x) for x in zip(temp1, temp2)]
            res.append(cur)
        return res
        
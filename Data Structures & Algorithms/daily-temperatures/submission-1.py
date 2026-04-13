class Solution:
    def dailyTemperatures(self, tmp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(tmp)

        for i in range(len(tmp)):
            while stack and tmp[i] > tmp[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx

                #sdsfdaf
            stack.append(i)
        return res


                

        
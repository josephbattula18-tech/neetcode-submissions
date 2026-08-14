class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temperatures whose may have greater ones,we store index and days
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            current_temp=temperatures[i]
            while len(stack)>0 and current_temp>stack[-1][1]:
                prev_i=stack[-1][0]
                prev_temp=stack[-1][1]
                stack.pop()
                day=i-prev_i
                res[prev_i]=day
            stack.append([i,current_temp])
        return res

        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        cnt = 0
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                a = stack.pop()
                result[a] = i-a
            
            stack.append(i)
            
        return result
'''
high = last element of the temperatures 28
count=1
loop through backwards:
    if you find a value higher than high:
        update high
        append output with count
    else:
        increment the count
    if the output is not updated then update it to 0

'''
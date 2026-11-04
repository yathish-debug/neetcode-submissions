class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        valid_parentheses = { ')':'(',
                              '}':'{',
                              ']':'['
        }
        stack = []
        stack.append(s[0])
        i=1
        while i<len(s):
            if stack and (s[i]== ')' or s[i]=='}' or s[i]==']') :
                if stack[-1] == valid_parentheses[s[i]]:
                    stack.pop()
                    i+=1
                else:
                    return False
            else:
                stack.append(s[i])
                i+=1
        return len(stack)==0   

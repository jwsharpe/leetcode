class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ele in s:
            if ele in parenMap:
                if len(stack) == 0:
                    return False
                if parenMap[ele] != stack.pop():
                    return False
            else:
                stack.append(ele)

        return len(stack) == 0

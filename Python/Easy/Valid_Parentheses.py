class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        pairs={'(':')', '{':'}', '[':']'}
        for c in s:
            if c in pairs:
                stack.append(c)
            elif stack:
                target=stack.pop()
                if c!=pairs.get(target):
                    return False
            else:
                return False
        return not stack

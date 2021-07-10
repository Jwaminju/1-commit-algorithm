class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'()',
            '}':'{',
            ']':'[]',
        }
        for char in s:
            if char not in table:  # 키를 검사
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
        

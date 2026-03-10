class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing → opening
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # If it's an opening bracket, push
            if ch in "([{":
                stack.append(ch)
            else:
                # If stack empty or mismatch → invalid
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()

        # Valid only if nothing left unmatched
        return len(stack) == 0